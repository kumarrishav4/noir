import pyttsx3
import speech_recognition as sr

class AI():
    __name =""
    __skill=[]
    
    def __init__ (self,name=None):
        self.engine =pyttsx3.init()
        self.r=sr.Recognizer()
        self.m=sr.Microphone()
        
        if name is not None:
            self.__name =name
        
        print("listeing")
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)
            
    @property
    def name(self):
        return self.__skill
    @name.setter
    def name(self,value):
        sentence ="hello my name is"+self.__name
        self.__skill = value
        self.engine.say(sentence)
        self.engine.runAndWait()
        
    def say(self,sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()
        
    def listen(self):
        print("say something")
        with self.m as source:
            audio =self.r.listen(source)
        print("got it")
        try:
            phase =self.r.recognize_google(audio,show_all=False,language="en-US")
            sentence ="Got it, you said "+ phase
            self.engine.say(sentence)
            self.engine.runAndWait()
        except:
            print("sorry there is a error ")
            self.engine.say("sorry there is a error")
            self.engine.runAndWait()
        print("you said", phase)
        return phase