from moviepy.editor import *

def extract_mp3(input_file: str):
    # Replace 'input.mp4' with the path to your MP4 file
    #input_file = "input.mp4"
    if not input_file.endswith(".mp4"):
        return

    # Replace 'output.mp3' with the desired output MP3 file path
    output_audio = input_file + ".mp3"

    try:
        # Attempt to load the file as a video file
        clip = VideoFileClip(input_file)

        # If the file is a video, extract the audio
        audio = clip.audio

    except Exception:
        # If the file is not a video file, treat it as an audio file
        audio = AudioFileClip(input_file)

    # Write the audio to an MP3 file
    audio.write_audiofile(output_audio)
    return
