import time, sys
import pyttsx
import speech_recognition as sr
import aiml
import os
import warnings

mode = "text"
if len(sys.argv) >1:
	if sys.argv[1]=="--voice" or sys.argv[1]=="voice":
		mode = "voice"

terminate = ['bye','byeava','goodbye','goodbyeava','gotosleep','gotosleepava','byebye']

def offline_speak(ava_speech):
	engine = pyttsx.init()
	engine.say(ava_speech)
	engine.runAndWait()

def hear():
	rss = sr.Recognizer()
	with sr.Microphone() as source:
	    print("Speak to AVA:- ")
	    audio = rss.listen(source)
	try:
	    print rss.recognize_google(audio)
	    return rss.recognize_google(audio)
	except sr.RequestError as e1:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e1))
	except sr.UnknownValueError:
	    offline_speak("I could not understand what you said! Would you mind repeating?")
	    return(hear())


kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std_loader.xml", commands = "LOAD AIML B")

os.system("clear")
# kernel now ready for use
while True:
	if mode == "voice":
		#os.system("clear")
		response = hear()
	else:
		#os.system("clear")
		response = raw_input("Write to AVA:- ")
	if response.lower().replace(" ","") in terminate:
		break
	ava_speech = kernel.respond(response)
	print "AVA:- " + ava_speech
	offline_speak(ava_speech)
	
