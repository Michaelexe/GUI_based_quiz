import tkinter as tk
import tkinter.font as tkfont
from time import sleep

def delete():
	for widget in overlaybg.winfo_children():
		widget.destroy()

	for widget in mainbg.winfo_children():
		widget.destroy()


def right_answer():
	fontsize_right = tkfont.Font(size = 20)
	rightlabel = tk.Label(overlaybg, text = "YOU ARE CORRECT!!", fg = "Green", bg = "White",font = fontsize_right)
	rightlabel.place(relx = 0.3, rely = 0.8)

	nextbutton = tk.Button(mainbg, text = "Next", fg = "Black", bg = "White", command = delete)
	nextbutton.place(relwidth = 0.1, relx = 0.45, rely = 0.9)

def wrong_answer():
	fontsize_wrong = tkfont.Font(size = 20)
	rightlabel = tk.Label(overlaybg, text = "YOU ARE WRONG!!", fg = "Red", bg = "White",font = fontsize_wrong)
	rightlabel.place(relx = 0.3, rely = 0.8)

	nextbutton = tk.Button(mainbg, text = "Next", fg = "Black", bg = "White", command = delete)
	nextbutton.place(relwidth = 0.1, relx = 0.45, rely = 0.9)


def question1():

	fontsize = tkfont.Font(size = 20)
	q1 = tk.Label(overlaybg, text = "Which is the fourth planet in our solar system?", fg = "Black", bg = "White", font = fontsize)
	q1.place(relx = 0.03, rely = 0.1)


	option1 = tk.Button(overlaybg, text = "a) Earth", fg = "Black", bg = "Grey", command = wrong_answer)
	option2 = tk.Button(overlaybg, text = "b) Mars", fg = "Black", bg = "Grey", command = right_answer)
	option3 = tk.Button(overlaybg, text = "c) Jupiter", fg = "Black", bg = "Grey", command = wrong_answer)
	option4 = tk.Button(overlaybg, text = "d) Saturn", fg = "Black", bg = "Grey", command = wrong_answer)

	option1.place(relwidth = 0.2, relx = 0.4, rely = 0.3)
	option2.place(relwidth = 0.2, relx = 0.4, rely = 0.4)
	option3.place(relwidth = 0.2, relx = 0.4, rely = 0.5)
	option4.place(relwidth = 0.2, relx = 0.4, rely = 0.6)

def question2():
	fontsize = tkfont.Font(size = 20)
	q1 = tk.Label(overlaybg, text = "What is the hottest substance in the universe?", fg = "Black", bg = "White", font = fontsize)
	q1.place(relx = 0.03, rely = 0.1)


	option1 = tk.Button(overlaybg, text = "a) The Sun", fg = "Black", bg = "Grey", command = wrong_answer)
	option2 = tk.Button(overlaybg, text = "b) Alpha centauri", fg = "Black", bg = "Grey", command = wrong_answer)
	option3 = tk.Button(overlaybg, text = "c) Quasars", fg = "Black", bg = "Grey", command = right_answer)
	option4 = tk.Button(overlaybg, text = "d) Neutron star", fg = "Black", bg = "Grey", command = wrong_answer)

	option1.place(relwidth = 0.2, relx = 0.4, rely = 0.3)
	option2.place(relwidth = 0.2, relx = 0.4, rely = 0.4)
	option3.place(relwidth = 0.2, relx = 0.4, rely = 0.5)
	option4.place(relwidth = 0.2, relx = 0.4, rely = 0.6)


root = tk.Tk()

mainbg = tk.Canvas(root, height = 450, width = 800, bg = "Red")
mainbg.pack()

overlaybg = tk.Frame(root, bg = "White")
overlaybg.place(relheight = 0.8, relwidth = 0.8, relx = 0.1, rely = 0.1)

question1()

root.mainloop()