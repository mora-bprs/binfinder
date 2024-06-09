import cv2


def list_working_ports():
    """
    test the ports and returns an array of the working ports
    """
    non_working_ports = []
    dev_port = 0
    working_ports = []
    # available_ports = []
    while len(non_working_ports) < 2:  # if there are more than 2 non working ports stop the testing.
        camera = cv2.VideoCapture(dev_port)
        if not camera.isOpened():
            pass
            non_working_ports.append(dev_port)
            # print("Port %s is not working." % dev_port)
        else:
            is_reading, img = camera.read()
            # w = camera.get(3)
            # h = camera.get(4)
            if is_reading:
                # print("Port %s is working and reads images (%s x %s)" % (dev_port, h, w))
                working_ports.append(dev_port)
            else:
                # print("Port %s for camera ( %s x %s) is present but does not reads." % (dev_port, h, w))
                # available_ports.append(dev_port)
                pass
        dev_port += 1
    return working_ports
