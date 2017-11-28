#!/usr/bin/python

import sys
import os
import cv2
import numpy as np

#imagename='rotated.jpg'
imagename='scenetext01.jpg'

img = cv2.imread(imagename,cv2.IMREAD_COLOR)
textRegions=[]
# for visualization
vis      = img.copy()
textRegions.append(vis)
rects=[]
# Extract channels to be processed individually
channels = cv2.text.computeNMChannels(img)
# Append negative channels to detect ER- (bright regions over dark background)
cn = len(channels)-1
for c in range(0,cn):
  channels.append((255-channels[c]))

# Apply the default cascade classifier to each independent channel (could be done in parallel)
print("Extracting Class Specific Extremal Regions from "+str(len(channels))+" channels ...")
print("    (...) this may take a while (...)")
for channel in channels:

  erc1 = cv2.text.loadClassifierNM1('trained_classifierNM1.xml')
  er1 = cv2.text.createERFilterNM1(erc1,16,0.00015,0.13,0.2,True,0.1)

  erc2 = cv2.text.loadClassifierNM2('trained_classifierNM2.xml')
  er2 = cv2.text.createERFilterNM2(erc2,0.5)

  regions = cv2.text.detectRegions(channel,er1,er2)

  rects.append(cv2.text.erGrouping(img,channel,[r.tolist() for r in regions]))

#Visualization
for _rect in rects:
  for rect in _rect:
    cv2.rectangle(vis, (rect[0],rect[1]), (rect[0]+rect[2],rect[1]+rect[3]), (0, 0, 0), 2)
    cv2.rectangle(vis, (rect[0],rect[1]), (rect[0]+rect[2],rect[1]+rect[3]), (255, 255, 255), 1)
    textRegions.append(vis[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]])

'''
vis2=vis.copy()
img2gray = cv2.cvtColor(vis,cv2.COLOR_BGR2GRAY)
thrsh = cv2.adaptiveThreshold(img2gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
vis=thrsh
'''
#Visualization
cv2.imshow("Text detection result", vis)
cv2.waitKey(0)

# cd D:\Desktop\Tempo\opencv_contrib-master\opencv_contrib-master\modules\text\samples
