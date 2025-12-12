import cv2 as cv

events = [i for i in dir(cv) if 'EVENT' in i]
print("\n-----------------\n|    Events     |\n-----------------")
print( events )

print("\n-----------------\n|  Color Flags  |\n-----------------")
flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print( flags )