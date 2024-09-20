import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QRadioButton, QVBoxLayout

def download_video():
    url = url_entry.text()
    format = "MP4" if mp4_radio.isChecked() else "MP3"
    # Add code here to download the video or audio based on the URL and selected format

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Downloader App")
window.setStyleSheet("background-color: black;")

layout = QVBoxLayout()

url_label = QLabel("Enter URL:")
url_entry = QLineEdit()
layout.addWidget(url_label)
layout.addWidget(url_entry)

format_label = QLabel("Select format:")
layout.addWidget(format_label)

mp4_radio = QRadioButton("MP4")
mp3_radio = QRadioButton("MP3")
mp4_radio.setChecked(True)

layout.addWidget(mp4_radio)
layout.addWidget(mp3_radio)

download_button = QPushButton("Download")
download_button.setStyleSheet("background-color: yellow;")
download_button.clicked.connect(download_video)
layout.addWidget(download_button)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())