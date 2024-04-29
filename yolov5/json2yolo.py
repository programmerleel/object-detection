# -*- coding: utf-8 -*-
# @Time    : 2024/4/28/028 21:21
# @Author  : Shining
# @File    : json2yolo.py
# @Description : 转换数据

import os
import json

path = r"D:\project\license-plate-recognition\assets\Annotations"
path_ = r"D:\resource\SODA-D"

for txt in os.scandir(path):
    txt_name = txt.name
    txt_path = txt.path
    txt_file = open(txt_path,"r")

    new_txt_path = os.path.join(path_,txt_name[0:-4] + ".txt")
    new_txt_file = open(new_txt_path,"a")

    data = json.load(txt_file)
    # print(data.keys())
    # print(data["images"][0])
    # print(data["annotations"][0])
    # exit()
    # print(data.keys())
    images_datas = data["images"]
    annotations_datas = data["annotations"]
    print(annotations_datas)
    categories_data = data["categories"]
    # print(categories_data)
    exit()
    for image_data in images_datas:
        file_name = image_data["file_name"]
        file_path = os.path.join(r"D:\resource\SODA-D\Images",file_name)
        new_txt_file.write(file_path + "\n")
        # print(r"D:/resource/SODA-D/Annotations" + file_name[0:-4] + ".txt","a")
        # exit()
        file = open(r"D:/resource/SODA-D/Annotations/{}".format(file_name[0:-4] + ".txt"),"a")
        id = image_data["id"]
        for annotation_data in annotations_datas:
            if annotation_data["image_id"] == id:
                height,width = int(image_data["height"]),int(image_data["width"])
                box = annotation_data["bbox"]
                x,y,w,h = (box[2]/width)/2+box[0]/width,(box[3]/height)/2+box[1]/height,box[2]/width,box[3]/height
                category_id = int(annotation_data["category_id"])-1
                file.write("{} {} {} {} {}\n".format(category_id,x,y,w,h))

