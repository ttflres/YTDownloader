import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os

def download_video():
    url=url_label.get()
    resolution=choose.get()

    pro_label.pack(padx=10, pady=5)
    bar.pack(padx=10, pady=5)
    dstatus.pack(padx=10, pady=5)
    
    try:
        yt=YouTube(url, on_progress_callback=on_progress)
        stream=yt.streams.filter(res=resolution).first()
        os.path.join("downloads", f"{yt.title}.mp4")
        stream.download(output_path="downloads")
        dstatus.configure(text="Done", text_color="green")
    except Exception as e:
        dstatus.configure(text=f"Error{str(e)}", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size=stream.filesize
    bytes_downloaded=total_size-bytes_remaining
    percentage=bytes_downloaded/total_size * 100
    pro_label.configure(text=str(int(percentage))+"%")
    pro_label.update()
    bar.set(float(percentage/100))


#window
root=ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue") 

#title
root.title("Youtube Downloader")

#width and height
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

#content
frame = ctk.CTkFrame(root)
frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

#entry
rlabel = ctk.CTkLabel(frame, text="Enter your URL: ")
url_label = ctk.CTkEntry(frame, width=400, height=40)
rlabel.pack(padx=10, pady=5)
url_label.pack(padx=10, pady=5)
downbutton = ctk.CTkButton(frame, text="Download", command=download_video)
downbutton.pack(padx=10, pady=5)

#choose resolution
res = ["720p", "360p", "240p"]
choose = ctk.StringVar();
res_combobox=ttk.Combobox(frame, values=res, textvariable=choose)
res_combobox.pack(padx=10, pady=5)
res_combobox.set("720p")

#progress
pro_label=ctk.CTkLabel(frame, text="0%")
pro_label.pack(padx=10, pady=5)
bar=ctk.CTkProgressBar(frame, width=400)
bar.set(0)
bar.pack(padx=10, pady=5)
dstatus= ctk.CTkLabel(frame, text="")


#start
root.mainloop()
