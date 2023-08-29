from tkinter import *
import speedtest

root=Tk()
root.title("internet speed test")
root.geometry("400x400")

title=Label(root,text="Internet Speed Check",fg="red",font=("Lucida Sans",20,"bold"))
title.place(relx=0.5,rely=0.1,anchor=CENTER)

upload_spd=Label(root,text="upload speed",fg="blue",font=("ariel",12))
upload_spd.place(relx=0.7,rely=0.3,anchor=CENTER)

download_spd=Label(root,text="download speed",fg="green",font=("ariel",12))
download_spd.place(relx=0.3,rely=0.3,anchor=CENTER)

show_down=Label(root)
show_down.place(relx=0.3,rely=0.5,anchor=CENTER)

show_upl=Label(root)
show_upl.place(relx=0.7,rely=0.5,anchor=CENTER)


def check():
    sp=speedtest.Speedtest()
    downloadspeed=round(sp.download()/1000000,2)
    show_down["text"]=str(downloadspeed) + " mbps"
    
    uploadspeed=round(sp.upload()/1000000,2)
    show_upl["text"]=str(uploadspeed) +" mbps"
    
check_spd=Button(root,text="check speed",command=check)
check_spd.place(relx=0.5,rely=0.7,anchor=CENTER)



root.mainloop()

