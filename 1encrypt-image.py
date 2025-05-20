from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("200x200")

def encrypt_image():
    file1 = filedialog.askopenfile(mode='r', filetypes=[('JPG File', '*.jpg')])
    if file1 is not None:
        file_name = file1.name
        key = entry1.get(1.0, END).strip()
        print(file_name, key)
        fi = open(file_name, 'rb')
        image = fi.read()
        fi.close()
        image = bytearray(image)
        for index, values in enumerate(image):
            image[index] = values ^ int(key)
        fi1 = open(file_name, 'wb')
        fi1.write(image)
        fi1.close()
def decrypt_image():
    file1 = filedialog.askopenfile(mode='r', filetypes=[('JPG File', '*.jpg')])
    if file1 is not None:
        file_name = file1.name
        key = entry2.get(1.0, END).strip()
        print(file_name, key)
        fi = open(file_name, 'rb')
        image = fi.read()
        fi.close()
        image = bytearray(image)
        for index, values in enumerate(image):
            image[index] = values ^ int(key)
        fi1 = open(file_name, 'wb')
        fi1.write(image)
        fi1.close()

b1 = Button(root, text="Encrypt", command=encrypt_image)
b1.place(x=70, y=10)

entry1 = Text(root, height=1, width=10)
entry1.place(x=50, y=50)

b2 = Button(root, text="Decrypt", command=decrypt_image)
b2.place(x=70, y=90)

entry2 = Text(root, height=1, width=10)
entry2.place(x=50, y=130)

root.mainloop()
