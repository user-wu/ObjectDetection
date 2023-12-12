# ... （之前的代码保持不变）
import json
import os

labelme_folder = 'data/bowl/annotations/'
output_folder = 'data/bowl/labels/'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for i in range(1, 247):
    json_filename = f"{i}.json"
    labelme_json_path = os.path.join(labelme_folder, json_filename)
    output_path = os.path.join(output_folder, f"{i}.txt")

    if os.path.exists(labelme_json_path):
        with open(labelme_json_path, 'r') as f:
            data = json.load(f)

        img_width = data['imageWidth']
        img_height = data['imageHeight']

        with open(output_path, 'w') as out_file:
            for shape in data['shapes']:
                label = shape['label']
                points = shape['points']

                x_center = (points[0][0] + points[1][0]) / 2.0 / img_width
                y_center = (points[0][1] + points[1][1]) / 2.0 / img_height
                box_width = abs(points[1][0] - points[0][0]) / img_width
                box_height = abs(points[1][1] - points[0][1]) / img_height

                out_file.write(f"{0} {x_center} {y_center} {box_width} {box_height}\n")

            # Remove the line containing the file name information
            with open(output_path, 'r+') as file:
                lines = file.readlines()
                file.seek(0)
                file.truncate()
                file.writelines(lines[:-1])  # Write all lines except the last one (the file name)
