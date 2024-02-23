from PIL import Image
import numpy as np
import os

def create_patt_from_png(png_file_path, output_directory, size=(16, 16)):
    # 出力ディレクトリの確認と作成
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    img = Image.open(png_file_path).convert('L')
    img = img.resize(size, Image.ANTIALIAS)
    img_array = np.array(img, dtype=np.uint8)

    # .pattファイルのパスを生成
    base_name = os.path.basename(png_file_path)
    patt_file_name = os.path.splitext(base_name)[0] + '.patt'
    patt_file_path = os.path.join(output_directory, patt_file_name)

    with open(patt_file_path, 'w') as f:
        for y in range(img_array.shape[0]):
            for x in range(img_array.shape[1]):
                normalized_value = img_array[y, x] / 255
                f.write(f'{normalized_value:.4f} ')
            f.write('\n')

def convert_all_pngs_in_directory(source_directory, output_directory):
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.endswith(".png"):
                png_file_path = os.path.join(root, file)
                create_patt_from_png(png_file_path, output_directory)
                print(f'Converted {file} to .patt format and saved in {output_directory}')

# 入力ディレクトリと出力ディレクトリのパスを指定
source_directory = 'aruco_generater/240223_aruco_generated'
output_directory = 'aruco_generater/240223_aruco_generated_patt'

# 指定されたディレクトリ内のすべてのPNGを.pattに変換して、指定された出力ディレクトリに保存
convert_all_pngs_in_directory(source_directory, output_directory)