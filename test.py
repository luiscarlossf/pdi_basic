import cv2 as cv

if __name__=="__main__":
    img = cv.imread("./vieira2.png")
    for i in img:
        print(i)

