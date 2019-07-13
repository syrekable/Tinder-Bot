import cv2

def getImage(fname):
    img = cv2.imread(fname,0)
    return img

def threshold(fname):
    img = getImage(fname)
    ret,threshImg = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
    return threshImg