import os
import speech_recognition as sr
r = sr.Recognizer()
os.system("color a")
try:

    mic = sr.Microphone()
    os.system("cls")
    language = input("What language do you want to continue with?(en-EN/tr-TR): ")
    if language == "en-EN":
        print('Listening...')
        with mic as source:
            audio = r.listen(source)
        print('Listen!')
        print("User's expression:",r.recognize_google(audio,language= "en-EN"))
    if language == "tr-TR":
        print('Dinliyor')
        with mic as source:
            audio = r.listen(source)
        print('Dinledi')
        print("Kullanıcının İfadesi:",r.recognize_google(audio,language= "tr-TR"))



except:
    print("Üzgünüm Bir Hata Oluştu Veya Ses Algılanamadı.")

