import cv2
import numpy as np


class Filters:
    Kernels = {
        "original": np.array(
            [[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=np.float32),
        "blur": np.array(
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]], dtype=np.float32) / 9,
        "gaussian blur": np.array(
            [[1, 2, 1], [2, 4, 2], [1, 2, 1]], dtype=np.float32) / 16,
        "sharpen": np.array(
            [[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32),
        "sobel (x)": np.array(
            [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32),
        "sobel (y)": np.array(
            [[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32),
        "edge detection": np.array(
            [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], dtype=np.float32),
        "emboss": np.array(
            [[-2, -1, 0], [-1, 1, 1], [0, 1, 2]], dtype=np.float32)
    }

    

    def __init__(self, kernels=Kernels):
        self.kernels = kernels
        self.names = list(self.kernels.keys())
        # bTODO: Implement internal variables
        self._index = 0

    def apply_filter(self, frame, filter_name) -> np.array:
        # TODO: Apply the selected filter kernel to the frame
        # pass
        kernel = self.kernels[filter_name]
        return cv2.filter2D(frame, -1, kernel)

    def get_current_filter_name(self) -> str:
        # TODO: Return currently set kernels's name
        # pass
        
        return self.names[self._index]


    def switch_next_filter(self):
        # TODO: Update currently selected kernel to the next
        if self._index < len(self.kernels) -1 :
            self._index += 1
        else:
            self._index = 0

    def switch_previous_filter(self):
        # TODO: Update currently selected kernel to the previous
        # pass
        if self._index > 0:
            self._index -= 1
        else:
            self._index = len(self.kernels ) - 1
