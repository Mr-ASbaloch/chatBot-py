from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading 
engine =pp.init()

voices = engine.getProperty("voices")
print ("voices")
engine.setProperty("voice", voices[1].id)

def speak(word):
 engine.say(word)
 engine.runAndWait()

bot = ChatBot("My Bot")

convo = (
    'hi ?',
    'hi there,im chatbot app for your help',
    'what is your name ?',
    'my name is chatBot',
    'where you live ?',
    'i live in pakistan '
    'what you can help me?',
    'i can help you according to my dataset ',
    'what you think ?',
    'i always think about my dataset',
    'tell me your self ?',
    'i have develop to help you'



)
trainer = ListTrainer(bot)
trainer.train(convo)
# answer = bot.get_response("where you live")
# print(answer)

# print("talk to chatbot")
# while True:
#     query = input()
#     if query == 'exist' :
#         break
#     answer = bot.get_response(query)
#     print("bot : " , answer)

# main = Tk ()
# main.geometry("500x500")
# main.title("MY Chat Bot")
# img = PhotoImage(file="download (11).png")
# photoL = Label(main, image=img)
# photoL.pack(pady=10)
#
# main.mainloop()

main = Tk()
main.geometry("500x600")
main.title("MY Chat Bot")

# Load the image
img = PhotoImage(file="download__11_-removebg-preview.png")

# Calculate the desired width
desired_width = 600

# Calculate the resize factor
resize_factor = desired_width / img.width()

# Resize the image using the subsample() method
img = img.subsample(int(resize_factor))

photoL = Label(main, image=img)
photoL.pack(pady=10)

# function for voce query 
def takeQuery():
 sr=s.Recognizer()
 sr.pause_threshold = 1
 with s.Microphone( ) as m:
   try:
     audio=sr.listen(m)
     query =sr.recognize_google(audio,language='eng-in')
     print(query)
     textF.delete(0,END)
     textF.insert(0,query)
     ask_from_bot()
   except Exception as e:
    print(e)
    print("not recognized ")
     
   
 

# function call
def ask_from_bot() :
   query = textF.get()
   answer = bot.get_response(query)
   msgs.insert(END, "You: " + query)
   msgs.insert(END, "Bot :" + str(answer))
   speak(answer)
   textF.delete(0,END)
   msgs.yview(END)

frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame,width=80,height=20,yscrollcommand=Scrollbar.set)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()

# text file

textF = Entry(main, font=("poppins", 13))
textF.pack(fill=X ,pady=20,padx=20)


# btn = Button(main, text="what`s your query ", font=("Verdana", 10)) 
# btn.pack()

btn = Button(main, text="What's your query", font=("bold italic", 12),command=ask_from_bot)
btn.configure(bg="blue", fg="white" )
btn.pack()

# enter key funcrion  
def enter_query(event):
   btn.invoke()
main.bind('<Return>',enter_query)

def repeatL():
  while True:
    takeQuery()

t=threading.Thread(target=takeQuery)
t.start()
main.mainloop()