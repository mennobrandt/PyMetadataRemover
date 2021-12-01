from tkinter import *
from tkinter import filedialog
import subprocess
from PIL import Image
from PIL import ImageTk


file_location = []


def upload_file(event=None):
    filename = filedialog.askopenfilename()  # fetches file name
    filename = filename.replace('"', "")  # removes quotation marks from the file directory
    file_location.append(filename)

    # Splits the file directory by forward slashes (and puts it into a list)
    # Picks the last item in the file directory, as this is the image name
    prev_text = file_location[0]
    prev_text_split = prev_text.split("/")
    upload_notif.configure(text=prev_text_split[-1])


def edit_file():
    if len(file_location) > 0:
        image = Image.open(file_location[0])

        data = list(image.getdata())
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(data)

        image_without_exif.save((file_location[0]))
        success_notif.configure(text="Metadata Removed")

    else:
        success_notif.configure(text="Upload a File")


def view_file():
    subprocess.Popen('explorer /select, ' + (file_location[0]))  # opens the edited file
    # Note: This does not work. Should open file, but is only opening explorer.
    # Should also check whether a file is uploaded.


if __name__ == "__main__":
    root = Tk()
    root.title('Metadata Remover')
    #root.resizable(False, False)  # Makes Tkinter Window Resizeable
    root.geometry('300x200')

    upload_btn = Button(root, text='Upload', command=upload_file)
    upload_btn.grid(row=1, column=1, padx=20)
    upload_notif = Label(root, text="None Selected")
    upload_notif.grid(row=1, column=2)

    submit_btn = Button(root, text='Submit', command=edit_file)
    submit_btn.grid(row=2, column=1)
    success_notif = Label(root, text="")
    success_notif.grid(row=2, column=2)

    view_btn = Button(root, text='View File', command=view_file)
    view_btn.grid(row=3, column=1, pady=20)

    root.mainloop()

