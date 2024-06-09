import time

import cv2

from binfinder.helpers import (
    annotate_frame_with_mask,
    get_model,
)
from binfinder.helpers.camera import list_working_ports

# device = get_device()
device = "cpu"

# #######################################
# model_name = input("Enter the model name you want >>> ")
model_name = "fastSAM-s"

model = get_model(model_name)


# define the camera index
working_ports = list_working_ports()
if len(working_ports) > 1:
    print("more than one working camera ports found!")
    camera_index = int(input(f"enter the camera index you want to use {working_ports}: "))
else:
    camera_index = working_ports[0]

# opening video capture stream
vcap = cv2.VideoCapture(camera_index)
if not vcap.isOpened():
    print("[Exiting]: Error accessing webcam stream.")
    exit(0)

fps_input_stream = int(vcap.get(5))
# fps_input_stream = int(vcap.get(cv2.CAP_PROP_FPS))
print("FPS of webcam hardware/input stream:", fps_input_stream)

# Reading single frame for initialization/hardware warm-up
grabbed, frame = vcap.read()

# Processing frames in input stream
num_frames_processed = 0
start = time.time()

while True:
    grabbed, frame = vcap.read()
    if not grabbed:
        print("[Exiting] No more frames to read")
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
print("FPS:", fps, ", Elapsed Time:", elapsed, ", Frames Processed:", num_frames_processed)

# Releasing input stream, closing all windows
vcap.release()
cv2.destroyAllWindows()
