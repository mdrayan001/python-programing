# Image to Sound Converter 🎵📸

Welcome to the **Image to Sound** project! This script combines Optical Character Recognition (OCR) and Speech Synthesis in Python. It reads text from an image and converts it into an audible MP3 file.

This project is part of my Python programming showcase. You can find more of my projects on my GitHub profile: [@mdrayan001](https://github.com/mdrayan001).

> **Repository Location:** `python-programing/20_PROJECTS/17-image-to-sound-python`

## 🚀 Features
- **OCR**: Extracts text from images using `pytesseract`.
- **Text-to-Speech**: Converts the extracted text into an MP3 file using `gTTS`.

## 🛠️ Dependencies

To run this code, you need to install the following Python libraries:

```bash
pip install pytesseract gTTS Pillow
```

*Note: You must also install the Tesseract OCR engine on your system for `pytesseract` to work. Make sure the Tesseract executable is added to your system's PATH.*

## 💻 How to Run

1. Open your terminal and navigate to the project directory within the repository:
   ```bash
   cd python-programing/20_PROJECTS/17-image-to-sound-python
   ```
2. Place an image with text inside the project directory and name it `image.jpg` (or modify `app.py` to use a different filename).
3. Run the script:
   ```bash
   python app.py
   ```

The script will read the text from the image, print it to the console, and generate a new audio file named `sound.mp3` in the same directory.

## 👤 Author
[mdrayan001](https://github.com/mdrayan001)

Feel free to explore the rest of my repository for more Python projects!
