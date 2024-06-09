import os

ROOT = os.getcwd()
TEST_DATASET_PATH = f"{ROOT}/data/test"
WEIGHTS_PATH = f"{ROOT}/data/weights"
SAM_CHECKPOINT = f"{WEIGHTS_PATH}/sam_vit_h_4b8939.pth"
FASTSAMX_CHECKPOINT = f"{WEIGHTS_PATH}/FastSAM-x.pt"
FASTSAMS_CHECKPOINT = f"{WEIGHTS_PATH}/FastSAM-s.pt"
SAVE_PATH = f"{ROOT}/data/result/annotate/plt_img.jpg"
