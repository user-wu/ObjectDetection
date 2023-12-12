import random

filelist = 'data/bowl/all.txt'  # 你的文件名列表文件
train_file = 'data/bowl/train.txt'    # 训练集文件
validation_file = 'data/bowl/val.txt'  # 验证集文件

with open(filelist, 'r') as file:
    filenames = file.read().splitlines()  # 读取文件并获取文件名列表

# 设置训练集和验证集的比例
train_ratio = 0.8  # 训练集比例
validation_ratio = 1 - train_ratio  # 验证集比例

# 随机化文件名顺序
random.shuffle(filenames)

# 计算训练集和验证集的边界索引
train_split = int(len(filenames) * train_ratio)

# 划分训练集和验证集
train_set = filenames[:train_split]
validation_set = filenames[train_split:]

# 将训练集写入文件
with open(train_file, 'w') as train:
    for filename in train_set:
        train.write("./images/"+filename + '\n')

# 将验证集写入文件
with open(validation_file, 'w') as validation:
    for filename in validation_set:
        validation.write("./images/"+filename + '\n')

# 输出训练集和验证集文件名
print("训练集文件:", train_file)
print("验证集文件:", validation_file)
