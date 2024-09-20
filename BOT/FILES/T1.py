import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QRadioButton
from PyQt6.QtGui import QColor

class DownloadWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Telegram Downloader")
        self.setGeometry(100, 100, 400, 200)
        self.setStyleSheet("background-color: black; color: white;")

        layout = QVBoxLayout()

        self.url_input = QLineEdit()
        layout.addWidget(self.url_input)

        self.mp4_radio = QRadioButton("MP4")
        self.mp4_radio.setChecked(True)
        layout.addWidget(self.mp4_radio)

        self.mp3_radio = QRadioButton("MP3")
        layout.addWidget(self.mp3_radio)

        self.download_button = QPushButton("Download")
        self.download_button.setStyleSheet("background-color: blue; color: white;")
        self.download_button.clicked.connect(self.f1)
        layout.addWidget(self.download_button)

        self.setLayout(layout)

    def f1(self):
        from pytube import YouTube

        # YouTube video URL
        video_url = "https://www.youtube.com/watch?v=rzlKZLWOD80"

        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        # Download the video
        stream.download()

        print("Video downloaded successfully!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DownloadWindow()
    window.show()
    sys.exit(app.exec())