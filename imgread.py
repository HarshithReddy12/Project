import tkinter as tk
from tkinter import filedialog
from PIL import Image,ImageTk
from io import BytesIO
import boto3
import codecs
from tkinter.filedialog import askopenfile


def get_imggg(filename, encoding="utf8", errors='ignore'):
    with open(filename.name, 'rb') as imagefile:
        return imagefile.read()


def get_imgb(filename, encoding="utf8", errors='ignore'):
    with open(filename.name, 'rb') as imagefile:
        return imagefile.name


def upload_file():
    aws=boto3.session.Session(profile_name="imguser")
    client=aws.client(service_name="textract", region_name="us-east-1")
    global img
    f_types = [('Jpg Files', "*.jpg")]
    filename = filedialog.askopenfile(filetypes=f_types)
    imgb = get_imgb(filename)
    img = Image.open(imgb)
    i_resize = img.resize((400, 200))
    img = ImageTk.PhotoImage(i_resize)
    b2 = tk.Button(x, image=img)
    b2.pack()
    imggg=get_imggg(filename)
    res=client.detect_document_text(Document={'Bytes':imggg})
    for i in res['Blocks']:
        if i['BlockType']=='LINE':
            print(i['Text'])

x = tk.Tk()
x.geometry("450x450")
x.title("DP Extract")
l = tk.Label(x, text="Upload Your Image", width=30, font=('times', 18, 'bold'))
l.pack()
b = tk.Button(x, text="Upload File", width=30, command=upload_file)
b.pack()

x.mainloop()