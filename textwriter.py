from os import write
import keyboard
from time import sleep as s
import random
def write():
    print("started")
    f = open("exam.txt", "r", encoding='utf-8')
    content = f.read()
    paragraphs = content.splitlines()
    for p, paragraph in enumerate(paragraphs):
        if p > 0:
            paragraphtime = random.uniform(1, 10)
            s(paragraphtime)
            print(paragraph)
            keyboard.press_and_release('enter')
        else:
            pass
        for x, sentence in enumerate(paragraph.split(".")):
            if x > 0:
                keyboard.write(".")
                sentencetime = random.uniform(2, 30)
                s(sentencetime)
                
            else:
                pass
            for w, word in enumerate(sentence.split(" ")):
                if w > 0:
                    wordtime = random.uniform(0.2, 0.05)
                    keyboard.write(" ")
                    s(wordtime)
                else: 
                    pass
                for l, letter in enumerate(word):
                    lettertime = random.uniform(0.15, 0.1)
                    keyboard.write(letter)
                    s(lettertime)
