import speech_recognition as sr
from google_trans_new import google_translator
from gtts import gTTS
from playsound import playsound

r = sr.Recognizer()
translator = google_translator

with sr.Microphone() as source:
    print("Speak now")
    audio = r.listen(source)
    try:
        speech_text = r.recognize_google(audio)
        print(speech_text)
    except sr.UnknownValueError:
        print("could not understand")
    except sr.RequestError:
        print("Could not request from google")

    translated_text = translator.translate(speech_text, lang_tgt = 'ta')
    print(translated_text)

    voice = gTTS(translated_text, lang='ta')
    voice.save("voice.mp3")