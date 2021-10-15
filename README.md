# stickerResizer

Python Script to resize all images from a folder to sticker size-format for telegram.

### Notes

* _Tested only on Windows 11 Home Insider Preview 22471.1000_
 
### Requirements

* Python 3.8+
* Pillow
  
### Usage

* Execute the script on a folder with the following structure:
```
\root
	|resizer.py
	\input
		|image1.png
		|image2.jpg
		|...
	\output
```
* After execution, output folder should contain telegram-ready resized png versions.