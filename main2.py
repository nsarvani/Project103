import sys
import time
import random
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir = "C:/Users/Sarvani Nagothi/OneDrive - San Ramon Valley Unified School District/Desktop/project102"
class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"hey,{event.src_path} has been created!")
    def on_deleted(self,event):
        print(f"oops!! someone deleted {event.src_path}")
    def on_modified (self,event):
        print(f"hey there!, {event.src_path} had been modified")
    def on_moved (self,event):
        print(f"someone moved {event.src_path} to {event.dest_path}")

event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler,from_dir,recursive = True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()