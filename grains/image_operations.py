#!/usr/bin/env python

def avgColor(myImage, minX, minY, maxX, maxY, pixelArray=None):
  "avgColor returns the average color from a section of a picture"
  if pixelArray==None:
    pixelArray = myImage.load()
  cumulativeCounts = [0, 0, 0]
  pixelsCounted = 0
  for x in range(minX, maxX):
    for y in range(minY, maxY):
      #cumulativeCounts += pixelArray[x, y]
      cumulativeCounts[0] += pixelArray[x, y][0]
      cumulativeCounts[1] += pixelArray[x, y][1]
      cumulativeCounts[2] += pixelArray[x, y][2]
      pixelsCounted += 1
  return [cumulativeCounts[0]/pixelsCounted, cumulativeCounts[1]/pixelsCounted, cumulativeCounts[2]/pixelsCounted]