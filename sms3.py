#Imports, (pip install keyboard, plyer)
#-----------------------------------------------------------
import keyboard
from plyer import notification
#Random variables
#-----------------------------------------------------------
index, message, typemode = 0, [], False
#Message Notification Function
#-----------------------------------------------------------
def Message(message, title):
    notification.notify(title= (title),
                        message= message,
                        app_name="Pornhub",
                        app_icon = None,
                        timeout= 0)
#Keypress reader
#-----------------------------------------------------------
def filter(char):
    global index, message
    ignorables = ["space", "ctrl", "skift"]
    if char == "space":
        index +=1
        return " "
    elif char in ignorables:
        return ""
    elif char == "backspace":
        message.pop(index+1)
        index-=1
        return ""
    elif char == "enter":
        message.pop(0)
        Message("".join(message), "SMS")
        message = []
        index = 0
        return ""
    elif len(char) > 1:
        index +=1
        return "[%s]" % char
    else:
        index +=1
        return char

def logger(event):
    if typemode:
        anus = (filter(event.name))
        message.append(anus)
#Notify when typing is available
#-----------------------------------------------------------
def typemoder():
    global typemode, index
    typemode = not typemode
    Message(f"Typemode {typemode}", "Settings")

#Starta typemode med ctrl+shift+/ och avsluta programmet med ctrl+shift+esc
#-----------------------------------------------------------
keyboard.on_press(logger)
keyboard.add_hotkey('ctrl+shift+/', typemoder)
keyboard.wait('ctrl+alt+delete')

#taskkill /IM pythonw.exe /F to force it shut
