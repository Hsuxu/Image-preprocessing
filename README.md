
# Image-preprocessing
This a python image data augmentation library based on [*opencv*](https://opencv.org/) and [*numpy*](http://www.numpy.org/) for deep learning for persenal usage. This library is compatible with Datagenertor in [*Keras*](https://keras.io/preprocessing/image/) and Dataset in [*PyTorch*](https://pytorch.org/docs/stable/data.html) Any question please 
## Components
- Remove mean
- Fix normalization with mean=[0.48462227599918,  0.45624044862054, 0.40588363755159], std=[0.22889466674951, 0.22446679341259, 0.22495548344775] which is computed from ImageNet.
- Instance normalization(Adaptive normalization
- Adjust contrast
- Random flip up-down left-right
- Crop image with a given size
- Image edge padding 
## Requirements
```Bash
pip install numpy
pip install opencv-python
```
## Installation:
```Bash
python setup.py install
```
