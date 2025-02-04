import tkinter as tk
from tkinter import Canvas, colorchooser

def paint(event):
    x1, y1 = event.x - 2, event.y - 2
    x2, y2 = event.x + 2, event.y + 2
    canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color, width=brush_size)

def change_color():
    global color
    color = colorchooser.askcolor(color=color)[1]

def change_brush_size(size):
    global brush_size
    brush_size = int(size)

def clear_canvas():
    canvas.delete("all")

root = tk.Tk()
root.title("Paint App")

color = "black"
brush_size = 2

canvas = Canvas(root, bg="white", width=600, height=400)
canvas.pack(fill=tk.BOTH, expand=True)
canvas.bind("<B1-Motion>", paint)

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Color", command=change_color).pack(side=tk.LEFT)
tk.Button(frame, text="Clear", command=clear_canvas).pack(side=tk.LEFT)
tk.Scale(frame, from_=1, to=10, orient=tk.HORIZONTAL, label="Size", command=change_brush_size).pack(side=tk.LEFT)

root.mainloop()
