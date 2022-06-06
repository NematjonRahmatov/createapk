import pyttsx3
  
# initialisation
engine = pyttsx3.init()
  
# testing
n = input()
engine.say(f" {n} ")
engine.runAndWait()