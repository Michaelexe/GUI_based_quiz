import tkinter as tk
import tkinter.font as tkfont
from time import sleep



result = 0
nextclick = 0


















#necessary functions

def delete():
	global nextclick
	for widget in overlaybg.winfo_children():
		widget.destroy()

	for widget in mainbg.winfo_children():
		widget.destroy()

	nextclick += 1

	if nextclick == 0:
		question1()

	if nextclick == 1:
		question2()

	if nextclick == 2:
		question3()

	if nextclick == 3:
		question4()

	if nextclick == 4:
		question5()

	if nextclick == 5:
		endscreen()

def right_answer():
	global result

	result += 1

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

def close():
	root.destroy()

def restart():
	global nextclick 
	global result

	result = 0
	nextclick = -1

	delete()
















#Question1
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


#Question2

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

#Question3

def question3():
	fontsize = tkfont.Font(size = 20)
	q1 = tk.Label(overlaybg, text = "What comes between Mars and Jupiter?", fg = "Black", bg = "White", font = fontsize)
	q1.place(relx = 0.1, rely = 0.1)


	option1 = tk.Button(overlaybg, text = "a) The Astroid Belt", fg = "Black", bg = "Grey", command = right_answer)
	option2 = tk.Button(overlaybg, text = "b) Saturn", fg = "Black", bg = "Grey", command = wrong_answer)
	option3 = tk.Button(overlaybg, text = "c) Nothing", fg = "Black", bg = "Grey", command = wrong_answer)
	option4 = tk.Button(overlaybg, text = "d) Earth", fg = "Black", bg = "Grey", command = wrong_answer)

	option1.place(relwidth = 0.2, relx = 0.4, rely = 0.3)
	option2.place(relwidth = 0.2, relx = 0.4, rely = 0.4)
	option3.place(relwidth = 0.2, relx = 0.4, rely = 0.5)
	option4.place(relwidth = 0.2, relx = 0.4, rely = 0.6)

#Question4

def question4():
	fontsize = tkfont.Font(size = 20)
	q1 = tk.Label(overlaybg, text = "which blackhole is at the center of our galaxy?", fg = "Black", bg = "White", font = fontsize)
	q1.place(relx = 0.03, rely = 0.1)


	option1 = tk.Button(overlaybg, text = "a) Sagitarius A-star", fg = "Black", bg = "Grey", command = right_answer)
	option2 = tk.Button(overlaybg, text = "b) Alpha centauri", fg = "Black", bg = "Grey", command = wrong_answer)
	option3 = tk.Button(overlaybg, text = "c) Milky Way", fg = "Black", bg = "Grey", command = wrong_answer)
	option4 = tk.Button(overlaybg, text = "d) Adromeda", fg = "Black", bg = "Grey", command = wrong_answer)

	option1.place(relwidth = 0.2, relx = 0.4, rely = 0.3)
	option2.place(relwidth = 0.2, relx = 0.4, rely = 0.4)
	option3.place(relwidth = 0.2, relx = 0.4, rely = 0.5)
	option4.place(relwidth = 0.2, relx = 0.4, rely = 0.6)

#Question5

def question5():
	fontsize = tkfont.Font(size = 20)
	q1 = tk.Label(overlaybg, text = "Which galaxy is likely to collide with our galaxy \n in the future?", fg = "Black", bg = "White", font = fontsize)
	q1.place(relx = 0.01, rely = 0.1)


	option1 = tk.Button(overlaybg, text = "a) Milky Way", fg = "Black", bg = "Grey", command = wrong_answer)
	option2 = tk.Button(overlaybg, text = "b) Kepler 250", fg = "Black", bg = "Grey", command = wrong_answer)
	option3 = tk.Button(overlaybg, text = "c) Sagitarius", fg = "Black", bg = "Grey", command = wrong_answer)
	option4 = tk.Button(overlaybg, text = "d) Adromeda", fg = "Black", bg = "Grey", command = right_answer)

	option1.place(relwidth = 0.2, relx = 0.4, rely = 0.3)
	option2.place(relwidth = 0.2, relx = 0.4, rely = 0.4)
	option3.place(relwidth = 0.2, relx = 0.4, rely = 0.5)
	option4.place(relwidth = 0.2, relx = 0.4, rely = 0.6)

def endscreen():
	global result
	result = str(result)

	fontsize1 = tkfont.Font(size = 30)
	congratulation = tk.Label(overlaybg, text = "CONGRATULATIONS!!!", fg = "Green", bg = "White", font = fontsize1)
	congratulation.place(relx = 0.15, rely = 0.1)

	fontsize2 = tkfont.Font(size = 20)
	end = tk.Label(overlaybg, text = "You have completed the quiz", fg = "Red", bg = "White", font = fontsize2)
	end.place(relx = 0.2, rely = 0.4)

	fontsize3 = tkfont.Font(size = 15)
	result = tk.Label(overlaybg, text = "You answered " + result + " out of 5 questions right", fg = "Green", bg = "White", font = fontsize3)
	result.place(relx = 0.2, rely = 0.6)

	exitbutton = tk.Button(mainbg, text = "Click to Close", fg = "White", bg = "Red", command = close)
	exitbutton.place(relwidth = 0.15, relx = 0.35, rely = 0.9)

	restartbutton = tk.Button(mainbg, text = "Retry quiz", fg = "Black", bg = "Green", command = restart)
	restartbutton.place(relwidth = 0.15, relx =0.5, rely = 0.9)






















root = tk.Tk()

root.title("GUI Quiz")

mainbg = tk.Canvas(root, height = 450, width = 800, bg = "Blue")
mainbg.pack()

overlaybg = tk.Frame(root, bg = "White")
overlaybg.place(relheight = 0.8, relwidth = 0.8, relx = 0.1, rely = 0.1)


question1()

root.mainloop()
