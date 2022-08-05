from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if (len(Folder_Name)>1):
        locationError.config(text=Folder_Name,fg="green")
    else:
        locationError.config(text="Please Choose Folder!!",fg="red")

#Download Video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntryvar.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()
        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()
        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()   
        else:
            ytdError.config(text="Paste Link Again!!",fg="red")

    #Download function
    select.download(Folder_Name)
    ytdError.config(text="Download Complated")

root = Tk()
root.geometry('350x350')
root.columnconfigure(0,weight=1) #get all content in center
root.resizable(0,0)
root.title("Youtube Video Downloader")

#Youtube Downloader link label
ytdLabel = Label(root,text="Enter the URL of the Video",font=("jost",15))
ytdLabel.grid()

#Entry Box
ytdEntryvar = StringVar()
ytdEntryvar = Entry(root, width=50,textvariable=ytdEntryvar)
ytdEntryvar.grid()

#Error Msg
ytdError = Label(root,text="Eror Msg", fg="red", font=("jost",10))
ytdError.grid()

#Asking save file label
saveLabel = Label(root,text="Save The Video File", font=("jost", 15,"bold"))
saveLabel.grid()

#Buttom Of Save File
saveEntry = Button(root, width=10, bg="red",fg="white",text="Choose Path",command=openLocation)
saveEntry.grid()

#Error Msg Location
locationError = Label(root, text="Error Msg Of Path", fg="red",font=("jost",10))
locationError.grid()

#Select Quality
ytdQuality = Label(root,text="Select Quality",font=("jost",15))
ytdQuality.grid()

#combobox
choices = ["720p","114p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid() 

#Download Buttom
downloadbtn = Button(root,text="Download",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()


root.mainloop()
