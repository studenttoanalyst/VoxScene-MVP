import speech_recognition as sr


class SpeechRecognizer:


    def __init__(self):

        self.recognizer = sr.Recognizer()



    def listen(self):

        with sr.Microphone() as source:

            print("Listening...")

            self.recognizer.adjust_for_ambient_noise(source)


            audio = self.recognizer.listen(source)



        try:

            command = self.recognizer.recognize_google(audio)

            print("You said:", command)

            return command.lower()


        except:

            print("Could not understand")

            return None
        