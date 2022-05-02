#sources:
#https://www.tutorialspoint.com/python/tk_pack.htm
#https://www.pythontutorial.net/tkinter/tkinter-pack/
#https://www.tutorialspoint.com/how-to-disable-enable-a-button-in-tkinter

from tkinter import *
from PIL import ImageTk
import random

root = Tk()
root.title("Shuffle Game")
root.geometry('700x500') #it give us width and size
root.resizable(0, 0) #can't resize the root

# pack() method is organizes widgets in blocks vertically
# title.pack and intro.pack are to place 2 labels into the root
# pady is to set the distance between the control boundary and the container vertical spacing
# title label has a 20pixel vertical space between the control boundary and the container
title = Label(root, text="Find the otter")
title.pack(pady=20)
intro = Label(root,text="Click the number to find the otter")
intro.pack(pady=10)

# new frame for pack() to have new row
# since I want the cards and buttons layout horizontally, they have to have their own frame
# cardFrame is the frame for cards and buttonFrame is the frame for button
# Frame(root) means means the new frame will be inside the root
cardFrame = Frame(root)
cardFrame.pack()
buttonFrame = Frame(root)
buttonFrame.pack()

#input image
blankCard = ImageTk.PhotoImage(file="blank.png")
otterCard = ImageTk.PhotoImage(file="csumbtransparent.png")

# correct and wrong are the variables for counting how many times the player won and lost the game
correct = 0
wrong = 0

#card List
# it contains 2 empty cards and the otter card
cardList = [blankCard, blankCard, otterCard]

#display the blank image in the cardFrame and use pack side to determind which side of the parent widget packs against
#Label(cardFramed) is set the cards into the cardFrame
# side= left is the set the label arranged vertically from the left
card1 = Label(cardFrame, image=blankCard)
card1.pack(side="left")
card2 = Label(cardFrame, image=blankCard)
card2.pack(side="left")
card3 = Label(cardFrame, image=blankCard)
card3.pack(side="left")

#use random function to shuffle the card list
#configure(image=) is to change the card image with the new cardList order
def shuffleCards():
    random.shuffle(cardList)
    card1.configure(image=cardList[0])
    card1.image = cardList[0]
    card2.configure(image=cardList[1])
    card2.image = cardList[1]
    card3.configure(image=cardList[2])
    card3.image = cardList[2]

#disable all the buttons after click
def disabledButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)

#active all the  buttons
def activeButton():
    button1.configure(state=NORMAL)
    button2.configure(state=NORMAL)
    button3.configure(state=NORMAL)

#b1/b2/b3 are all the same function represeted the three button
#b1 is for button1 and card1; b2 is for button2 and card2; b3 is for button3 and card3
#when button1 is clicked, it active b1();shuffleCards();disabledButton()
#if card1 is the otter card, number of correct will +1 & show congrat message
#if not, number of wrong will +1 & show lost message
#then the result label will update the message
def b1():
    shuffleCards()
    disabledButton()
    global correct
    global wrong
    if cardList[0] == otterCard:
        message.configure(text="You found the otter")
        correct +=1
    else:
        message.configure(text="Sorry, otter is not here")
        wrong += 1
    result.configure(text="Found: " + str(correct) + " Lost: " + str(wrong))

def b2():
    shuffleCards()
    disabledButton()
    global correct
    global wrong
    if cardList[1] == otterCard:
        message.configure(text="You found the otter")
        correct += 1
    else:
        message.configure(text="Sorry, otter is not here")
        wrong += 1
    result.configure(text="Found: " + str(correct) + " Lost: " + str(wrong))

def b3():
    shuffleCards()
    disabledButton()
    global correct
    global wrong

    if cardList[2] == otterCard:
        message.configure(text="You found the otter")
        correct +=1
    else:
        message.configure(text="Sorry, otter is not here")
        wrong +=1
    result.configure(text="Found: " + str(correct) + " Lost: " + str(wrong))

#let player keeps playing the game
#all the cards set to blank card
#remove the text in the message label
#active all the button and let player to play it again
def again():
    card1.configure(image=blankCard)
    card1.image = blankCard
    card2.configure(image=blankCard)
    card2.image = blankCard
    card3.configure(image=blankCard)
    card3.image = blankCard
    message.configure(text="")
    activeButton()

#back to defult setting
#set the result =0 (correct/wrong) and remove the result text
def reset():
    again()
    global correct
    global wrong
    correct = 0
    wrong = 0
    result.configure(text="")

#Button for select answer
#button1 is for card1; button2 is for card2; button3 is for card3
#command=b1 when the button is clicked, b1() will be active
#pack(ipadx) is to set the button position on the frame horizontal
#pack(padx) is to set the button distance horizontal space
button1 = Button(buttonFrame, text="1", command=b1)
button1.pack(side="left", ipadx=20, padx=90)
button2 = Button(buttonFrame, text="2",  command=b2)
button2.pack(side="left", ipadx=20, padx=40)
button3 = Button(buttonFrame,text="3", command=b3)
button3.pack(side="left", ipadx=20, padx=90 )

#new label show on the root
message = Label(root)
message.pack()
result = Label(root)
result.pack()

#againButton is to play the game again
#resetButton is to reset the game
againButton = Button(root, text="Again", command=again)
againButton.pack()
restButton = Button(root, text="Reset", command=reset)
restButton.pack()

root.mainloop()

# I wrote all the code by myself, I wrote the same game in javascript before
# I researched on how to used pack() method for the layout and disable the button



