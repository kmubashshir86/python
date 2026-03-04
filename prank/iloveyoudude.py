from tkinter import*

Window=Tk()
Window.configure(bg='black')


import ctypes
while True:
    ctypes.windll.user32.MessageBoxW(0,"love you <3","Dude",1)
    




Window.mainloop()
