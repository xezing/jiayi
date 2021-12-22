# 引入模块
from PIL import Image


def cut_img(path, count):
    # 读取原图
    img = Image.open(path)
    print(img.size)

    # 图片剪切crop(x,y,x1,y1)
    im = img.crop((1666 - 323 + 30, 514 - 173, 1758 - 323 -12 , 593 - 173 -30))
    print(im.size)
    im = im.convert('L')

    # 保存剪切出来的图片
    cut_name = r'D:\screenshot3\sc' + str(count) + '.jpg'
    im.save(cut_name)


if __name__ == '__main__':
    count = 0
    while count < 138070:
    # while count < 13:
        path = r'D:\screenshot2\sc' + str(count) + '.jpg'
        cut_img(path, count)
        count += 30
