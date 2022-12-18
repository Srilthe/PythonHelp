#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 04:13:23 2022

@author: srilthe

You'll need a __init__.py file in directory to import
ie:  from TKCV import converter as ct
"""


import cv2
import numpy as np
from PIL import Image, ImageTk

class converter:
    def CVtoTK(img):
        b,g,r = cv2.split(img)
        img = cv2.merge((r,g,b))
        im = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=im)
        return (imgtk)

    def CVtoTKgrey(img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        b,g,r = cv2.split(img)
        img = cv2.merge((r,g,b))
        im = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=im)
        return (imgtk)

    def TKtoCV(img):
        img_tk = np.array(img)
        b, g, r = cv2.split(img_tk)
        img = cv2.merge((r, g, b))
        imgcv = cv2.cvtColor(img, 1)
        return (imgcv)

    def TKtoCVgrey(img):
        img_tk = np.array(img)
        b, g, r = cv2.split(img_tk)
        img = cv2.merge((r, g, b))
        imgcv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return (imgcv)
