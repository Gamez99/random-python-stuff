from music import play_music
from tkinter import ttk
import tkinter as tk
import threading
import math
import sys

WIN_W, WIN_H = 160, 160

WINDOW_COUNT = 7

radius = 230
center_x = 400
center_y = 300
angles = [i * (360 / WINDOW_COUNT) for i in range(WINDOW_COUNT)]
rotation_speed = 108  # default: 2

root = tk.Tk()
root.geometry("+0+0")
root.resizable(False, False)
icon_path = "img/icon.ico"
root.iconbitmap(icon_path)

image_paths = [f"img/{i}.png" for i in range(1, 8)]
images = [tk.PhotoImage(file=path) for path in image_paths]

windows = []
for i in range(WINDOW_COUNT):
    window = tk.Toplevel(root)
    window.geometry(f"{WIN_W}x{WIN_H}")
    window.iconbitmap(icon_path)  # Set the same icon for each window
    label = tk.Label(window, image=images[i])
    label.pack(expand=True)
    window.overrideredirect(True)
    windows.append(window)

speed_label = ttk.Label(root, text=f"Current Speed: {rotation_speed}")

def __exit(event=None):
    root.destroy()
    sys.exit()

root.protocol("WM_DELETE_WINDOW", __exit)

def update_rotation_speed(value):
    global rotation_speed
    global speed_label
    rotation_speed = int(float(value))
    speed_label.config(text=f"Current Speed: {rotation_speed}")

speed_label.pack()

speed_scale = ttk.Scale(root, from_=2, to=314, orient=tk.HORIZONTAL, command=update_rotation_speed)
speed_scale.pack()

ttk.Button(root, text="Exit", command=__exit).pack()

def move_windows():
    global angles
    for i, window in enumerate(windows):
        x = center_x + int(radius * math.cos(math.radians(angles[i])))
        y = center_y + int(radius * math.sin(math.radians(angles[i])))
        window.geometry(f"+{x}+{y}")
        angles[i] += rotation_speed
    root.after(50, move_windows)

print("is running from main: yes" if __name__ == "__main__" else "is running from main: no")

move_windows()

threading.Thread(target=play_music).start()
root.mainloop()