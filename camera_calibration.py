import cv2
import numpy as np
import glob
import os

# ================= 配置区 =================
# 1. 棋盘格内角点数目 (列数, 行数)
CHECKERBOARD = (9, 6) 

# 2. 单个正方形格子的物理边长 (单位: mm)
SQUARE_SIZE = 20.0  

# 3. 存放标定图片的文件夹路径
IMAGE_DIR = '/home/swust/机械臂/pictures' 
# ==============================================

def calibrate():
    # 停止准则：角点亚像素精确化的迭代中止条件 (最大迭代30次或精度达到0.001)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    # 准备世界坐标系中的 3D 点，如 (0,0,0), (20,0,0), (40,0,0) ... (单位: mm)
    # 假设标定板放在 Z=0 的平面上
    objp = np.zeros((CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
    objp[:, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)
    objp = objp * SQUARE_SIZE

    # 用于存储所有图像的对象点和图像点的数组
    objpoints = [] # 真实世界中的 3D 点
    imgpoints = [] # 图像平面中的 2D 像素点

    # 读取文件夹下所有的 jpg 或 png 图片
    images = glob.glob(os.path.join(IMAGE_DIR, '*.jpg')) + glob.glob(os.path.join(IMAGE_DIR, '*.png'))
    
    if len(images) == 0:
        print(f"在 {IMAGE_DIR} 中没有找到图片，请检查路径！")
        return

    print(f"找到 {len(images)} 张图片，开始提取角点...")
    
    gray = None
    success_count = 0

    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 寻找棋盘格内角点
        ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, None)

        # 如果找到了，就添加对象点和图像点
        if ret == True:
            objpoints.append(objp)
            
            # 亚像素级角点检测，提高精度
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)
            
            # (可选) 在图像上绘制并显示角点，方便确认提取是否正确
            cv2.drawChessboardCorners(img, CHECKERBOARD, corners2, ret)
            cv2.imshow('Find Corners', cv2.resize(img, (800, 600)))
            cv2.waitKey(1000) # 闪烁显示 100ms
            success_count += 1
        else:
            print(f"图片 {fname} 未能识别出所有角点，已跳过。")

    cv2.destroyAllWindows()

    if success_count < 10:
        print("成功提取角点的图片少于10张，标定可能不准确，建议重拍！")
        return

    print(f"成功提取了 {success_count} 张图片的角点，正在计算内参矩阵...")

    # 执行核心标定算法
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    # 评估标定误差 (重投影误差)
    mean_error = 0
    for i in range(len(objpoints)):
        imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
        error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
        mean_error += error
    total_error = mean_error / len(objpoints)

    print("\n" + "="*40)
    print("标定完成！")
    print(f"重投影误差 (RMS Error): {total_error:.4f} 像素")
    if total_error < 0.5:
        print(" -> 评级：极佳！你的相机标定非常完美。")
    elif total_error < 1.0:
        print(" -> 评级：良好。可以用于日常机械臂抓取。")
    else:
        print(" -> 评级：较差。误差大于1像素，建议检查照片是否模糊，或重新拍照标定。")

    print("\n相机内参矩阵 (Camera Matrix):")
    print(mtx)
    print("\n畸变系数 (Distortion Coefficients):")
    print(dist)
    print("="*40)

    # 保存参数供后续使用
    np.save('camera_matrix.npy', mtx)
    np.save('dist_coeffs.npy', dist)
    print("\n参数已保存为 'camera_matrix.npy' 和 'dist_coeffs.npy'")

if __name__ == '__main__':
    calibrate()