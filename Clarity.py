import cv2
import os
import numpy as np

def DummyClarityMetric(img):
    img_focus = img.get_focus()
    focus_to_clarity = {
        -3.0 : 10,
        -2.5 : 10.5,
        -2.0 : 11,
        -1.5 : 11.5,
        -1.0 : 12,
        -0.5 : 12.5,
        0 : 13,
        0.5 : 12.5,
        1.0 : 12,
        1.5 : 11.5,
        2.0 : 11,
        2.5 : 10.5,
        3.0 : 10
    }
    return focus_to_clarity[img_focus]

if __name__ == "__main__":
    c = DummyClarityMetric

            



