import os

folder_path = 'data/bowl/images/'  # 更换为你的文件夹路径
output_file = 'data/bowl/all.txt'    # 输出文件名

with open(output_file, 'w') as file:
    for filename in os.listdir(folder_path):
        file.write(filename + '\n')
