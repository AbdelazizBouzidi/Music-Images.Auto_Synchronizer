from moviepy.editor import *
from clipsGen import clips_gen
from beatMaker import beat_gen
# a list with your images
img = ["0.jpg", "1.png", "2.jpg"] 

# you need your song in both mp3 and wav format
your_song_wav = "Zack Hemsey - The Hands Of An Ape [High quality].wav"
your_song_mp2 = "Zack Hemsey - The Hands Of An Ape.mp3"

# the max number of picture's swaps in 1 second
movement_rate = 15

#a numpy array with the moments where beats happens 
beats = beat_gen(your_song_wav , movement_rate)

#a list with the generated synchronized sequences 
clips = clips_gen(beats, img)

#and finaly the moviepy magic where we putt everything together 
concat_clip = concatenate_videoclips(clips, method="compose")
concat_clip.write_videofile(
    "final.mp4", fps=30, audio=your_song_mp2)
