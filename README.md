# COR Image Watermark App

COR Image Watermark App is a small desktop utility for adding the `@COR_CARES` watermark to an image without having to open an editor or place the text by hand.

Pick an image, and the app puts the watermark at the bottom centre, shows you the result, and saves a new PNG copy. The original image is left alone.

## What it does

- Opens PNG, JPG, JPEG, and GIF images
- Adds a semi-transparent white `@COR_CARES` watermark
- Centres the watermark along the bottom edge with a little padding
- Displays a resized preview in the app window
- Saves the finished image in an `outputs` folder as `<original-name>_watermarked.png`

## Getting started

You will need Python 3 and Pillow.

```bash
git clone https://github.com/okwuchukwuchiedozie-stack/COR-Image-Watermark-App.git
cd COR-Image-Watermark-App
pip install pillow
python main.py
```

On Windows, `py main.py` may be the right command if `python` is not available in your terminal.

## Using the app

1. Start the program.
2. Click **Upload Image**.
3. Choose an image file.
4. The watermarked preview appears in the window.
5. Find the saved PNG in the `outputs` directory next to `main.py`.

For example, choosing `summer-photo.jpg` creates `outputs/summer-photo_watermarked.png`.

## A small note about fonts

The app tries to use Arial at 20 points. If Arial is not installed, it falls back to Pillow’s default font so the watermark can still be added.

## Built with

- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the window and file picker
- [Pillow](https://python-pillow.org/) for reading, drawing on, and saving images

## Project layout

```text
COR-Image-Watermark-App/
├── main.py        # application code
├── README.md      # project guide
└── outputs/       # created when the first image is saved
```

## Ideas for the next version

The watermark text, position, size, and colour are currently set in the code. Useful additions would be controls for those settings, an image/logo watermark option, and batch processing.
