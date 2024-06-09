import shlex
import sys
import time

import cv2

from binfinder import *
from binfinder.config import SELECTED_MODEL
from binfinder.helpers import (
    annotate_frame_with_mask,
    load_model,
)
from binfinder.helpers.camera import list_working_ports


def main() -> int:
    """main func"""
    # device = get_device()
    device = "cpu"
    model = load_model(SELECTED_MODEL)
    # define the camera index
    working_ports = list_working_ports()
    if len(working_ports) > 1:
        log(bg("more than one working camera ports found!"))
        camera_index = int(input(bp(f"enter the camera index you want to use {working_ports}: ")))
    else:
        camera_index = working_ports[0]

    # opening video capture stream
    vcap = cv2.VideoCapture(camera_index)
    if not vcap.isOpened():
        print(br("[exiting]: error accessing webcam stream."))
        exit(0)

    fps_input_stream = int(vcap.get(cv2.CAP_PROP_FPS))
    print(bg("fps of webcam hardware/input stream:"), fps_input_stream)

    # Reading single frame for initialization/hardware warm-up
    grabbed, frame = vcap.read()

    # Processing frames in input stream
    num_frames_processed = 0
    start = time.time()

    while True:
        grabbed, frame = vcap.read()
        if not grabbed:
            log(br("[exiting] no more frames to read"))
            break

        # Adding a delay for simulating time taken for processing a frame
        try:
            # box_corners_dict = get_box_coordinates(frame, model, device, False, False, False)
            # print(box_corners_dict)

            # TO PLOT THE BOX CORNERS
            # annotated_frame = get_image_with_box_corners(frame, box_corners_dict)  # in RGB

            # TO PLOT THE MASK
            annotated_frame = annotate_frame_with_mask(frame, model, device, False, False, False)
            num_frames_processed += 1

            cv2.imshow(f"stream from camera {camera_index}", annotated_frame)

        except ValueError:  # No box is detected
            cv2.imshow(f"stream from camera {camera_index}", frame)

        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    end = time.time()

    # Printing time elapsed and FPS
    elapsed = end - start
    fps = num_frames_processed / elapsed
    print(by("fps:", fps), "|", bb("elapsed time:", elapsed), "|", bg("frames processed:", num_frames_processed))

    # Releasing input stream, closing all windows
    vcap.release()
    cv2.destroyAllWindows()
    # phrase = shlex.join(sys.argv)j
    # print(phrase)
    return 0


if __name__ == "__main__":
    try:
        main()
        sys.exit(main())
    except KeyboardInterrupt:
        print("")
        log("interrupted by user")
        sys.exit(1)
