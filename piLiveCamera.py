rom Tkinter import *
import tkFont
import subprocess
import os
import numpy as np
import cv2

win = Tk()

def takeLive():
        cap = cv2.VideoCapture(0)
        while(True):
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame',gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

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

liveButton = Button(win, text = "Video", command = takeLive, height = 10, width = 15)
liveButton.pack()

mainloop()
