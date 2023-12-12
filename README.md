# ObjectDetection
自定义类别目标检测通用步骤，Pytorch实现。

文件目录：

<img width="318" alt="image" src="https://github.com/user-wu/ObjectDetection/assets/67259115/438297ea-4f06-4baa-b338-6d5c5566c840">

# 数据准备
* 首先从网络或自建数据集获取符合需求的目标检测任务的数据；
* 采用流行的标注软件进行标注得到标注文件，此例程采用Labelme软件标注，数据：[data](https://pan.baidu.com/s/13lTKHH1zui6ZCLI_B1YQYg?pwd=jsbe)
  
标注示例图：

 <img width="500" alt="image" src="https://github.com/user-wu/ObjectDetection/assets/67259115/92f05aed-477e-4d4a-9aa4-2ce486532bc7">
 
* 得到标注数据目录格式：

```
|-------------------------------|
|-class  |-annotations |-1.json | 
|        |             |-2.json |
|        |             |-3.json |
|        |----------------------|
|        |-images      |-1.jpg  | 
|        |             |-2.jpg  |
|        |             |-3.jpg  |
|-------------------------------|
```

# 数据格式转换
1_transformat.py实现格式转换功能；

目前有三种主流格式：
* coco格式标注
* Yolo格式的标注
* 标注软件原生标注

各个标注格式的文件一般可以相互转换；

# 数据集划分
* 生成文件名列表 2_file_list.py
* 根据文件名列表划分数据集 3_split_data.py

# 训练验证 
4_train.py

配置文件：[bowl.yaml](https://pan.baidu.com/s/1mYRg4IxCcgvAns7XmRihiA?pwd=pmm1)
```
# Bowl
path: ./data/ # dataset root dir
train: /data/bowl/train.txt  # train images
val: /data/bowl/val.txt # val images

# Classes
names:
  0: Bowl
```
预训练模型：[pretrained_model](https://pan.baidu.com/s/1b90dUBONRNR4WtFrgYfeGw?pwd=ypd5)

采用Yolov8实现 

<img width="800" alt="image" src="https://github.com/user-wu/ObjectDetection/assets/67259115/0690f79c-dd0a-4cb7-9004-56a2bc99e5e0">

yolo运行起来检查是否读取到标签，若不成功检查格式转换的label目录和配置文件是否错误；

查看训练过程：

```
终端切换到当前目录：tensorboard --logdir=runs/detection/train* # *代表当前训练
查看链接：http://localhost:6006/
```

# 测试
5_predict.py

用训练好的模型测试相应图像进行性能评估，[测试图像](https://pan.baidu.com/s/12hkWSMvyoZefjCmNEtc5TQ?pwd=z3ae)
