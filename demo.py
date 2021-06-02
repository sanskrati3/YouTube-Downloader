from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
#total size container
file_size=0
obj1 = YouTube()
url = "https://www.youtube.com/watch?v=1I-3vJSC-Vo"
path_to_save_video = "C:\\Users\\Vikrant\\Desktop"
strm = obj1.streams.last()
file_size = strm.filesize
        # print(file_size)
        # print(strm)
        # print(strm.filesize)
        #titl = strm.title
        # print(obj1.description)

titl = StringVar()
titl.set("Label")
label = Label(main, textvariable=titl)
titl.set(strm.title)


main.mainloop()



