import pyjokes
from ai import AI

jack=AI()

def joke():
    funny=pyjokes.get_joke()
    print(funny)
    jack.say(funny)
    
command =""
while True and command != "goodbye":
    command=jack.listen()
    print("command was:",command)
    if command == "tell me a joke ":
        joke()
        
jack.say("Goodbye")