"""
program: musicplayer.py
author: mike 4/13/2021
simple program to play an audio file
"""
from pygame import mixer

#store the file name in a variable for easy reference
file = "getlove.mp3"

#initialize the mixer
mixer.init()

#load the music file into the mixer
mixer.music.load(file)

#play the loaded music file 
mixer.music.play()

#this statment will provide a delay in exiting the program without it, mixer.music.play() wouldnt be able to play before the app closed
input("playing song... press enter to quit")