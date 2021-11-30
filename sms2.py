import keyboard
from plyer import notification

index = 0
message = []
typemode = False
def Message(message, title):
    notification.notify(title= (title),
                        message= message,
                        app_name="Pornhub",
                        app_icon = None,
                        timeout= 0)
def filter(char):
    global index
    global message

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
        pass
    else:
        pass
    

def yes():
    print("".join(message))


keyboard.on_press(logger)

def typemoder():
    global typemode, index
    typemode = not typemode
    Message(f"Typemode {typemode}", "Settings")

keyboard.add_hotkey('ctrl+shift+/', typemoder)
keyboard.wait()

#taskkill /IM pythonw.exe /F
