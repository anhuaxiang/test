import numpy as np
import pandas as pd

from imgaug import augmenters as iaa
from PIL import Image


a = Image.open('a.jpg')
b = Image.open('b.jpg')

a_data = np.array(a)
b_data = np.array(b)
images = np.array([a_data, b_data])


seq = iaa.Sequential([
    # iaa.Crop(px=(0, 16)),  # 裁剪
    # iaa.Fliplr(0.5),  # 水平翻转50%的图片
    # iaa.Flipud(0.5),  # 垂直翻转50%的图片
    # iaa.GaussianBlur(sigma=(0, 3.0)),  # 0-3 模糊图像
    # iaa.AverageBlur(k=(2, 7)),  # 模糊图像
    # iaa.MedianBlur(k=(3, 11)),  # 模糊图像
    # iaa.Affine(rotate=(-45, 45)),  # 旋转图片
    # iaa.ContrastNormalization((0.75, 1.5)),  # 对比度
    # iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5),  # 噪声
    # iaa.Multiply((0.8, 1.2), per_channel=0.2),  # 暗, 亮
    # iaa.Superpixels(p_replace=(0, 1.0), n_segments=(20, 200))  # 完全或部分地将图像转换为其超像素表示。
    iaa.Sharpen(alpha=(0, 1.0), lightness=(0.75, 1.5)),  # 图片锐化
    # iaa.Emboss(alpha=(0, 1.0), strength=(0, 2.0)),  #
])
result = seq(images=images)


Image.fromarray(result[0]).show(), Image.fromarray(result[1]).show()