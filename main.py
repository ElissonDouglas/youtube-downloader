import os
from tkinter import *
from webbrowser import open_new_tab
from utils import PlaylistDownloader, VideoDownloader


def abrir_playlist_downloader():
    """Abre uma nova janela para baixar playlist completa do youtube."""
    playlist = PlaylistDownloader()
    Button(playlist, text='Voltar para janela principal', command=lambda: [
           master.deiconify(), playlist.destroy()]).place(relx=0.5, rely=0.85, anchor=CENTER)
    master.after(100, master.withdraw)


def abrir_video_downloader():
    """Abre uma nova janela para baixar video do youtube."""
    video = VideoDownloader()
    Button(video, text='Voltar para janela principal', command=lambda: [
           master.deiconify(), video.destroy()]).place(relx=0.5, rely=0.85, anchor=CENTER)
    master.after(100, master.withdraw)


master = Tk()
largura = 300
altura = 350
largura_tela = master.winfo_screenwidth()
altura_tela = master.winfo_screenheight()
x = (largura_tela/2) - (largura/2)
y = (altura_tela/2) - (altura/2)
master.title('Youtube Downloader')
master.geometry('%dx%d+%d+%d' % (largura, altura, x, y))
master.resizable(False, False)
img = PhotoImage(file='imagens/ytdown.png')
fundo = Label(master, image=img).place(relx=0.5, rely=0.5, anchor=CENTER)
creditos = Label(master, text='by: Elisson Douglas', cursor='hand2',
                 fg='blue', font=('Arial', 10, 'underline'))
creditos.place(relx=0.5, rely=0.97, anchor=CENTER)
creditos.bind(
    '<Button-1>', lambda x: open_new_tab('https://github.com/ElissonDouglas'))


# Baixar apenas um video
img1 = PhotoImage(file='imagens/botao_video.png')
baixar_video = Button(master, command=lambda: abrir_video_downloader(
), image=img1, borderwidth=0, activebackground='#d9d9d9').place(relx=0.5, rely=0.6, anchor=CENTER)


# Baixar playlist
img2 = PhotoImage(file='imagens/botao_playlist.png')
baixar_playlist = Button(master, image=img2, borderwidth=0, activebackground='#d9d9d9', command=lambda: abrir_playlist_downloader(
)).place(relx=0.5, rely=0.8, anchor=CENTER)


master.mainloop()
