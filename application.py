#dependencies

from tkinter import *
from tkinter.filedialog import askopenfile
import googletrans
from googletrans import Translator
from langdetect import detect
from PIL import Image
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr():
    global img_to_text
    #print(file_path)
    ocr_img = Image.open(file_path.name)
    text = pytesseract.image_to_string(ocr_img, lang='eng')
    #print(text)
    img_to_text.set(text)

def upload():
    global file_path
    file_path = askopenfile(initialdir='/',title='Select a file',filetype=(('jpeg','*jpg'),('All Files','*.*')))
    #print(file_path.name)
    #print(type(file_path))
    ocr()

def swap():
    global from_var,to_var
    #print(from_var.get())
    #print(to_var.get())
    lang1 = from_var.get()
    lang2 = to_var.get()
    #print(lang1)
    #print(lang2)
    lang1,lang2 = lang2,lang1
    #print(lang1)
    #print(lang2)
    from_var.set(lang1)
    to_var.set(lang2)

def detect_lang():
    #text = detect_entry.get() // the section has been jammed for the time being as it has an unsolved bug in it.
    text = 'Hello World'
    print(text)
    #detect_lang_code = detect(text)  #detects language and shows its lang code
    #print(detect_lang_code)
    #new_dict = {value: key for key, value in googletrans.LANGCODES.items()} #have swapped keys to values
    #code_to_lang = new_dict[detect_lang_code]  #now storing the name of the language from the lang code
    code_to_lang = 'English'
    detected_lang = Label(root,text='< '+code_to_lang+' >',bg='white',fg='blue',font=('bold',10))
    detected_lang.place(x=320,y=96)

def translate():
    global translated

    translator = Translator()
    entry1 = entry_from.get()
    result = translator.translate(entry1,src=from_var.get(),dest=to_var.get())
    translated.set(result.text)


g_languages = list(googletrans.LANGUAGES.values())
languages = []
for i in g_languages:
    i = i.title()
    languages.append(i)
#print(languages)

root = Tk()
root.geometry('600x500')
root.title('Multi Lingual')
root.configure(background='white')
root.resizable(0,0)

translated = StringVar()
img_to_text = StringVar()

#logo of Google translate
img = Image.open('logo.png')
img = img.resize((45,45),Image.ANTIALIAS)
img = img.save('image.ppm','ppm')
img = PhotoImage(file='image.ppm')

#swap pic
img2 = Image.open('swap.png')
img2 = img2.resize((30,30))
img2 = img2.save('image2.ppm','ppm')
img2 = PhotoImage(file='image2.ppm')

#camera pic
img3 = Image.open('camera.png')
img3 = img3.resize((30,30))
img3 = img3.save('image3.png','png')
img3 = PhotoImage(file='image3.png')

title = Label(root,text='MULTI LINGUAL',fg='black',bg='white',font=('bold',15))
title.place(x=220,y=30)

logo = Label(root,image=img,bg='white')
logo.place(x=175,y=23)

#detecting language
v = StringVar()
lang_detect = Label(root,text='Detect Language :',bg='white',fg='black')
lang_detect.place(x=20,y=100)
detect_entry = Entry(root,bg='DodgerBlue2',fg='white')
detect_entry.place(x=130,y=100)
detect = Button(root,text='Detect',command=detect_lang,activebackground='orange')
detect.place(x=265,y=95)

From = Label(root,text='From',bg='white',fg='blue',font=('bold',10))
From.place(x=150,y=150)

cam = Button(root,image=img3,bg='white')
cam.place(x=30,y=215)

upload = Button(root,text='Upload',bg='white',fg='black',activebackground='orange',command=upload)
upload.place(x=24,y=275)

choose_from = Label(root,text='Choose Language',bg='white',fg='blue')
choose_from.place(x=110,y=200)

from_var = StringVar(root)
index = languages.index('English') #finding the index of English lang
from_var.set(languages[index]) #sets English as the default Language
from_lang = OptionMenu(root,from_var,*languages)
from_lang.place(x=120,y=230)

entry_from = Entry(root,text=img_to_text,bg='DodgerBlue2',fg='white')
entry_from.place(x=120,y=280)

swap = Button(root,image=img2,bg='white',command=swap)
swap.place(x=270,y=145)

To = Label(root,text='To',bg='white',fg='blue',font=('bold',10))
To.place(x=390,y=150)

choose_to = Label(root,text='Choose Language',bg='white',fg='blue')
choose_to.place(x=360,y=200)

to_var = StringVar(root)
to_var.set('French')
to_lang = OptionMenu(root,to_var,*languages)
to_lang.place(x=370,y=230)

entry_to = Entry(root,text=translated,bg='DodgerBlue2',fg='white')
entry_to.place(x=370,y=280)

translate = Button(root,text='Translate',bg='white',fg='black',font=('bold',10),activebackground='orange',command=translate)
translate.place(x=260,y=350)

credits = Label(root,bg='black',fg='white',text='©Developed by Bhavishya Pandit',height=3,width=90)
credits.place(x=0,y=450)

root.mainloop()

