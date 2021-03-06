import cv2
import pyzbar.pyzbar as pyzbar
import random
import matplotlib
# def nothin(x):
#     pass

# cv2.nameWindow('Barcode')

# img = cv2.imread('C:/project/opencv/barcode/bh.jpg', cv2.IMREAD_COLOR)
img_SEOUL = cv2.imread('C:/project/opencv/barcode/SEOUL.png', cv2.IMREAD_COLOR)
img_BUSAN = cv2.imread('C:/project/opencv/barcode/BUSAN.png', cv2.IMREAD_COLOR)
img_SUWON = cv2.imread('C:/project/opencv/barcode/SUWON.png', cv2.IMREAD_COLOR)
img_DAEGU = cv2.imread('C:/project/opencv/barcode/DAEGU.png', cv2.IMREAD_COLOR)
img_ANDONG = cv2.imread('C:/project/opencv/barcode/ANDONG.png', cv2.IMREAD_COLOR)
img_GOCHANG = cv2.imread('C:/project/opencv/barcode/GOCHANG.png', cv2.IMREAD_COLOR)
img_GUNSAN = cv2.imread('C:/project/opencv/barcode/GUNSAN.png', cv2.IMREAD_COLOR)
img_GOSUNG = cv2.imread('C:/project/opencv/barcode/GOSUNG.png', cv2.IMREAD_COLOR)
img_YESAN = cv2.imread('C:/coding/YESAN.png', cv2.IMREAD_COLOR)

while True:
    choice_random = random.randint(1,9)
    if choice_random == 1:
        cv2.imshow('SEOUL', img_SEOUL)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        gray = cv2.cvtColor(img_SEOUL, cv2.COLOR_BGR2GRAY)  #
        decoded = pyzbar.decode(img_SEOUL)
    elif choice_random ==2:
        cv2.imshow('BUSAN', img_BUSAN)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        gray = cv2.cvtColor(img_BUSAN, cv2.COLOR_BGR2GRAY)
        decoded = pyzbar.decode(gray)
    elif choice_random == 3:
        cv2.imshow('SUWON', img_SUWON)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        gray = cv2.cvtColor(img_SUWON, cv2.COLOR_BGR2GRAY)
        decoded = pyzbar.decode(gray)
    elif choice_random == 4:
        cv2.imshow('DAEGU', img_DAEGU)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        gray = cv2.cvtColor(img_DAEGU, cv2.COLOR_BGR2GRAY)
        decoded = pyzbar.decode(gray)
    elif choice_random == 5:
        cv2.imshow('ANDONG', img_ANDONG)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        gray = cv2.cvtColor(img_ANDONG, cv2.COLOR_BGR2GRAY)
        decoded = pyzbar.decode(gray)
    elif choice_random == 6:
        cv2.imshow('GOCHANG', img_GOCHANG)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        gray = cv2.cvtColor(img_GOCHANG, cv2.COLOR_BGR2GRAY)
        decoded = pyzbar.decode(gray)
    elif choice_random == 7:
        cv2.imshow('GUNSAN', img_GUNSAN)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        gray = cv2.cvtColor(img_GUNSAN, cv2.COLOR_BGR2GRAY)
        decoded = pyzbar.decode(gray)
    elif choice_random == 8:
        cv2.imshow('GOSUNG', img_GOSUNG)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        gray = cv2.cvtColor(img_GOSUNG, cv2.COLOR_BGR2GRAY)
        decoded = pyzbar.decode(gray)
    elif choice_random == 9:
        cv2.imshow('YESAN', img_YESAN)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        gray = cv2.cvtColor(img_YESAN, cv2.COLOR_BGR2GRAY)
        decoded = pyzbar.decode(gray)
    # cv2.imshow(gray, cmap='gray')


    for d in decoded:
        URL = d.data.decode('utf-8')
        if URL == 'SEOUL':
            print('????????? : ??????')
        elif URL == 'BUSAN':
            print('????????? : ??????')
        elif URL == 'SUWON':
            print('????????? : ??????')
        elif URL == 'DAEGU':
            print('????????? : ??????')
        elif URL == 'ANDONG':
            print('????????? : ??????')
        elif URL == 'GOCHANG':
            print('????????? : ??????')
        elif URL == 'GUNSAN':
            print('????????? : ??????')
        elif URL == 'GOSUNG':
            print('????????? : ??????')
        elif URL == 'YESAN':
            print('????????? : ??????')
        else:
            print('????????? ???????????????.')
        # if d == ord('q'):
        #     break