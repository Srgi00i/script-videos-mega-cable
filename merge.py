#!/usr/bin/env python
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

# numero de segmentos totales a tener en cuenta (originales + editados)
MAX_SEGMENTS = 7
# array de clips
VIDEO_CLIPS = []

def main():
    # se cargan los videos
    for i in range(MAX_SEGMENTS):
        # si el id es par, es un clip original
        if (i % 2) == 0:
            VIDEO_CLIPS.append(VideoFileClip(f"original/{i}/{i}.mp4"))
        # si por el contrario es impar, se trata de un fragmento editado
        else:
            video_clip_aux = VideoFileClip(f"altered/{i}/{i}.mp4")
            audio_clip_aux =AudioFileClip(f"altered/{i}/{i}.mp3")

            VIDEO_CLIPS.append(video_clip_aux.set_audio(audio_clip_aux))

    final_video = concatenate_videoclips(VIDEO_CLIPS)

    # Write the final video with the added audio
    final_video.write_videofile("final_video.mp4")

    # Close the clips
    for i in VIDEO_CLIPS:
        i.close()

if __name__ == "__main__":
    main()
