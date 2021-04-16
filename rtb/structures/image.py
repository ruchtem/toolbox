import numpy as np
import itertools


try:
    from PIL import Image as PImage
except ImportError:
    raise ImportError("Please install PIL to use this module.")


"""Colors that can be used to display segmentation masks"""
COLORS = [
    [128,  64, 128],
    [244,  35, 232],
    [ 70,  70,  70],
    [102, 102, 156],
    [190, 153, 153],
    [153, 153, 153],
    [250, 170,  30],
    [220, 220,   0],
    [107, 142,  35],
    [152, 251, 152],
    [ 0, 130, 180],
    [220,  20,  60],
    [255,   0,   0],
    [  0,   0, 142],
    [  0,   0,  70],
    [  0,  60, 100],
    [  0,  80, 100],
    [  0,   0, 230],
    [119,  11,  32]
]

color_iter = itertools.cycle(COLORS)


MAX_CATEGORIES = 40


class Image(PImage.Image):
    """
    Extend the PIL Image to handle more datatypes.
    """

    def __init__(self, image: PImage.Image) -> None:
        super().__init__()
        self.__dict__.update(image.__dict__)


    def fromarray(obj, channel_pos=2, mode=None):
        if channel_pos < 2:
            obj = np.moveaxis(np.array(obj), channel_pos, 2)

        try:
            return Image(PImage.fromarray(obj, mode))
        except TypeError:
            a = np.array(obj)

            # Segmentation?
            if a.dtype in ['int64', 'int32', 'int16', 'bool']:

                # int encoding?
                if a.ndim == 2 or (a.ndim == 3 and a.shape[-1] == 1):
                    if len(np.unique(a)) < MAX_CATEGORIES:
                        image = np.zeros((a.shape[0], a.shape[1], 3), dtype='int8')
                        for c in np.unique(a):
                            if c == 0:
                                continue
                            image[a == c] = next(color_iter)
                        return Image(PImage.fromarray(image, mode='RGB'))
                # channel encoding?
                elif a.ndim == 3 and a.max() == 1 and a.shape[-1] < MAX_CATEGORIES:
                    image = np.zeros((a.shape[0], a.shape[1], 3), dtype='int')
                    for mask in np.moveaxis(a, -1, 0):
                        image[mask.bool()] = next(color_iter)
                    return Image(PImage.fromarray(image))
            
            elif a.shape[-1] > 3:
                raise TypeError(f"Don't know how to display float image with shape {a.shape}")
            
            # Fallback: normalize to 0, 1
            a = (a - a.min()) / (a.max() - a.min()) * 255
            return Image(Image.fromarray(a.astype('int8'), mode='RGB'))


    def show(self):
        """Matplotlib is much more nicer to display images."""
        try:
            import matplotlib.pyplot as plt
            plt.imshow(np.array(self))
            plt.show()
        except ImportError:
            super().show()
