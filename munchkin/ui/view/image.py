from tkinter import Misc
from tkinter.ttk import Label

from PIL import Image, ImageTk

from munchkin.base.validations import validate_exist, validate_text


class UIViewImage:
    @staticmethod
    def base(master: Misc, image: str) -> Label:
        validate_exist("master", master)
        validate_text("image", image)

        # using PIL (Python image library = Pillow) open the image
        # and wrap it into a Tkinter Image to set it within a label
        image = ImageTk.PhotoImage(Image.open(image))
        # set image file name as text to create a textual replacement for
        # the image in case it does not show propertly
        view = Label(master, text=image, image=image)
        # we need to set it individually again as Tkinter does not keep an
        # internal reference and the garbage collector picks up the image object
        # and deletes it due to it no longer being referenced anywhere.
        # if this line is removed the image is not shown.
        view.image = image
        # pack the image to expand for all the master available space
        view.pack(expand=True)

        return view
