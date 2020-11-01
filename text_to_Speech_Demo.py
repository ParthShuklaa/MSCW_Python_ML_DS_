"""
WAP to Convert Written text into Speech

Step1:Import Fucntionality (GTTS) - Google text to Speech Fucntionality
Step2:Call Constructor
Step3:Output
"""
import gtts
import os
MyText = "Welcome to this online session on Python- I hope You are learning something new. Dont forget to have Fun while coding "

MyValue = gtts.gTTS(text = MyText,lang= 'en', slow = True)

MyValue.save("MySpeech1.mp3")
os.system("MySpeech1.mp3")



