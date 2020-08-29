import gtts
from playsound import playsound

tts = gtts.gTTS("Hello World my name is Gaurav Srivastava I live in Noida ,basically I am from Raebareli uttar pradesh")

tts.save(("hello.mp3"))

playsound("hello.mp3")



