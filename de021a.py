#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
from pygame import mixer
mixer.init()
mixer.music.load('years.mp3')
mixer.music.play()
x=input('Digite algo para parar ')
#Você precisa colocar o arquivo.mp3 na pasta D:\10_Labs\Dev\Python\PyCharm\CursoemVideo

