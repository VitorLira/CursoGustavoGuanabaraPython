# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.

from pygame import mixer
mixer.init()
mixer.music.load('whitcher.mp3')
mixer.music.play()
input('digite algo para parar')
