import cv2
import time
import os
input_video = r'D:\伽易公司\地铁惯性导航\测试视频\12-16测试视频\VID_20211216_011509.mp4'
output_dir = r'D:\screenshot2\sc'

import cv2

START_TIME= 0 #设置开始时间(单位秒)
END_TIME= 4602 #设置结束时间(单位秒)

vidcap = cv2.VideoCapture(input_video)

fps = int(vidcap.get(cv2.CAP_PROP_FPS))     # 获取视频每秒的帧数
# fps = 3
print("fps: ", fps)

frameToStart = START_TIME*fps + 23               #开始帧 = 开始时间*帧率
print("frameToStart: ", frameToStart)
frametoStop = END_TIME*fps                  #结束帧 = 结束时间*帧率
print("frameToStop: ", frametoStop)
#
vidcap.set(cv2.CAP_PROP_POS_FRAMES, frameToStart) #设置读取的位置,从第几帧开始读取视频
print(vidcap.get(cv2.CAP_PROP_POS_FRAMES))  # 查看当前的帧数
#
success,image = vidcap.read()               # 获取第一帧
#
count = 0
seconds = 1
while success and frametoStop >= count:
    if count % (fps*seconds) == 0:          # 每second秒保存一次
        save_path = output_dir + str(count) + ".jpg"
        print(save_path)
        cv2.imwrite(save_path, image)       # 保存图片
        print('Process %dth seconds: ' % int(count / (fps*seconds)), success)
    success,image = vidcap.read()           # 每次读取一帧
    count += 1
#
print("end!")
