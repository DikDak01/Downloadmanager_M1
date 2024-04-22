
from datetime import datetime
import shutil
import os
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from tkinter import *
from tkinter.ttk import *

download = 'C:/Users/nikna/Downloads'
download_files = os.listdir(download)
download_file = ''

pdf_files = 'C:/Users/nikna/OneDrive/Dokumente/Knowledge' 
txt_files = 'C:/Users/nikna/OneDrive/Dokumente/Knowledge'
py_files = 'C:/Users/nikna/OneDrive/Dokumente/Projekte/Programming/Python/Python Scripts'
mp4_files = 'C:/Users/nikna/Videos'
picture_files = 'C:/Users/nikna/Bilder'


def download_gui():
    
    
    for file in download_files:            
            download_file = file + '.part'  
            
            if file.endswith('.pdf'):
                shutil.copyfile(os.path.join(download, file), os.path.join(pdf_files, file))
                
            elif file.endswith('.txt'):
                shutil.copyfile(os.path.join(download, file), os.path.join(txt_files, file))
                print('The .txt file is in the Knowledge folder')
                
            elif file.endswith('.py'):
                shutil.copyfile(os.path.join(download, file), os.path.join(py_files, file))
                print('The .py file is in the Python Scripts folder')
                
            elif file.endswith('.mp4'):
                shutil.copyfile(os.path.join(download, file), os.path.join(mp4_files, file))
                print('The .mp4 file is in the movie folder')
                
            elif file.endswith('.png') or file.endswith('.jpg'):
                shutil.copyfile(os.path.join(download, file), os.path.join(picture_files, file))
                print('The png or jpg file is in the picture folder')





#Tkinter GUI
gui = Tk()
gui.title("Downloadmanager")
gui.geometry('300x300')


#create a style object
style = Style()

text_box = Text(
    gui,
    height=10,
    width=80)

text_box2 = Text(
    gui,
    height=10,
    width=80)

message = '''Writer: Nik Nak \n Project: Downloadmanager \n''', datetime.now()
message2 = '''#####Introdocution#####\nThis is the UI of my Downloadmanager Project'''

text_box.pack(expand=True)
text_box.insert('end', message)
text_box.config(state = 'disabled')

text_box2.pack(expand=True)
text_box2.insert('end', message2)
text_box2.config(state = 'disabled')

style.configure('W.TButton', font = 
                ('courier new', 10, 'bold'),
                foreground = 'blue')

btn_download = Button(gui, text = 'Download Files!', style = 'W.TButton', command = download_gui)
btn_close = Button(gui, text = 'close the window!', style = 'W.TButton', command = gui.destroy)

btn_download.pack(side = 'top') 
btn_close.pack(side = 'bottom')


gui.mainloop()

#! Watchdog monitors changes
if __name__ == "__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

def on_created(event):
    print(f"hey, {event.src_path} has been created!")

def on_deleted(event):
     print(f"what the f**k! Someone deleted {event.src_path}, idiot!")
 
def on_modified(event):
     print(f"hey nak, {event.src_path} has been modified")
 
def on_moved(event):
    print(f"ok ok ok, you moved {event.src_path} to {event.dest_path}")

my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved

path = "."
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)


my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()