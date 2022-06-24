#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 07:49:36 2022

@author: winter
"""

import numpy as np
from scipy.ndimage import convolve1d
from scipy.signal import firwin, welch
import requests
from PIL import Image, ImageEnhance
import pytesseract

def remove_lines(image, distortion_freq=None, num_taps=65, eps=0.025):
  """Removes horizontal line artifacts from scanned image.
  Args:
    image: 2D or 3D array.
    distortion_freq: Float, distortion frequency in cycles/pixel, or
      `None` to estimate from spectrum.
    num_taps: Integer, number of filter taps to use in each dimension.
    eps: Small positive param to adjust filters cutoffs (cycles/pixel).
  Returns:
    Denoised image.
  """
  image = np.asarray(image, float)
  if distortion_freq is None:
    distortion_freq = estimate_distortion_freq(image)

  hpf = firwin(num_taps, distortion_freq - eps,
               pass_zero='highpass', fs=1)
  lpf = firwin(num_taps, eps, pass_zero='lowpass', fs=1)
  return image - convolve1d(convolve1d(image, hpf, axis=0), lpf, axis=1)

def estimate_distortion_freq(image, min_frequency=1/25):
  """Estimates distortion frequency as spectral peak in vertical dim."""
  f, pxx = welch(np.reshape(image, (len(image), -1), 'C').sum(axis=1))
  pxx[f < min_frequency] = 0.0
  return f[pxx.argmax()]

download = requests.get('https://secure.thefreedictionary.com/access/image-rnd.ashx?0.8241203757116862')
file = open("captca_image.png", "wb")
file.write(download.content)
file.close()
img = Image.open('captcha_image.png')
filter = ImageEnhance.Contrast(img)
new_image = filter.enhance(3)
remove_lines(new_image)
text = pytesseract.image_to_string(new_image)

