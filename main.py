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
   'hi?',
    'Hi there, I am a chatbot app here to help you.',
    'What is your name?',
    'My name is ChatBot.',
    'Where do you live?',
    'I live in Pakistan.',
    'What can you help me with?',
    'I can help you with various topics based on my dataset.',
    'What do you think about?',
    'I always think about my dataset.',
    'Tell me about yourself.',
    'I have been developed to help you.',
    'Do you have any hobbies?',
    'As a chatbot, I don\'t have physical hobbies, but I enjoy helping people.',
    'What languages do you speak?',
    'I can communicate in multiple languages, including English.',
    'How can I contact you?',
    'You can reach me through this chat interface.',
    'Can you tell a joke?',
    'Sure, here\'s one: Why don\'t scientists trust atoms? Because they make up everything!',
    'What is the meaning of life?',
    'The meaning of life can vary for each person. It\'s a philosophical question.',
    'What is your favorite movie?',
    'Since I am an AI chatbot, I don\'t have personal preferences.',
    'Tell me a fun fact.',
    'Did you know that the first computer programmer was a woman named Ada Lovelace?',
    'How do you learn new things?',
    'I learn through the data and conversations I am exposed to, constantly improving my responses.',
    'Can you help me with programming?',
    'Yes, I can provide assistance and information on programming topics.',
    'What is your favorite book?',
    'As an AI chatbot, I don\'t have personal preferences for books.',
    'How long have you been a chatbot?',
    'I have been developed recently and I am constantly learning and improving.',
    'What is the weather like today?',
    'I\'m sorry, I don\'t have real-time information. You can check a weather website or app for the latest updates.',
    'Tell me a quote.',
    'Here\'s a quote: "The only way to do great work is to love what you do." - Steve Jobs',
    'What is the capital of France?',
    'The capital of France is Paris.',
    'What is your favorite food?',
    'As an AI, I don\'t have the ability to eat or taste, so I don\'t have a favorite food.',
    'Can you recommend a good movie?',
    'It depends on your preferences. What genre of movies do you enjoy?',
    'What is the largest country in the world?',
    'The largest country in the world by land area is Russia.',
    'What is the time right now?',
    'I don\'t have real-time information. You can check the time on your device or search for it online.',
    'Thank you for your help!',
    'You\'re welcome! I\'m here to assist you anytime.',
    'How can I improve my programming skills?',
    'Improving programming skills requires practice and learning. You can try building projects, solving coding challenges, and studying from reliable resources.',
    'What are the latest technological advancements?',
    'There are many exciting technological advancements happening, such as artificial intelligence, blockchain, virtual reality, and more. It\'s a rapidly evolving field.',
    'What are some popular programming languages?',
    'Some popular programming languages include Python, JavaScript, Java, C++, and Ruby.',
    'Tell me about the benefits of learning a new language.',
    'Learning a new language can expand your horizons, improve cognitive abilities, enhance communication skills, and open up new opportunities for personal and professional growth.',
    'Can you help me with a math problem?',
    'Yes, I can assist you with math problems. Please provide the details of the problem.',
    'What are some good resources for learning web development?',
    'There are many great resources for learning web development, including online tutorials, coding bootcamps, and documentation for popular web development frameworks like React and Angular.',
    'How can I stay motivated while learning?',
    'Staying motivated while learning can be challenging. Setting clear goals, breaking tasks into smaller steps, finding a supportive community, and celebrating achievements can help maintain motivation.',
    'What is the difference between machine learning and artificial intelligence?',
    'Artificial intelligence (AI) is a broad field that encompasses various technologies and methods that enable machines to simulate human intelligence. Machine learning is a subset of AI that focuses on algorithms and statistical models that allow machines to learn from and make predictions or decisions based on data.',
    'Tell me about the latest smartphones in the market.',
    'The smartphone market is constantly evolving, with new models being released by various manufacturers. It would be best to check technology news websites or consult with experts for the latest information on smartphones.',
    'How can I protect my online privacy?',
    'To protect your online privacy, you can use strong and unique passwords, enable two-factor authentication, be cautious while sharing personal information online, use secure and encrypted connections, and regularly update your software and devices.',
    'Can you recommend any online learning platforms?',
    'There are many reputable online learning platforms available, such as Coursera, Udemy, edX, and Khan Academy. The choice depends on your specific learning goals and preferences.',




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