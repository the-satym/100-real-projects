import sys
from PySide6.QtCore import Qt, QUrl
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PySide6.QtWebEngineWidgets import QWebEngineView


class FloatingYouTubePlayer(QMainWindow):
    """
    A floating window to play YouTube videos. It includes a text input for the
    user to paste a URL and a button to load the video.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Floating YouTube Player")

        # --- Window Flags ---
        # Use the native OS window frame but keep it on top of other windows.
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Window)
        self.resize(750, 500)  # Increased height slightly for the new input box
        self.setMinimumSize(360, 240)

        # --- Main Container ---
        container = QWidget()
        # No need for a background color here as the child widgets will cover it.

        main_layout = QVBoxLayout(container)
        main_layout.setContentsMargins(5, 5, 5, 5)  # Add some padding
        main_layout.setSpacing(5)
        self.setCentralWidget(container)

        # --- URL Input Controls ---
        # A horizontal layout for the input box and button.
        controls_layout = QHBoxLayout()

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Paste a YouTube URL here and press Enter...")
        # Trigger the play_video method when the user presses Enter
        self.url_input.returnPressed.connect(self.play_video)

        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.play_video)

        controls_layout.addWidget(self.url_input)
        controls_layout.addWidget(self.play_button)

        # Add the controls layout to the main vertical layout
        main_layout.addLayout(controls_layout)

        # --- YouTube Web View ---
        self.browser = QWebEngineView()
        # Start with a blank page
        self.browser.setUrl(QUrl("about:blank"))

        main_layout.addWidget(self.browser)

    def play_video(self):
        """
        Gets the URL from the input box, converts it to an embeddable format,
        and loads it in the web view.
        """
        # Get the text from the QLineEdit
        url = self.url_input.text()
        if not url:
            return  # Do nothing if the input is empty

        embed_url = self.convert_to_embed(url)
        self.browser.setUrl(QUrl(embed_url))

    def convert_to_embed(self, url):
        """Converts various YouTube URL formats to a standard embed URL."""
        video_id = ""
        url_str = str(url)
        if "watch?v=" in url_str:
            # Standard URL: https://www.youtube.com/watch?v=VIDEO_ID
            video_id = url_str.split("watch?v=")[-1].split("&")[0]
        elif "youtu.be/" in url_str:
            # Shortened URL: https://youtu.be/VIDEO_ID
            video_id = url_str.split("youtu.be/")[-1].split("?")[0]

        if video_id:
            # Return the embed URL with autoplay enabled for a better experience
            return f"https://www.youtube.com/embed/{video_id}?autoplay=1"

        # If it's not a recognizable YouTube link, try loading it directly
        return url_str


if __name__ == "__main__":
    app = QApplication(sys.argv)

    player = FloatingYouTubePlayer()
    player.show()

    sys.exit(app.exec())
