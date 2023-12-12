# ObjectDetection
自定义类别目标检测通用步骤，Pytorch实现。

# 数据准备
* 首先从网络或自建数据集获取符合需求的目标检测任务的数据；
* 采用流行的标注软件进行标注得到标注文件，此例程采用Labelme软件标注；
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
目前有三种主流格式：
* coco格式标注
* Yolo格式的标注
* 标注软件原生标注

各个标注格式的文件一般可以相互转换；
