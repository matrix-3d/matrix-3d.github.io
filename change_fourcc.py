import cv2

def resize_video_to_match_height(video2_path, output_path):

    # 打开视频2
    cap2 = cv2.VideoCapture(video2_path)
    width2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
    height2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps2 = cap2.get(cv2.CAP_PROP_FPS)
    fourcc = int(cap2.get(cv2.CAP_PROP_FOURCC))
    frame_count2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

    # 计算新宽度，保持宽高比
    new_width = width2
    new_height = height2

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
    print(f"Processed {frame_count2} frames from {video2_path} to {output_path}")
    cap2.release()
    out.release()

# 示例用法
resize_video_to_match_height('/Users/jiaqichen/Documents/YS-IMTech.github.io/arthurhero.github.io/projects/llrm/static/video/52_4.mp4', 
                             '/Users/jiaqichen/Documents/YS-IMTech.github.io/arthurhero.github.io/projects/llrm/static/video/52_4_resize.mp4')