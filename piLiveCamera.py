rom Tkinter import *
import tkFont
import subprocess
import os
win = Tk()

def takePic():
        print("Camera Captured")
        subprocess.call(['./webcam-save.sh'])

def quitCamera():
        os.system('clear')
        print("----------------------------------------------------------------------")
        print("Quiting")
        print("Find your pictures in /home/pi/webcam/")
        print("The Pictures are named by that time you took it")
        print("----------------------------------------------------------------------")
        win.quit()

win.title("Camera")
win.geometry("800x480")

picButton = Button(win, text = "Capture Picture", command = takePic, height = 10, width = 15)
picButton.pack(side = TOP)

quitButton = Button(win, text = "Quit", command = quitCamera, height = 10, width = 15)
quitButton.pack(side = BOTTOM)

mainloop()
