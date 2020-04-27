## Directions for Windows

My friend /u/max030994 also made a live version of this and a video explaining it here: https://www.youtube.com/watch?v=z_-mKcHoWwg

**Step 1**: You will only be able to use this OCR file in conjunction with screenshots of your gear. The screenshots are most easily taken in an emulator. You must set the emulator resolution to 2200x1080. Nox and LDPlayer support this resolution, others may as well.

When taking the screenshots be sure to tap on each piece of gear before screenshotting. Do not hover/hold down your finger on each one, as the placement of the item box is different between tapping and holding.

**Step 2**: Download and install the Anaconda python distribution - https://repo.anaconda.com/archive/Anaconda3-2020.02-Windows-x86_64.exe

**Step 3**: Download and Install Tesseract-OCR - https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.0.0.20190526.exe

**Step 4**: Open CMD prompt. (search -> run -> cmd)

``python -m pip install --upgrade pip``

``pip install pillow``

``pip install pytesseract``

``pip install opencv-python``

``pip install matplotlib``

Run each line in succession. If you get a error like 'python is not recognized', please look up how to add python to the PATH variable)

**Step 5**: Download and extract the files in this repository. Add your 2200x1080 screenshots into the screenshots folder. There is an example image in there so that you know how to take it. Just open your inventory up and click the item and then take a screenshot. Make sure you delete the example screenshot so you don't find it in the optimizer.

**Step 6**: Run Anaconda Navigator. Launch JupyterLab. From within JupyterLab load the "E7 Gear OCR.ipynb" file you downloaded in this repository. Then go to Run > Run All Cells. This will create a json file with all your gear in it in the same folder as E7 Gear OCR.ipynb

**Step 7**: Download the latest version of the optimizer here: https://github.com/Zarroc2762/E7-Gear-Optimizer/releases

Then, you simply import the json into the optimizer, add the heroes you want to optimize your gear for, and proceed.
