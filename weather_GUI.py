import tkinter
from tkinter import *
from tkinter import messagebox
import subprocess
import psutil

BLUE = "#CFDEE4"
GREEN = "#BAC9B0"

window = Tk()
window.title("RES Inspections Rain Data")
window.config(padx=50, pady=50, bg=BLUE)
window_width = 300
window_height = 200
# window.grid_columnconfigure(0, minsize=100)
# window.grid_columnconfigure(1, minsize=300)
# window.grid_columnconfigure(2, minsize=100)

# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

def run_script():
    start_button.config(text="Processing...")
    messagebox.showinfo("Message", "Gathering weather data, this may take a few minutes.")
    program = r"R:\Resgis\entgis\Resources\Scripts\Inspections_Rain_Data_Script\web_scraper_WU.py"
    subprocess.call(['python', program])
    running = True
    while running:
        if "web_scraper_WU.py" in (p.name() for p in psutil.process_iter()):
            start_button.config(text="Gathering weather data...")
        else:
            start_button.config(text="Done!")
            start_button.config(state=DISABLED)
            running = False

start_button = Button(text="Run Program", bg = GREEN, font=("Verdana", 24, "bold"), command=run_script)
start_button.place(relx=0.5, rely=0.5, anchor=CENTER)
# start_button.grid(row=1, column=0)

window.mainloop()