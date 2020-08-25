from moviepy.editor import *
# clips_gen is function that take the beats array from the beat_gen function
# and a list of strings with the images name or directory and return a liste of synchronised sequences


def clips_gen(beats, img):
    clips = []
    t0 = 0
    j = 0
    for t in beats:
        if j == 3:
            j = 0
        clips.append(ImageClip(img[j]).set_duration(t-t0))
        t0 = t
        j = j+1
    return clips
