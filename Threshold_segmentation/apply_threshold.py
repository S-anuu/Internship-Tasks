import numpy as np

def apply_threshold(image, lower_thres, upper_thres):
    mask = np.logical_and(image >= lower_thres, image <= upper_thres).astype(np.uint8)

    return mask