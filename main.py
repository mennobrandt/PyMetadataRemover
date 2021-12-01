from tkinter import *
from tkinter import filedialog
import subprocess
from PIL import Image  # PIL install has been problematic for me. I run the app in VENV, with a local copy of the library.


file_location = []


def upload_file(event=None):
    filename = filedialog.askopenfilename()  # fetches file name
    filename = filename.replace('"', "")  # removes quotation marks from the file directory
    file_location.append(filename)
    print(file_location)


def edit_file():
    image = Image.open(file_location[0])

    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)

    image_without_exif.save((file_location[0]))
    print("it worked")


def view_file():
    subprocess.Popen('explorer /select, ' + (file_location[0]))  # opens the edited file
    # Note: This does not work. Should open file, but is only opening explorer.
    # Should also check whether a file is uploaded.


if __name__ == "__main__":
    root = Tk()
    root.title('Metadata Remover')
    #root.resizable(False, False)  # Makes Tkinter Window Resizeable
    root.geometry('200x200')

    upload_btn = Button(root, text='Upload', command=upload_file)
    upload_btn.grid(row=1, column=1, padx=20)

    submit_btn = Button(root, text='Submit', command=edit_file)
    submit_btn.grid(row=1, column=2, padx=20)

    view_btn = Button(root, text='View File', command=view_file)
    view_btn.grid(row=2, column=1, pady=20)

    root.mainloop()

