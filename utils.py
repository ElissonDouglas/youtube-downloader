from pytube import Playlist, YouTube
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askdirectory
import os


class PlaylistDownloader(Toplevel):
    """Janela de Download de Playlist"""

    def __init__(self: object):
        super().__init__()
        largura = 400
        altura = 300
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        x = (largura_tela/2) - (largura/2)
        y = (altura_tela/2) - (altura/2)
        self.geometry('%dx%d+%d+%d' % (largura, altura, x, y))
        self.resizable(False, False)
        self.title('Playlist Downloader')
        self.link_playlist = StringVar()
        self.l1 = Label(self, text='Cole a URL da playlist:').place(
            relx=0.5, rely=0.1, anchor=CENTER)
        self.entrada = Entry(self, textvariable=self.link_playlist, width=30).place(
            relx=0.5, rely=0.2, anchor=CENTER)
        self.p = StringVar(self)
        self.p.set('Selecione um formato')
        self.opcoesplaylist = [
            'mp3', 'mp4 (Resolução alta)', 'mp4 (Resolução baixa)']
        self.formato = OptionMenu(
            self, self.p, *self.opcoesplaylist).place(relx=0.5, rely=0.3, anchor=CENTER)
        self.d_b2 = Button(self, text='Fazer o Download da playlist', width=30, command=lambda: self.baixar_playlist(self.link_playlist.get(
        ), self.p.get(), askdirectory(initialdir='~/Downloads')), background='#009826').place(relx=0.5, rely=0.58, anchor=CENTER)

    def baixar_playlist(self: object, url: str, formato: str, local: str) -> None:
        self.link_playlist.set('')
        if url == '' or formato not in self.opcoesplaylist:
            self.erro()
        else:
            self.playlist1 = Playlist(url)
            if formato == self.opcoesplaylist[0]:
                for url in self.playlist1:
                    self.video = YouTube(url)
                    self.baixar = self.video.streams.get_audio_only().download(local)
                    self.base, self.ext = os.path.splitext(
                        self.baixar)  # Selecionando Arquivo
                    self.novo_audio = self.base + '.mp3'  # Alteração de Formato
                    os.rename(self.baixar, self.novo_audio)
                showinfo('Sucesso!', 'Playlist Baixada com sucesso!')
            elif self.formato == self.opcoesplaylist[1]:
                for url in self.playlist1:
                    self.video = YouTube(url)
                    self.baixar = self.video.streams.get_highest_resolution().download(local)
                showinfo('Sucesso!', 'Playlist Baixada com sucesso!')
            elif formato == self.opcoesplaylist[2]:
                for url in self.playlist1:
                    self.video = YouTube(url)
                    self.baixar = self.video.streams.get_lowest_resolution().download(local)
                showinfo('Sucesso!', 'Playlist Baixada com sucesso!')

    def erro(self: object):
        """Caso algum dos campos esteja vazio o usuário será avisado"""
        self.errolabel = Label(
            self, text='ERRO: Preencha os campos de URL e formato do arquivo!', fg='red')
        self.errolabel.place(relx=0.5, rely=0.68, anchor=CENTER)
        self.errolabel.after(2000, self.errolabel.destroy)


class VideoDownloader(Toplevel):
    """Janela de Download de Video do Youtube"""

    def __init__(self: object) -> None:
        super().__init__()
        largura = 400
        altura = 300
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        x = (largura_tela/2) - (largura/2)
        y = (altura_tela/2) - (altura/2)
        self.geometry('%dx%d+%d+%d' % (largura, altura, x, y))
        self.resizable(False, False)
        self.title('Video Downloader')
        self.link = StringVar()
        Label(self, text='Cole a URL do vídeo:').place(
            relx=0.5, rely=0.05, anchor=CENTER)
        Entry(self, textvariable=self.link, width=30).place(
            relx=0.5, rely=0.15, anchor=CENTER)
        self.v = StringVar(self)
        self.v.set('Selecione um formato')
        self.opcoes = ['mp3', 'mp4 (Resolução alta)', 'mp4 (Resolução baixa)']
        self.formato = OptionMenu(self, self.v, *self.opcoes).place(relx=0.5,
                                                                    rely=0.25, anchor=CENTER)

        Button(self, text='Fazer o Download do video', width=30, command=lambda: self.baixa_video(self.link.get(
        ), self.v.get(), askdirectory(initialdir='~/Downloads')), background='#009826').place(relx=0.5, rely=0.53, anchor=CENTER)

    def baixa_video(self: object, url: str, formato: str, local: str) -> None:
        self.link.set('')
        if url == '' or formato not in self.opcoes:
            self.erro()
        else:
            if formato == self.opcoes[0]:
                self.video1 = YouTube(url)
                audio = self.video1.streams.get_audio_only().download(local)
                base, ext = os.path.splitext(audio)  # Selecionando Arquivo
                novo_audio = base + '.mp3'  # Alteração de Formato
                os.rename(audio, novo_audio)  # Alterado
                showinfo('Sucesso', 'MP3 Baixado com sucesso!')
            elif formato == self.opcoes[1]:
                self.video1 = YouTube(url)
                video = self.video1.streams.get_highest_resolution().download(local)
                showinfo('Sucesso', 'MP4 Baixado com sucesso!')
            elif formato == self.opcoes[2]:
                self.video1 = YouTube(url)
                video = url.streams.get_lowest_resolution().download(local)
                showinfo('Sucesso', 'MP4 Baixado com sucesso!')

    def erro(self: object):
        """Caso algum dos campos esteja vazio o usuário será avisado"""
        self.errolabel = Label(
            self, text='ERRO: Preencha os campos de URL e formato do arquivo!', fg='red')
        self.errolabel.place(relx=0.5, rely=0.68, anchor=CENTER)
        self.errolabel.after(2000, self.errolabel.destroy)
