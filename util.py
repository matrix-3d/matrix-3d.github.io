import cv2

def resize_video_to_match_height(video1_path, video2_path, output_path):
    # 获取视频1的高度
    cap1 = cv2.VideoCapture(video1_path)
    ret1, frame1 = cap1.read()
    if not ret1:
        raise ValueError("无法读取视频1")
    height1 = frame1.shape[0]
    cap1.release()

    # 打开视频2
    cap2 = cv2.VideoCapture(video2_path)
    width2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
    height2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps2 = cap2.get(cv2.CAP_PROP_FPS)
    fourcc = int(cap2.get(cv2.CAP_PROP_FOURCC))
    frame_count2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

    # 计算新宽度，保持宽高比
    ratio = height1 / height2
    new_width = int(width2 * ratio)
    new_height = height1

    # 使用H264编码格式
    fourcc = cv2.VideoWriter_fourcc(*'avc1')  # H264编码

    # 输出视频
    out = cv2.VideoWriter(output_path, fourcc, fps2, (new_width, new_height))

    for _ in range(frame_count2):
        ret, frame = cap2.read()
        if not ret:
            break
        resized_frame = cv2.resize(frame, (new_width, new_height))
        out.write(resized_frame)

    cap2.release()
    out.release()

# 示例用法
resize_video_to_match_height('/Users/jiaqichen/Documents/YS-IMTech.github.io/arthurhero.github.io/projects/llrm/static/video/52_3.mp4', 
                             '/Users/jiaqichen/Documents/YS-IMTech.github.io/arthurhero.github.io/projects/llrm/static/video/52_33.mp4', 
                             '/Users/jiaqichen/Documents/YS-IMTech.github.io/arthurhero.github.io/projects/llrm/static/video/52_33_resize.mp4')