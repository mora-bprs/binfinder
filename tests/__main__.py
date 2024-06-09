import cv2
from binfinder.helpers import (
    get_box_coordinates,
    get_image_with_box_corners,
    load_model,
)

# device = get_device()
device = "cpu"

# #######################################3

print("Choose the model you want to choose")
print("""1) DeepLabv3\n2) Segnet\n3) UNet\n4) CornerNet\n5) fastSAM\n6) fastSAM-s\n7) SAM""")
# model_name = input("Enter the model name you want >>> ")
model_name = "fastSAM-s"

camera_index = 1
model = load_model(model_name)

# # Initialize the video capture object with the index of the webcam (usually 0)
cap = cv2.VideoCapture(camera_index)

while True:
    ret, frame = cap.read()  # Read frame from webcam

    if not ret:
        print("Error: Couldn't read frame.")
        break

    # cv2.imshow("Webcam input", frame)
    # print("frame_shape", frame.shape)

    try:
        box_corners_dict = get_box_coordinates(
            frame, model, device, False, False, False
        )  # it seems like model does not care about the color format , i'm not sure, have to verify???
        annotated_frame = get_image_with_box_corners(frame, box_corners_dict)  # in RGB

        # convert back to BGR
        cv2.imshow("Annotated image", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    except ValueError:
        pass

# Release the capture object and close the window
cap.release()
cv2.destroyAllWindows()
