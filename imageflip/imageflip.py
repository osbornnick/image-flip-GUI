from PIL import Image, ImageTk
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog


def get_image():
    filetypes = ()
    filename = askopenfilename(title="Choose an image file to rotate.")
    return filename


def rotate(path, degrees):
    im = Image.open(path)
    rotated = im.rotate(degrees)
    return rotated


def run():
    Tk().withdraw()
    filename = askopenfilename(title="Choose an image file to rotate")

    type = filename[-3:].upper()
    path = filename.split('/')
    # save_path = '/'.join(path[:-1])

    im = Image.open(filename)
    imtk = ImageTk.PhotoImage(im)

    degrees = simpledialog.askinteger("Degrees",
                                      "Rotate the image how many degrees?",
                                      minvalue=0,
                                      maxvalue=360
                                      )

    rotated = im.rotate(degrees)

    im.show()
    rotated.show()

    im.save(path[-1] + '-rotated', type)


if __name__ == "__main__":
    run()
