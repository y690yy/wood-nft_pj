# -*- coding: utf-8 -*-

import cv2
import cv2.aruco as aruco
import os

directory = 'aruco_generater/aruco_generated'  # select directory file
num_markers = 2  # number of marker

def find_next_marker_id(directory, prefix='aruco_'):
    """指定ディレクトリ内で最も大きな連番IDを探し、次のIDを返す"""
    max_id = -1
    for filename in os.listdir(directory):
        if filename.startswith(prefix) and filename.endswith('.png'):
            try:
                file_id = int(filename[len(prefix):-4])
                max_id = max(max_id, file_id)
            except ValueError:
                continue
    return max_id + 1

# アルコマーカーの生成と保存
def generate_aruco_markers(directory, num_markers):
    # アルコマーカーの辞書を指定 (5x5)
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_5X5_1000)
    # マーカーのサイズを指定
    marker_size = 300
    
    # 次のマーカーIDを見つける
    next_id = find_next_marker_id(directory)

    # 指定された数のマーカーを生成
    for i in range(next_id, next_id + num_markers):
        marker_image = aruco.generateImageMarker(aruco_dict, i, marker_size)
        file_path = os.path.join(directory, f'aruco_{i}.png')
        cv2.imwrite(file_path, marker_image)
        print(f'Marker {i} saved at {file_path}')

# スクリプトを実行
if __name__ == '__main__':
    generate_aruco_markers(directory, num_markers)



