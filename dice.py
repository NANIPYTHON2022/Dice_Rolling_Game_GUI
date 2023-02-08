import tkinter as tk
from PIL import Image, ImageTk
import random



window=tk.Tk()
window.geometry("500x360")
window.title("Dice Roll")
window.configure(bg="black")

dice=["C:\\Users\\konda\\Desktop\\dice-roll-py\\images\\dice1.png",
      "C:\\Users\\konda\\Desktop\\dice-roll-py\\images\\dice2.png",
      "C:\\Users\\konda\\Desktop\\dice-roll-py\\images\\dice3.png",
      "C:\\Users\\konda\\Desktop\\dice-roll-py\\images\\dice4.jpg",
      "C:\\Users\\konda\\Desktop\\dice-roll-py\\images\\dice5.png",
      "C:\\Users\\konda\\Desktop\\dice-roll-py\\images\\dice06.jpg"]

image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))


label1=tk.Label(window,image=image1)
label2=tk.Label(window,image=image2)

label1.image=image1
label2.image=image2


label1.place(x=400,y=100)
label2.place(x=800,y=100)


def dice_roll():
    image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image=image1

    image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image=image2

button = tk.Button(window,text="ROLL",bg="green",fg="white",font="times 20 bold",command=dice_roll)
button.place(x=670,y=500)
window.mainloop()