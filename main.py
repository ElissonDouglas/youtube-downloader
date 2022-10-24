from tkinter.filedialog import askdirectory
from pytube import YouTube, Playlist
import os
from tkinter import *
from tkinter import messagebox
from webbrowser import open_new_tab



def baixar(linkvideo: str, formato: str, local: str) -> None:
    link.set('')
    if formato == opcoes[0]:
        try:
            url = YouTube(linkvideo)

            audio = url.streams.get_audio_only().download(local)
            base, ext = os.path.splitext(audio) # Selecionando Arquivo

            novo_audio = base + '.mp3' # Alteração de Formato

            os.rename(audio, novo_audio) # Alterado
            messagebox.showinfo('Sucesso', 'MP3 Baixado com sucesso!')
        except:
            pass
    elif formato == opcoes[1]:
        try:
            url = YouTube(linkvideo)
            video = url.streams.get_highest_resolution().download(local)
            messagebox.showinfo('Sucesso', 'MP4 Baixado com sucesso!')
        except:
            pass
    elif formato == opcoes[2]:
        try:
            url = YouTube(linkvideo)
            video = url.streams.get_lowest_resolution().download(local)
            messagebox.showinfo('Sucesso', 'MP4 Baixado com sucesso!')
        except:
            pass
        
def baixar_playlist(link: str, local: str, formato: str) -> None:
    playlist = Playlist(link)
    link_playlist.set('')
    
    if formato == opcoesplaylist[0]:
        for url in playlist:
            video = YouTube(url)
            baixar = video.streams.get_audio_only().download(local)
            base, ext = os.path.splitext(baixar) # Selecionando Arquivo
            novo_audio = base + '.mp3' # Alteração de Formato
            os.rename(baixar, novo_audio)
        messagebox.showinfo('Sucesso!', 'Playlist Baixada com sucesso!')
    elif formato == opcoesplaylist[1]:
        for url in playlist:
            video = YouTube(url)
            baixar = video.streams.get_highest_resolution().download(local)
        messagebox.showinfo('Sucesso!', 'Playlist Baixada com sucesso!')
    elif formato == opcoesplaylist[2]:
        for url in playlist:
            video = YouTube(url)
            baixar = video.streams.get_lowest_resolution().download(local)
        messagebox.showinfo('Sucesso!', 'Playlist Baixada com sucesso!')

             
master = Tk()
largura = 400
altura = 450
teste = Label(master, text='by: Elisson Douglas', cursor='hand2', fg='blue', font=('Arial', 10, 'underline'))
teste.place(relx=0.5, rely=0.97, anchor=CENTER)
teste.bind('<Button-1>', lambda x: open_new_tab('https://github.com/ElissonDouglas'))
largura_tela = master.winfo_screenwidth()
altura_tela = master.winfo_screenheight()
x = (largura_tela/2) - (largura/2)
y = (altura_tela/2) - (altura/2)
master.title('Youtube Downloader')
master.geometry('%dx%d+%d+%d' % (largura, altura, x, y))

# Baixar apenas um video
link = StringVar()
Label(master, text='Cole a URL do vídeo:').place(relx=0.5, rely=0.05, anchor=CENTER)
Entry(master, textvariable=link, width=30).place(relx=0.5, rely=0.1, anchor=CENTER)
v = StringVar(master)
v.set('Selecione um formato')
opcoes = ['mp3', 'mp4 (Resolução alta)', 'mp4 (Resolução baixa)']
formato = OptionMenu(master, v, *opcoes).place(relx=0.5, rely=0.17, anchor=CENTER)
local = StringVar(master)
local.set('Selecione o diretório que deseja salvar.')
Button(master, textvariable=local, width=30, command=lambda: local.set(askdirectory(initialdir='~/Downloads'))).place(relx=0.5, rely=0.25, anchor=CENTER)
Button(master, text='Fazer o Download do video', width=30, command=lambda: baixar(link.get(), v.get(), local.get()), background='#009826').place(relx=0.5, rely=0.35, anchor=CENTER)

# Baixar playlist
link_playlist = StringVar()
Label(master, text='Cole a URL da playlist:').place(relx=0.5, rely=0.5, anchor=CENTER)
Entry(master, textvariable=link_playlist, width=30).place(relx=0.5, rely=0.55, anchor=CENTER)
p = StringVar(master)
p.set('Selecione um formato')
opcoesplaylist = ['mp3', 'mp4 (Resolução alta)', 'mp4 (Resolução baixa)']
formato = OptionMenu(master, p, *opcoesplaylist).place(relx=0.5, rely=0.63, anchor=CENTER)
localplaylist = StringVar(master)
localplaylist.set('Selecione o diretório que deseja salvar.')
Button(master, textvariable=localplaylist, width=30, command=lambda: localplaylist.set(askdirectory(initialdir='~/Downloads'))).place(relx=0.5, rely=0.72, anchor=CENTER)
d_b2 = Button(master, text='Fazer o Download da playlist', width=30, command=lambda: baixar_playlist(link_playlist.get(), localplaylist.get(), p.get()), background='#009826').place(relx=0.5, rely=0.8, anchor=CENTER)




master.mainloop()
