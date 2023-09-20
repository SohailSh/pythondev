import tkinter
from tkinter import Tk
from tkinter import Label
from tkinter import Text
from tkinter import Button
from tkinter import Entry

#displaying the main window
root = Tk()
root.geometry("400x300")
root.title("Band Name Generator")
root.resizable(0, 0)
root.config(bg = "black")

#creating the labels and entry boxes for the user to input their horoscope and city
label1 = Label(root, text = "What is your horoscope?", font = ("Comic Sans", 20))
label1.pack()
entry1 = tkinter.StringVar()
entry1 = tkinter.Entry(root, textvariable = entry1, font = ("Comic Sans", 20))
entry1.pack()

label2 = Label(root, text = "What is the name of your city?", font = ("Comic Sans", 20))
label2.pack()
entry2 = tkinter.StringVar()
entry2 = tkinter.Entry(root, textvariable = entry2, font = ("Comic Sans", 20))
entry2.pack()


# Function to generate the band name
def generate_band_name():
    horoscope = entry1.get()
    city = entry2.get()
    band_name = f"{horoscope} {city}"
    output = tkinter.Label(text=f"Your Band Name Is: {band_name}", font = ("Comic Sans", 20))
    output.pack()
 
#setting up the generate button and call the generate_band_name() function
set_up_button = tkinter.Button(root, height=1, width=6, text="Generate", command=generate_band_name, fg = 'blue', font = ("Comic Sans", 20))
set_up_button.pack()

#reset function and deleting the entry boxes and output labels
def reset():
    entry1.delete(0, tkinter.END)
    entry2.delete(0, tkinter.END)

#rest button calling the reset function
reset_button = tkinter.Button(root, height=1, width=6, text="Reset", command=reset, fg = 'blue', font = ("Comic Sans", 20))
reset_button.pack()


#outputting the main window
root.mainloop() 