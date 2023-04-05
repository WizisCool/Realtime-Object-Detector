import cv2
import numpy as np

# 调用摄像头
cap = cv2.VideoCapture(0)

while True:
    # 获取视频流的帧
    ret, frame = cap.read()

    # 对帧进行处理，转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 对灰度图像进行高斯模糊处理
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # 使用Canny算子进行边缘检测
    edges = cv2.Canny(gray, 50, 150)

    # 对边缘进行形态学操作，平滑边缘
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    # 寻找边缘中的轮廓
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 绘制轮廓
    for contour in contours:
        # 获取轮廓的矩形边界框和轮廓面积
        x, y, w, h = cv2.boundingRect(contour)
        area = cv2.contourArea(contour)

        # 如果轮廓面积大于一定的阈值，就认为该物体是主要物体，然后给它描边
        if area > 30:
            # 获取轮廓的近似多边形
            epsilon = 0.02 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            # 绘制轮廓
            cv2.drawContours(frame, [approx], 0, (0, 0, 255), 3)

    # 显示帧
    cv2.imshow('frame', frame)

    # 如果按下q键，退出程序
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
