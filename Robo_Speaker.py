#import python libraries to use them in code;
#Make sure the libraries you want to use are installed in your Python environment. 
# If not, you can install them using pip, Python's package installer. For example:
# used this command in terminal - pip install <library name>.
# Eg. --> pip install win32.com

import win32com.client as wincom
import time
import os

speak = wincom.Dispatch("SAPI.SpVoice")

text = "Welcome this is Robo Anirudh"
speak.Speak(text)


while True:
    x=input("Enter Text to Speak & q to exit : ")
    if x == "q":
        speak.Speak ("goodbye have a nice day")
        break
    speak.Speak(x)
    