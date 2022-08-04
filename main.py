from PIL import Image
import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog


def get_image():
    global image_path
    image_path = tk.filedialog.askopenfilename()
    root.destroy()


logo_path = 'img/logo.png'

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = ctk.CTk()  # create CTk window like you do with the Tk window (you can also use normal tkinter.Tk window)
root.geometry("350x180+800+300")
root.title("Watermark your photos!")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1, minsize=200)

# Frame
frame_1 = ctk.CTkFrame(master=root, width=80, height=200, corner_radius=15)
frame_1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
frame_1.grid_columnconfigure(0, weight=1)
frame_1.grid_columnconfigure(1, weight=1)

# Button
button_1 = ctk.CTkButton(master=frame_1, text="Browse", height=40, compound="right", command=get_image)
button_1.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

# Label
title = ctk.CTkLabel(master=frame_1, text="Choose an image to watermark", width=150, height=40, compound="right")
title.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

root.mainloop()

try:
    im1 = Image.open(image_path)
    im2 = Image.open(logo_path)

    w1 = im1.size[0]
    h1 = im1.size[1]

    ratio = w1 / h1

    im2.thumbnail((int(w1*0.15), int(h1*0.15)), Image.Resampling.LANCZOS)

    w2 = im2.size[0]
    h2 = im2.size[1]

    im = Image.new("RGBA", (w1, h1))

    im.paste(im1)
    im.paste(im2, (im1.size[0] - (w2 + 50), im1.size[1] - (h2 + 50)), im2)

    im.show()
except NameError:
    root = ctk.CTk()  # create CTk window like you do with the Tk window (you can also use normal tkinter.Tk window)
    root.geometry("350x100+800+300")
    root.title("Error!")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1, minsize=200)

    # Frame
    frame_1 = ctk.CTkFrame(master=root, width=80, height=200, corner_radius=15)
    frame_1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    frame_1.grid_columnconfigure(0, weight=1)
    frame_1.grid_columnconfigure(1, weight=1)

    # Label
    title = ctk.CTkLabel(master=frame_1, text="You didn't pick a photo to watermark", width=150, height=40,
                         compound="right")
    title.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

    root.mainloop()
except AttributeError:
    root = ctk.CTk()  # create CTk window like you do with the Tk window (you can also use normal tkinter.Tk window)
    root.geometry("350x100+800+300")
    root.title("Error!")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1, minsize=200)

    # Frame
    frame_1 = ctk.CTkFrame(master=root, width=80, height=200, corner_radius=15)
    frame_1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    frame_1.grid_columnconfigure(0, weight=1)
    frame_1.grid_columnconfigure(1, weight=1)

    # Label
    title = ctk.CTkLabel(master=frame_1, text="You didn't pick a photo to watermark", width=150, height=40,
                         compound="right")
    title.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

    root.mainloop()
