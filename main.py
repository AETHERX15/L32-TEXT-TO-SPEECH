import speech_recognition as sr
import pyttsx3
from googletrans import Translator

languages={
    "1":"fr",
    "2":"es",
    "3":"de"

}

def main():
    print("Choose Language")
    print("1 french")
    print("2 spanish")
    print("3 Germany")
    target=languages.get(input("Choose:"))
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("Speak In English")
        audio=r.listen(source)
    try:
        text=r.recognize_google(audio,language="en-US")
        print("You Said:",text)
        translated=Translator().translate(text,dest=target).text
        print("Translation:",translated)

        engine=pyttsx3.init()
        engine.say(translated)
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Could Not Understand The Audio")

main()