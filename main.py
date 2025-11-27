import pygame
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import time

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("🎵 Player de Música Python")
        self.root.geometry("500x400")
        self.root.configure(bg='#2C3E50')
        
        # Inicializar pygame mixer
        pygame.mixer.init()
        
        # Variáveis
        self.playlist = []
        self.current_index = 0
        self.paused = False
        self.playing = False
        
        # Configurar interface
        self.setup_ui()
        
    def setup_ui(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#2C3E50')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título
        title_label = tk.Label(
            main_frame, 
            text="🎵 Player de Música", 
            font=('Arial', 18, 'bold'),
            fg='white',
            bg='#2C3E50'
        )
        title_label.pack(pady=10)
        
        # Informações da música atual
        self.song_info = tk.Label(
            main_frame,
            text="Nenhuma música selecionada",
            font=('Arial', 12),
            fg='lightgray',
            bg='#2C3E50',
            wraplength=400
        )
        self.song_info.pack(pady=10)
        
        # Controles
        controls_frame = tk.Frame(main_frame, bg='#2C3E50')
        controls_frame.pack(pady=20)
        
        # Botões
        self.btn_load = tk.Button(
            controls_frame, 
            text="📁 Carregar", 
            command=self.load_music,
            bg='#3498DB',
            fg='white',
            font=('Arial', 10),
            width=10,
            height=2
        )
        self.btn_load.grid(row=0, column=0, padx=5)
        
        self.btn_play = tk.Button(
            controls_frame, 
            text="▶ Play", 
            command=self.play_music,
            bg='#27AE60',
            fg='white',
            font=('Arial', 10),
            width=8,
            height=2
        )
        self.btn_play.grid(row=0, column=1, padx=5)
        
        self.btn_pause = tk.Button(
            controls_frame, 
            text="⏸ Pause", 
            command=self.pause_music,
            bg='#F39C12',
            fg='white',
            font=('Arial', 10),
            width=8,
            height=2
        )
        self.btn_pause.grid(row=0, column=2, padx=5)
        
        self.btn_stop = tk.Button(
            controls_frame, 
            text="⏹ Stop", 
            command=self.stop_music,
            bg='#E74C3C',
            fg='white',
            font=('Arial', 10),
            width=8,
            height=2
        )
        self.btn_stop.grid(row=0, column=3, padx=5)
        
        self.btn_next = tk.Button(
            controls_frame, 
            text="⏭ Next", 
            command=self.next_music,
            bg='#9B59B6',
            fg='white',
            font=('Arial', 10),
            width=8,
            height=2
        )
        self.btn_next.grid(row=0, column=4, padx=5)
        
        # Volume
        volume_frame = tk.Frame(main_frame, bg='#2C3E50')
        volume_frame.pack(pady=10)
        
        tk.Label(
            volume_frame, 
            text="Volume:", 
            font=('Arial', 10),
            fg='white',
            bg='#2C3E50'
        ).pack(side=tk.LEFT)
        
        self.volume_scale = tk.Scale(
            volume_frame,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            length=200,
            command=self.set_volume,
            bg='#34495E',
            fg='white'
        )
        self.volume_scale.set(70)
        self.volume_scale.pack(side=tk.LEFT, padx=10)
        
        # Playlist
        playlist_frame = tk.Frame(main_frame, bg='#2C3E50')
        playlist_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        tk.Label(
            playlist_frame,
            text="Playlist:",
            font=('Arial', 12, 'bold'),
            fg='white',
            bg='#2C3E50'
        ).pack(anchor=tk.W)
        
        self.playlist_box = tk.Listbox(
            playlist_frame,
            bg='#34495E',
            fg='white',
            selectbackground='#3498DB',
            font=('Arial', 10),
            height=8
        )
        self.playlist_box.pack(fill=tk.BOTH, expand=True)
        self.playlist_box.bind('<<ListboxSelect>>', self.on_playlist_select)
        
    def load_music(self):
        files = filedialog.askopenfilenames(
            title="Selecione músicas",
            filetypes=(
                ("Arquivos MP3", "*.mp3"),
                ("Todos os arquivos", "*.*")
            )
        )
        
        if files:
            self.playlist.extend(files)
            self.update_playlist()
            messagebox.showinfo("Sucesso", f"{len(files)} músicas carregadas!")
            
            # Se não está tocando nada, tocar a primeira música
            if not self.playing:
                self.current_index = 0
                self.play_music()
    
    def update_playlist(self):
        self.playlist_box.delete(0, tk.END)
        for file_path in self.playlist:
            file_name = os.path.basename(file_path)
            self.playlist_box.insert(tk.END, file_name)
    
    def play_music(self):
        if not self.playlist:
            messagebox.showwarning("Aviso", "Nenhuma música na playlist!")
            return
        
        try:
            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
            else:
                current_song = self.playlist[self.current_index]
                pygame.mixer.music.load(current_song)
                pygame.mixer.music.play()
                self.playing = True
                
                # Atualizar informações
                file_name = os.path.basename(current_song)
                self.song_info.config(text=f"🎵 Tocando: {file_name}")
                self.highlight_current_song()
                
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível reproduzir a música:\n{str(e)}")
    
    def pause_music(self):
        if self.playing:
            pygame.mixer.music.pause()
            self.paused = True
            self.song_info.config(text="⏸ Música pausada")
    
    def stop_music(self):
        pygame.mixer.music.stop()
        self.playing = False
        self.paused = False
        self.song_info.config(text="⏹ Música parada")
    
    def next_music(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.stop_music()
            time.sleep(0.1)  # Pequeno delay
            self.play_music()
    
    def set_volume(self, value):
        volume = int(value) / 100
        pygame.mixer.music.set_volume(volume)
    
    def highlight_current_song(self):
        self.playlist_box.selection_clear(0, tk.END)
        self.playlist_box.selection_set(self.current_index)
        self.playlist_box.activate(self.current_index)
    
    def on_playlist_select(self, event):
        if self.playlist_box.curselection():
            selected_index = self.playlist_box.curselection()[0]
            if selected_index != self.current_index:
                self.current_index = selected_index
                self.stop_music()
                time.sleep(0.1)
                self.play_music()

def main():
    try:
        root = tk.Tk()
        app = MusicPlayer(root)
        root.mainloop()
    except Exception as e:
        print(f"Erro ao iniciar o player: {e}")
        input("Pressione Enter para sair...")

if __name__ == "__main__":
    main()