import sys
from PySide6.QtCore import Qt, QUrl
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PySide6.QtWebEngineWidgets import QWebEngineView


class FloatingYouTubePlayer(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Floating YouTube Player")

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Window)
        self.resize(750, 500)
        self.setMinimumSize(360, 240)

        container = QWidget()

        main_layout = QVBoxLayout(container)
        main_layout.setContentsMargins(5, 5, 5, 5)  # Add some padding
        main_layout.setSpacing(5)
        self.setCentralWidget(container)

        controls_layout = QHBoxLayout()

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Paste a YouTube URL here and press Enter...")

        self.url_input.returnPressed.connect(self.play_video)

        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.play_video)

        controls_layout.addWidget(self.url_input)
        controls_layout.addWidget(self.play_button)

        main_layout.addLayout(controls_layout)

        self.browser = QWebEngineView()

        self.browser.setUrl(QUrl("about:blank"))

        main_layout.addWidget(self.browser)

    def play_video(self):

        url = self.url_input.text()
        if not url:
            return

        embed_url = self.convert_to_embed(url)
        self.browser.setUrl(QUrl(embed_url))

    def convert_to_embed(self, url):

        video_id = ""
        url_str = str(url)
        if "watch?v=" in url_str:
            video_id = url_str.split("watch?v=")[-1].split("&")[0]
        elif "youtu.be/" in url_str:
            video_id = url_str.split("youtu.be/")[-1].split("?")[0]

        if video_id:
            return f"https://www.youtube.com/embed/{video_id}?autoplay=1"

        return url_str

if __name__ == "__main__":
    app = QApplication(sys.argv)

    player = FloatingYouTubePlayer()
    player.show()

    sys.exit(app.exec())
