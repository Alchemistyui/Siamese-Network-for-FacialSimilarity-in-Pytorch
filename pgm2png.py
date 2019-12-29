from PIL import Image
import os
from glob import glob
# path = input_raw("input path")
for i in range(1, 41):
    # print(i)
    path="/Users/Alchemist/Desktop/Facial-Similarity-with-Siamese-Networks-in-Pytorch-master/data/faces/training/s" + str(i)
    # path = "/Users/Alchemist/Downloads/att_faces/s" + str(i)
    # 获取指定目录下的所有pgm文件列表
# print("aaa")
# path="/Users/Alchemist/Desktop/Facial-Similarity-with-Siamese-Networks-in-Pytorch-master/data/faces/testing/s7"
    img_list = glob(os.path.join(path, "*.pgm"))
    # 遍历列表，重新保存为jpg格式
    print(len(img_list))
    for img in img_list:
        filename = img[:-3] + "jpg"
        # os.remove(img)
        # print(filename)
        Image.open(img).save(filename)
        os.remove(img)
        