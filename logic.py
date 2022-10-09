import cv2
import numpy as np

def inccont(x,n):

    img = cv2.imread(x, 1)

    clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))

    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB) 
    l, a, b = cv2.split(lab) 

    l2 = clahe.apply(l) 

    lab = cv2.merge((l2,a,b)) 
    img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR) 
    cv2.imwrite('CImages/'+str(n)+'.jpg', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    pc1(n)

def pc1(n):
    a=str(n)+'.jpg'

    image = cv2.imread('CImages/'+a)

    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

    cv2.imwrite('OPV1Images/'+a,thresh)
    if dets(n):
        pc2(n)
    else:
        cv2.imwrite('FOPImages/'+a,thresh)
        print('Completed OPV1')

def dets(n):
    img=cv2.imread("OPV1Images/"+str(n)+".jpg")

    b = np.sum(img == 0)
    w = np.sum(img == 255)

    if b > (w//2):
        return True
    else:
        return False

def pc2(n):
    i=cv2.imread('OPV1Images/'+str(n)+'.jpg')
    ig=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    ie=cv2.equalizeHist(ig)

    fs=cv2.saliency.StaticSaliencyFineGrained_create()
    x,fsm=fs.computeSaliency(ie)

    fsm=(fsm*255).astype('uint8')
    tm=cv2.threshold(fsm.astype('uint8'),0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    itm=cv2.bitwise_not(tm)

    cv2.imwrite('OPV2Images/'+str(n)+'.jpg',itm)
    cv2.waitKey(0)
    print("Completed OPV2")

    cv2.imwrite('FOPImages/'+str(n)+'.jpg',itm)
    