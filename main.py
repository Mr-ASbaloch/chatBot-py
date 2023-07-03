from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

bot = ChatBot("My Bot")

# convo = [
#     'hi ?',
#     'hi there',
#     'what is your name ?',
#     'my name is abdul saeed',
#     'how are you ',
#     'where you live ?',
#     'i live in pakistan'
#
# ]
# trainer = ListTrainer(bot)
# trainer.train(convo)
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
main.geometry("500x500")
main.title("MY Chat Bot")

# Load the image
img = PhotoImage(file="download (11).png")

# Calculate the desired width
desired_width = 600

# Calculate the resize factor
resize_factor = desired_width / img.width()

# Resize the image using the subsample() method
img = img.subsample(int(resize_factor))

photoL = Label(main, image=img)
photoL.pack(pady=10)

main.mainloop()