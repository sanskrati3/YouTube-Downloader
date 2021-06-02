from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *

# total size container
file_size = 0


# this function is called for updating percentage
def progress(stream=None, chunk=None, file_handle=None, remaining=None):
    # get the per of the file that has been downloaded
    file_downloaded = (file_size - remaining)
    per = (file_downloaded / file_size) * 100
    bstr.config(text="{:00.0f} % downloaded".format(per))

def start_download720():
    global file_size
    try:
        url = urlField.get()
        # changing button text
        bstr.config(text="Please Wait...")
        bstr.config(state=DISABLED)
        # url = "https://www.youtube.com/watch?v=bU78K14x8I8"
        # path_to_save_video = "C:\\Users\\Vikrant\\Desktop"
        path_to_save_video = askdirectory()
        if path_to_save_video is None:
            return

        # creating you tube object with url
        obj1 = YouTube(url, on_progress_callback=progress)

        strm = obj1.streams.first()
        file_size = strm.filesize

        strm.download(path_to_save_video)
        print("done...")
        # changing button text
        bstr.config(text="Start Download")
        bstr.config(state=NORMAL)
        showinfo("Download Finished", "Downloaded\nSuccesfully!")
        urlField.delete(0, END)
    except Exception as e:
        print(e)
        print("Cannot Download Your Video!!")


def StartDownloadThread720():
    # creating thread
    thread = Thread(target=start_download)
    thread.start()


def start_download480():
    global file_size
    try:
        url = urlField.get()
        # changing button text
        bstr.config(text="Please Wait...")
        bstr.config(state=DISABLED)
        # url = "https://www.youtube.com/watch?v=bU78K14x8I8"
        # path_to_save_video = "C:\\Users\\Vikrant\\Desktop"
        path_to_save_video = askdirectory()
        if path_to_save_video is None:
            return

        # creating you tube object with url
        obj1 = YouTube(url, on_progress_callback=progress)

        strm = obj1.streams.last()
        file_size = strm.filesize

        strm.download(path_to_save_video)
        print("done...")
        # changing button text
        bstr.config(text="Start Download")
        bstr.config(state=NORMAL)
        showinfo("Download Finished", "Downloaded\nSuccesfully!")
        urlField.delete(0, END)
    except Exception as e:
        print(e)
        print("Cannot Download Your Video!!")
def StartDownloadThread480():
    # creating thread
    thread = Thread(target=start_download)
    thread.start()



def start_download360():
    global file_size
    try:
        url = urlField.get()
        # changing button text
        bstr.config(text="Please Wait...")
        bstr.config(state=DISABLED)
        # url = "https://www.youtube.com/watch?v=bU78K14x8I8"
        # path_to_save_video = "C:\\Users\\Vikrant\\Desktop"
        path_to_save_video = askdirectory()
        if path_to_save_video is None:
            return

        # creating you tube object with url
        obj1 = YouTube(url, on_progress_callback=progress)

        strm = obj1.streams.last()
        file_size = strm.filesize

        strm.download(path_to_save_video)
        print("done...")
        # changing button text
        bstr.config(text="Start Download")
        bstr.config(state=NORMAL)
        showinfo("Download Finished", "Downloaded\nSuccesfully!")
        urlField.delete(0, END)
    except Exception as e:
        print(e)
        print("Cannot Download Your Video!!")
def StartDownloadThread360():
    # creating thread
    thread = Thread(target=start_download)
    thread.start()


# start making gui
main = Tk()
main.title("YouTube Downloader")
main.iconbitmap("icon.ico")
main.geometry("500x600")
file = PhotoImage(file="download.png", width=300, height=200)
headingIcon = Label(main, image=file)
headingIcon.pack(side=TOP, pady=10)
urlField = Entry(main, font=("verdana", 18), justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10)


bstr = Button(main, text="Start Download", font=("verdana", 18), relief='ridge', command=choice)
bstr.pack(side=TOP, pady=10)
# showing video info
main.mainloop()

