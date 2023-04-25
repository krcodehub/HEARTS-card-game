import tkinter
from tkinter import *


root = Tk()
root.title('Hearts Template')
root.geometry("900x500")
root.configure(background = "green")



my_frame = Frame(root, bg="green")
my_frame.pack(pady = 20)

#create frames for cards
dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.grid(row=0, column=1, padx=20, ipadx=20)

#Future players 
#dealer_frame = LabelFrame(my_frame, text="Player", bd=0)
#dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

#dealer_frame = LabelFrame(my_frame, text="Player", bd=0)
#dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

#shuffle cards
def shuffle():
    suits = ["diamonds", "spades", "hearts", "clubs"]
    values = range(2, 15)
    # 11 = jack, 12 = queen, 13 = king, 14 = ace

    global deck
    deck=[]
    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')

    print(deck)
#Put cards in frames
dealer_label = Label(dealer_frame, text='')
dealer_label.pack(pady=20)

player_label= Label(player_frame, text='')
player_label.pack(pady=20)


#button creation
shuffle_button = Button(root, text='Shuffle Deck', font=())

root.mainloop()


