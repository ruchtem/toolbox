import numpy as np
import fvcore.transforms as T
from fvcore.transforms.transform import NoOpTransform, ScaleTransform

__all__ = [
    "CropTransform",
    "ScaleTransform",
    "NoOpTransform",
    "RotationTransform",
]


"""
Deterministic transforms.

Inspired by the great work in `detectron2`.
"""

class RotationTransform(T.Transform):
    """
    Perform rotation using the provided angle
    """

    def __init__(self, h, w, angle, expand=False, interp=None) -> None:
        super().__init__()
        image_center = np.array([w, h]) // 2



        self._set_attributes(locals())


class NormalizeTransform(T.Transform):

    def __init__(self, range=[0, 1]) -> None:
        super().__init__()
        self._set_attributes(locals())
    

    def apply_image(self, img: np.ndarray):
        return (img - img.min()) / (img.max() - img.min()) * self.range[1] + self.range[0]
    

    def apply_coords(self, coords: np.ndarray):
        return coords
    

    def apply_segmentation(self, segmentation: np.ndarray) -> np.ndarray:
        return segmentation
    

    def inverse(self):
        return T.NoOpTransform







# aliases
CropTransform = T.CropTransform
ScaleTransform = T.ScaleTransform
NoOpTransform = T.NoOpTransform
