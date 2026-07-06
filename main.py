import customtkinter as ctk
import yt_dlp
import imageio_ffmpeg

def download():
    ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
    
    ydl_opts = {
        # Meilleure qualité vidéo et audio
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'ffmpeg_location': ffmpeg_path, 
        'merge_output_format': 'mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url_input.get()])

app = ctk.CTk()
app.geometry("400x200")

url_input = ctk.CTkEntry(app, placeholder_text="Colle le lien ici...", width=300)
url_input.pack(pady=30)

btn = ctk.CTkButton(app, text="Télécharger", command=download, fg_color="red")
btn.pack()

app.mainloop()