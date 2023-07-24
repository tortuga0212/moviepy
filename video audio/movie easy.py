import moviepy.editor

video = moviepy.editor.VideoFileClip('Barby.mp4')
audio = video.audio
audio.write_audiofile('Barby.mp3')
