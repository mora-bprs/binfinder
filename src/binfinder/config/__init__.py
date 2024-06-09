"""configuration file"""

# initialized values

TARGET_SIZE = 320
TARGET_WIDTH = 480
TARGET_HEIGHT = 320
# TARGET_WIDTH = TARGET_SIZE
# TARGET_HEIGHT = TARGET_SIZE


SELECTED_MODEL = 0  # default model


# model values
C_FASTSAMX = 0
C_FASTSAMS = 1
C_SAM = 2


# availability values
TEST_DATASET_AVAILABLE = False
FASTSAM_WEIGHTS_AVAILABLE = False


DETAILED_LOGS = True  # True for detailed logs
DEFAULT_COLORS = False  # True for not overriding your colors
RESET_FASTSAM = False  # True to reset FastSAM repo
RESET_DATASET = False  # True to reset box_train dataset
RESET_WEIGHTS = False  # True to reset weights
