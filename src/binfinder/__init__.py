"""this file will be loaded first in the package"""

__version__ = "0.1.1"
import os

import gdown
import yachalk
from questionary import Choice as qc
from questionary import confirm as qf
from questionary import select as qs
from yachalk import chalk as c

from binfinder.config import (
    C_FASTSAMS,
    C_FASTSAMX,
    C_SAM,
    DEFAULT_COLORS,
    DETAILED_LOGS,
    FASTSAM_WEIGHTS_AVAILABLE,
    SELECTED_MODEL,
    TEST_DATASET_AVAILABLE,
)
from binfinder.config.paths import (
    FASTSAMS_CHECKPOINT,
    FASTSAMX_CHECKPOINT,
    ROOT,
    SAM_CHECKPOINT,
    TEST_DATASET_PATH,
    WEIGHTS_PATH,
)

c.enable_full_colors()

by = c.bold.yellow_bright if DEFAULT_COLORS else c.bold.hex("#f0deb2")
br = c.bold.red_bright if DEFAULT_COLORS else c.bold.hex("#df8ca4")
bg = c.bold.green_bright if DEFAULT_COLORS else c.bold.hex("#abd6a0")
bb = c.bold.blue_bright if DEFAULT_COLORS else c.bold.hex("#92b3f4")
bm = c.bold.magenta_bright if DEFAULT_COLORS else c.bold.hex("#dcb6d6")
bc = c.bold.cyan_bright if DEFAULT_COLORS else c.bold.hex("#9cdae9")
bp = c.bold.hex("#c5a7f2")


def log(*args):
    if DETAILED_LOGS:
        print(bc("log:"), *args)


def initial_verification():
    """initial verification"""
    try:
        print(br("--------------------------------------------"))
        print(f"{bg(__name__)} {by(f"v{__version__}")} initializing...")
        if not os.path.exists("src/binfinder/__init__.py"):
            log(br("possible environment misconfiguration"))
            log(bc("please run this script from the root of the project"))
            raise UserWarning()
        print(bc("working directory:"), ROOT)
        if not os.path.exists("data/weights"):
            print("weights not configured")
            raise UserWarning()
        initial_preferences()

        print(br("--------------------------------------------"))
    except:
        print(br("--------------------------------------------"))
        exit(1)


def initial_preferences():
    """get user preferences"""
    try:
        print(bg("--------------------------------------------"))
        SELECTED_MODEL = qs(
            "which model do you want to use?",
            choices=[qc("fastsam-s", C_FASTSAMS), qc("fastsam-x", C_FASTSAMX), qc("sam", C_SAM)],
            use_jk_keys=True,
            use_arrow_keys=True,
            # default=qc("fastsam-s", Model.FASTSAMS),
        ).ask()
        check_weights()
        # TODO: set downscale factor for camera
        # TODO: check if test dataset is available
        print(bg("--------------------------------------------"))
    except:
        print(bg("--------------------------------------------"))
        exit(1)


def check_weights():
    if SELECTED_MODEL == C_FASTSAMS:
        if not os.path.exists(FASTSAMS_CHECKPOINT):
            print(bc("fastsam-s weight not found"))
            if qf("do you want to download?").ask():
                gdown.download(
                    "https://drive.google.com/uc?id=10XmSj6mmpmRb8NhXbtiuO9cTTBwR_9SV",
                    FASTSAMS_CHECKPOINT,
                    quiet=False,
                )
    if SELECTED_MODEL == C_FASTSAMX:
        if not os.path.exists(FASTSAMX_CHECKPOINT):
            print(bc("fastsam-x weight not found"))
            if qf("do you want to download?").ask():
                gdown.download(
                    "https://drive.google.com/uc?id=1m1sjY4ihXBU1fZXdQ-Xdj-mDltW-2Rqv",
                    FASTSAMX_CHECKPOINT,
                    quiet=False,
                )
    if SELECTED_MODEL == C_SAM:
        if not os.path.exists(SAM_CHECKPOINT):
            print(bc("sam weight not found"))
            if qf("do you want to download?").ask():
                print(br("downloading sam weight (this may take a while...)"))
                if not os.system(
                    f"wget -O {SAM_CHECKPOINT} https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth"
                ):
                    print(bg("sam weights downloaded"))


initial_verification()
