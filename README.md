# Music-Images.Auto_Synchronizer
This's a simple project that can take a bunch of pictures and a song as an input and automatically synchronize the transitions which result an easy made amazing video 
# Requirements 
in order to run this project you will need to install 3 main libraries:
moviepy,numpy and wave, make sure u have'em before lunching the scripts,
# Ho to use 
you first need to pick a song of your choice, in most of the cases you will have it as a mp3 file, u also need to provide the same file cconverted to a wave format in order to
do the required preprocessing.
the se cond thing you need to do is prearing a set of pictures that you want to use, in my case i used 3 pictures that get reapetedly looped in order to make "Sans" look like he's dancing.
# how does it work 
the beat_gen function take the wave file you provided and the swaprate and generate a numpy array that contain the moments where we have local minimus
these local ares are defined using the swaprate you defined, the density of the sound and the sampling frequency of your song,
after generating this array we use the clips_gen function that will place every pictures in the moments we found using the beat_gen 
 
