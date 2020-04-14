import tkinter as tk
from tkinter import *
import requests
from tkinter.scrolledtext import ScrolledText

def clear():
	viewBox.configure(state=NORMAL)
	viewBox.delete(1.0, END)
	viewBox.configure(state=DISABLED)

def check():
	address = "https://api.openweathermap.org/data/2.5/weather?appid=a5da043b07499da9b964e606695c64e2&q="
	location = loc_ent.get()
	if location == "":
		print("app")
	else:
		url = address+location
		req = requests.get(url).json()
		weather = req["weather"][0]["main"]
		description = req["weather"][0]["description"]
		
		print(weather)
		viewBox.configure(state=NORMAL)
		viewBox.insert(END, f"Location: {location}\n\n")
		viewBox.insert(END, f"Temperature: {weather}\n\n")
		viewBox.insert(END, f"Description: {description.title()}\n\n")
		viewBox.configure(state=DISABLED)

		loc_ent.delete(0, END)


root = tk.Tk()
root.title("Weather App")
root.geometry("425x350")
root.configure(bg="grey")
root.resizable(width=False, height=False)

global loc_ent
global viewBox

f = Frame(bg="grey")
f.grid(row=1, column=0, pady=20)

f1 = Frame(bg="grey")
f1.grid(row=2, column=0, padx=20)

loc_intro = tk.Label(f, text="Location", font=("Lucida Sans", 15, "bold"), bg="grey")
loc_intro.grid(row=0, column=0)

loc_ent = tk.Entry(f, width=20, font=("Lucida Sans", 15))
loc_ent.grid(row=0, column=1, padx=10)

check_btn = tk.Button(f, text="Check", font=("Lucida Sans", 11, "bold"), bg="grey", width=10, command=check)
check_btn.grid(row=1, column=1, pady=4)

viewBox = ScrolledText(f1, width=int(36.5), height=10, font=("Lucida Sans Typewriter", 12), state=DISABLED, bg="grey")
viewBox.grid(row=0, column=0, columnspan=1)

clearBtn = tk.Button(f1, text="Clear", font=("Lucida Sans", 11, "bold"), bg="grey", width=10, command=clear)
clearBtn.grid(row=3, column=0, pady=4)

mainloop()
