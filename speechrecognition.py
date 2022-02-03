import speech_recognition as sr


class SpeechRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.recording = False

    def set_speech(self, recording):
        self.recording = recording

    def recognize_speech_from_mic(self, recognizer, microphone):
        print("silence please!")
        with microphone as source:  # adjust the recognizer sensitivity to ambient noise and record audio
            recognizer.adjust_for_ambient_noise(source)
            print("you can talk now!")
            audio = recognizer.listen(source)  # from the microphone

        response = None
        try:
            response = recognizer.recognize_google(audio)  # use google API
        except sr.RequestError:
            print("requesterrror")
            pass
        except sr.UnknownValueError:
            print("unknownvalue")
            pass
        return response

    def speech(self):  # record the audio for input
        if self.recording is True:
            voice = str(self.recognize_speech_from_mic(self.recognizer, self.microphone))
            print(voice)
            self.recording = False
            return voice



