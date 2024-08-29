from moviepy.editor import AudioFileClip

def extract_audio_segment(input_file, start_time, end_time):
    """
    从MP3文件中截取指定时间段的音频片段并保存为新文件。

    参数:
    - input_file: 输入的MP3文件路径
    - start_time: 开始时间（秒）
    - end_time: 结束时间（秒）
    - output_file: 输出的音频文件路径
    """
    # 读取音频文件
    audio = AudioFileClip(input_file)

    # 截取指定时间段的片段
    extracted_segment = audio.subclip(start_time, end_time)

    # 输出截取的片段
    output_file = input_file.replace(".mp3", f"_{start_time}-{end_time}.mp3")
    extracted_segment.write_audiofile(output_file)

    # 关闭音频文件
    audio.close()
    return output_file

# 示例使用
input_file = "static/videos/98342395564/rank5_4+5xd6f83m45sf28u+够爱（烟嗓版）.mp3"
start_time = 0.02
end_time = 15.3

output_file = extract_audio_segment(input_file, start_time, end_time)
print(f"音频片段已保存到 {output_file}")