import cv2
import numpy as np
import os
import glob
import sys
DIM=(1920, 1080)
K=np.array([[518.5206194361012, 0.0, 932.0926791943779], [0.0, 518.0241546073428, 507.22695301062527], [0.0, 0.0, 1.0]])
D=np.array([[-0.09556402717747697], [0.012374049436718767], [-0.010465758469831311], [0.0033159128053917544]])
def undistort(img_path):
    img = cv2.imread(img_path)
    cv2.imshow("original", img)
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    cv2.imshow("undistorted", undistorted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    for p in sys.argv[1:]:
        undistort(p)