import cv2
import numpy as np

"""
This is a image preprocessing library for personal use
Is there any problems please concat:
Hsuxu820@gmail.com
"""

def remove_mean(image):
    """
    remove RGB mean values which from ImageNet
    input:
        image:  RGB image np.ndarray 
                type of elements is np.uint8
    return:
        image:  remove RGB mean and scale to [0,1] 
                type of elements is np.float32
    """
    mean = [0.48462227599918,  0.45624044862054, 0.40588363755159]
    image = image.astype(np.float32)
    image = np.subtract(np.divide(image, 255.0), mean)
    return image


def standardize(image, mean=[0.48462227599918,  0.45624044862054, 0.40588363755159], std=[0.22889466674951, 0.22446679341259, 0.22495548344775]):
    """
    standardize RGB mean and std values which from ImageNet
    input:
        image:  RGB image np.ndarray 
                type of elements is np.uint8
    return:
        image:  standarded image
                type of elements is np.float32
    """
    image = image.astype(np.float32) / 255.0
    image = np.divide(np.subtract(image, mean), std)
    return image
    
def samele_wise_normalization(data):
    """
    normalize each sample to 0-1
    Input:
        sample image
    Output:
        Normalized sample
    x=1.0*(x-np.min(x))/(np.max(x)-np.min(x))
    """
    data.astype(np.float32)
    if np.max(data) == np.min(data):
        return np.ones_like(data, dtype=np.float32) * 1e-6
    else:
        return 1.0 * (data - np.min(data)) / (np.max(data) - np.min(data))


def contrast_adjust(image, alpha=1.3, beta=20):
    """
    adjust constrast through gamma correction
    newimg = image * alpha + beta
    """
    newimage = image.astype(np.float32) * alpha + beta
    newimage[newimage < 0] = 0
    newimage[newimage > 255] = 255
    return np.uint8(newimage)

def random_flip(image,lr,ud):
    """
    random flip image 
    """
    if lr:
        if np.random.random()>0.5:
            image=cv2.flip(image,flipCode=1)
    if ud:
        if np.random.random()>0.5:
            image=cv2.flip(image,flipCode=0)
    return image

def image_crop(image,crop=None):
    """
    input:
        image: image np.ndarray [H,W,C]
        crop: [target_height,target_width]
    output:
        croped image with shape[crop[0],crop[1],C]
    """
    hei, wid, _ = image.shape
    if crop is None:
        crop = (np.random.randint(int(hei / 2), int(3 * hei / 4)),
                np.random.randint(int(wid / 2), int(3 * wid / 4)))
    th, tw = [int(round(x / 2)) for x in crop]
    return image[th:th + crop[0], tw:tw + crop[0]]
    
