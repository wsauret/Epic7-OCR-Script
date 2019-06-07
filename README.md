Directions by /u/Aicilia: https://www.reddit.com/r/EpicSeven/comments/bv2hkx/ocr_gear_exporter_installation_guide_courtesy_of/

Step 1: Download and Install Python 3.6.1 - https://www.python.org/ftp/python/3.6.1/python-3.6.1.exe

Important: Before you click install now, be sure that Python 3.6 is in your PATH variable

Step 2: Download and Install Tesseract-OCR - https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.0.0.20190526.exe

Step 3: Open CMD prompt. (search -> run -> cmd)
1. python -m pip install --upgrade pip 
2. pip install pillow
3. pip install pytesseract
4. pip3 install opencv-python
5. pip install matplotlib
Each line is its own command. If you get a error like python is not recognized as an internal or external command, you might have forgotten to check the box when installing python, in which case, please look up how to add python to path or uninstall/reinstall)

Step 4: Download and extract the files in this repository. When you're done, click into the folder where you'll find two folders (e7 and screenshots) and two files.

Right click ‘e7_ocr_gear_2200x1080’ and open with Notepad. Make sure that ‘C:/Program Files (x86)/Tesseract-OCR/tesseract’ is indeed the install location of your tesseract, if not, change that line and the line under it that has the folder location.

Then, scroll down to “filenames = glob(r'C:\Users\Matthew\Documents\python scripts\screenshots\*')” and replace 'C:\Users\Matthew\Documents\python scripts\screenshots\*’ with the location of the screenshots folder that was included in the zip you extracted. Make sure you keep the *’ at the end. So for example, if you downloaded and extracted the zip to your desktop, the line should look like: filenames = glob(r'C:\Users\Aicilia\Desktop\epic7-master\epic7-master\screenshots\*')

Save and exit.

After that, you add your 2200x1080 screenshots into the screenshots folder. There is an example image in there so that you know how to take it. Just open your inventory up and click the item and then take a screenshot. Make sure you delete the example screenshot so you don't find it in your optimizer like I discovered earlier. ☹

Once you have put your screenshots in the folder, double click on 'e7_ocr_gear_2200x1080' so you run it (with python). It will go through each image one at a time and have a count of what image out of total it is through. Once it is finished, it will export in .json to the e7 folder with the name 'endure' and automatically close itself. Then, you simply import that into the Epic Seven Equipment Optimizer, delete the example heroes and add your own.
