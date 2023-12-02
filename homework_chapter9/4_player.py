import tkinter as tk
from tkinter import ttk
from pygame import mixer  # 导入pygame库

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("音乐播放器")

        # 数据成员
        self.current_song = tk.StringVar()
        self.current_artist = tk.StringVar()
        self.playing = False

        # 创建界面元素
        self.song_label = tk.Label(root, textvariable=self.current_song, font=("Helvetica", 16))
        self.artist_label = tk.Label(root, textvariable=self.current_artist, font=("Helvetica", 12))
        self.progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.play_button = tk.Button(root, text="播放", command=self.toggle_play)
        self.next_button = tk.Button(root, text="切歌", command=self.next_song)

        # 布局
        self.song_label.pack(pady=10)
        self.artist_label.pack(pady=5)
        self.progress_bar.pack(pady=10)
        self.play_button.pack(side="left", padx=10)
        self.next_button.pack(side="right", padx=10)

        # 模拟歌曲数据
        self.songs = [("song1.mp3", "歌手1"), ("song2.mp3", "歌手2"), ("song3.mp3", "歌手3")]
        self.current_song_index = 0

        # 初始化界面
        self.update_song_info()

    def toggle_play(self):
        self.playing = not self.playing
        if self.playing:
            self.play_button["text"] = "暂停"
            self.play_music()
        else:
            self.play_button["text"] = "播放"
            self.pause_music()

    def play_music(self):
        song_path, _ = self.songs[self.current_song_index]
        mixer.init()  # 初始化mixer
        mixer.music.load(song_path)
        mixer.music.play()

    def pause_music(self):
        mixer.music.pause()

    def next_song(self):
        mixer.music.stop()
        self.current_song_index = (self.current_song_index + 1) % len(self.songs)
        self.update_song_info()
        self.play_music()

    def update_song_info(self):
        current_song, current_artist = self.songs[self.current_song_index]
        self.current_song.set(f"歌名: {current_song}")
        self.current_artist.set(f"歌手: {current_artist}")

# 创建主窗口
root = tk.Tk()
app = MusicPlayer(root)
root.mainloop()
