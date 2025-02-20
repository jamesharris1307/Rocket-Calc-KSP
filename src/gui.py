""" GUI components, Collects User Input, Displays Results"""

""" Imports """
from tkinter import *
from constants import midResolution

""" Window Settings """
window = Tk() # Instantiate an instance of window
window.geometry(midResolution) # Resolution of window
window.title("Rocket Calc KSP") # Title of window
window.config(background="white") # Change background colour
icon = PhotoImage(file='../assets/Spider.png') # Set custom icon
window.iconphoto(True, icon) # Replace default icon with custom icon

""" Title Label """
label = Label(window,text="Hello World") # Set label text
label.place(x=0,y=0) # Location of text

window.mainloop() # Listen for Events