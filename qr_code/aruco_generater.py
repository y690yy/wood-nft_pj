

import cv2
import cv2.aruco as aruco
import os


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

def generate_aruco_markers(directory, num_markers, marker_size=200):
    """指定された数の ArUco マーカーを生成し、ディレクトリに保存する"""
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

    # ディレクトリが存在しない場合は作成
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # 次のマーカーIDを見つける
    next_id = find_next_marker_id(directory)

    for i in range(next_id, next_id + num_markers):
        marker_image = aruco.generateImageMarker(aruco_dict, i, marker_size)
        file_path = os.path.join(directory, f'aruco_{i}.png')
        cv2.imwrite(file_path, marker_image)
        print(f'Marker ID {i}が{file_path}に保存されました')

# 使用例
directory = 'C:/Users/taise/OneDrive/ドキュメント/GitHub/wood-nft_pj/qr_code/arco_marker'  # 保存先ディレクトリのパスを指定
num_markers = 5  # 生成したいマーカーの数
generate_aruco_markers(directory, num_markers)