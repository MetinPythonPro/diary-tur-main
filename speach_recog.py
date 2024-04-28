from email.mime import audio
import speech_recognition as sr

def speech_tr():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
    return r.recognize_google(audio, language="tr-TR")

def speech_eng():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
    return r.recognize_google(audio)

#print(speech_tr())