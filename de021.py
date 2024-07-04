#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
import mp3play
filename = r'D:\years.mp3'
clip=mp3play.load(filename)
clip.play()

import time
time.sleep(min(30,clip.seconds()))
clip.stop()