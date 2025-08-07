import tkinter as tk
import tkinter.font as tkfont
import ctypes
import pynput as pynput
import threading
import time
import webbrowser
active=False
def toggle():
    global active
    active=not active
    if active:
        threading.Thread(target=autoclick,daemon=True).start()
def handleKey(key):
    if key==pynput.keyboard.Key.f6:
        toggle()

        
listener = pynput.keyboard.Listener(on_release=handleKey)
listener.start()


window=tk.Tk(className="Autoclicker")
window.geometry('300x300')

defaultFont=tkfont.Font(size=20)


tk.Label(window,text='Interval (ms):',font=defaultFont).pack()
intervalBox=tk.Entry(window,width=5,font=defaultFont)
intervalBox.insert(0,"100")
intervalBox.pack()
status=tk.Label(window,text="Status: zzZ",font=defaultFont)
status.pack()
startButton=tk.Button(window,text="Toggle(F6)",command=toggle)
startButton.pack()
credits=tk.Label(window,text="Follow me on GitHub! <3 Duy", fg='blue',cursor='hand2')
credits.bind("<Button-1>",lambda e: webbrowser.open("https://github.com/Banacumbe27"))
credits.pack()

sendInput=ctypes.windll.user32.SendInput
down=0x0002
up=0x0004
def click():
    ctypes.windll.user32.mouse_event(down,0,0,0,0)
    ctypes.windll.user32.mouse_event(up,0,0,0,0)
def autoclick():
    global active   
    try:
        interval=int(intervalBox.get())
        status.config(text="Status: RUNNING")
        while active:
            click()
            time.sleep(interval/1000)
        status.config(text="Status: STOPPED")
        time.sleep(1)
        status.config(text="Status: zzZ")
            
    except:
        status.config(text="Status: Invalid Number")
        active=False
        time.sleep(0.5)
        status.config(text="Status: zzZ")
        
    

window.mainloop()


    