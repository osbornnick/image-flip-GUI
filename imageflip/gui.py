from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog
from PIL import Image, ImageTk


def get_image():
    filetypes = ()
    filename = askopenfilename(title="Choose an image file to rotate.")
    path.set(filename)
    return filename


def submit():
    im = Image.open(path.get())
    img = ImageTk.PhotoImage(im)
    print(f"Loaded {type(img)} named {img} from {path.get()}")
    panel.configure(text="")
    panel.im = im
    panel.image = img
    panel.configure(image=img)
    root.update_idletasks()


def save():
    filename = path.get()
    type = 'PNG'
    im = panel.im
    im = im.rotate(degrees.get())
    saved_name = filename[:-4] + '-rotated' + '.' + type
    im.save(saved_name, type)
    print(f"Saved {saved_name} as {type} after rotating {degrees.get()} degrees.")


root = Tk()
root.title("Image rotation")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

path = StringVar()
degrees = IntVar()

path_entry = ttk.Entry(mainframe, width=40, textvariable=path)
path_entry.grid(column=1, row=1, sticky=(N, W))
ttk.Button(mainframe, text="Browse", command=get_image).grid(column=2, row=1)

ttk.Button(mainframe, text="Submit", command=submit).grid(column=3, row=1)
panel = ttk.Label(mainframe, text="Select an Image")
panel.grid(column=1, row=2)

ttk.Label(mainframe, text="Degrees rotation:").grid(column=2, row=2)

radios = ttk.Frame(mainframe)
radios.grid(column=3, row=2)

ttk.Radiobutton(radios,
                text="90",
                variable=degrees,
                value=90).grid(column=1, row=1)

ttk.Radiobutton(radios,
                text="180",
                variable=degrees,
                value=180).grid(column=1, row=2)

ttk.Radiobutton(radios,
                text="270",
                variable=degrees,
                value=270).grid(column=1, row=3)

ttk.Button(mainframe, text="Rotate & Save", command=save).grid(column=4, row=2)

root.mainloop()
