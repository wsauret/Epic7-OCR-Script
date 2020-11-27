## Directions for Windows

###### Notice

* I started a new job and so I no longer have much free time. As a result, I have quit playing Epic Seven. This means I no longer have access to gear screenshots to test/debug the script when issues arise. It also means I don't really have enough free time to keep this script updated on my own.

* Happily it seems that we have an active community using this script, so if things break in the future, I will be happy to merge pull requests from you guys to keep it running. If you don't know how to do a pull request but have a proposed code update, just open and issue and paste the new code and I'll manually merge it to the main branch.

###### Screenshots

* To use this script you will need screenshots of all the gear you want to import into the optimizer. The resolution of the screenshots must be **2200x1080**. This is an uncommon resolution (most phones do not match it), so I suggest that you take your screenshots via an **approved emulator** set to an internal resolution of **2200x1080**. You can verify the resolution of your screenshots by examining them in a photo app.

* **Approved Emulators**: Nox and LDPlayer. These will take screenshots at the internal resolution (2200x1080). Test other emulators at your own risk. If you have success with another emulator, feel free to open an [Issue](https://github.com/compeanansi/epic7/issues) and I will add it to the approved list!

* **Emulators that do NOT work**: Bluestacks and MuMu. Neither take screenshots at the internal resolution. Instead the screenshot resolution is determined by the size of the window. DO NOT USE THEM. Their screenshots are unfortunately not compatible with this script.

* Tip: When taking a screenshot be sure to **tap** on each piece of gear to bring up its stats before screenshotting. Do not hold down your finger on each one, as the placement of the item box is different between tapping and holding.

### Installation

###### Python Setup

1. Download and install the **64 bit** Anaconda python 3.x distribution for Windows: https://www.anaconda.com/products/individual

2. Download and install the **64 bit** Tesseract-OCR: https://github.com/UB-Mannheim/tesseract/wiki

    You should install it to the default directory unless you have a good reason not to.

3. The Anaconda python distribution will have installed a launcher named ``Anaconda Navigator``. Run it, then launch ``Powershell Prompt`` from the tile menu. Copy and paste the two lines below into the prompt, in succession, hitting enter after each.

    ``pip install pytesseract``

    ``pip install opencv-python``

    You should see "Successfully installed [package name]" after each. Close the prompt when done.

###### Download and Test the Script

4. Download the files in this repository. To do this, scroll up to the top of this webpage and click the green ``Code`` button, then click ``Download ZIP``. Extract the folder somewhere (I extracted it to the Downloads folder since that was where the ZIP file already was).

5. Return to ``Anaconda Navigator``. Launch ``JupyterLab`` from the tile menu. This will open a browser window. Once it is loaded, look at the sidebar on the left. Navigate to where you extracted the folder (in my case: ``Downloads/epic7-master``). Double click on ``E7 Gear OCR.ipynb``. This will open the code for the OCR script.

6. Let's do a test run! In the menu at the top, click ``Run > Run All Cells``. If you scroll down to the bottom of the window, you'll see a text progress indicator. When you see ``JSON file finished!`` you should see a new file in the sidebar: ``exported_gear.json``. If that file is present and you didn't get any error messages, then the test worked!

    Note: If you are not using Windows, you will need to comment two lines in the settings cell at the top. Otherwise the test run will fail.

###### Copy Screenshots & Run

7. Delete the sample image in the screenshots folder (``epic7-master/screenshots``) that we just tested the script on.

8. Copy your 2200x1080 gear screenshots to ``epic7-master/screenshots`` from wherever you have them stored.

9. Go back to the ``JupyterLab`` browser tab and do ``Run > Run All Cells`` again. This will overwrite ``exported_gear.json`` with one that has all your gear in it. Congratulations! You're done with this script.

###### Optimizer

* Make sure you have the latest version of the optimizer here: https://github.com/Zarroc2762/E7-Gear-Optimizer/releases.

* After launching the optimizer, select ``Import JSON from web optimizer (/u/HyrTheWinter)``. Then click the ``Import`` button and browse to the folder that ``exported_gear.json`` is in and load it. You should see green text at the bottom saying ``Succesfully imported 0 heroes and X items...`` where x is the number of screenshots you took. Congratulations! You've imported your gear into the optimizer.

### Next Steps

###### Sanity Checks

* I highly recommend doing some quick sanity checks of the imported gear to ensure the script didnt make any mistakes.

* The most common error with this OCR library is adding a '7' to the end of the recognized number. So a spd sub of 10 could be recorded as 107. Go to the inventory tab in the optimizer and click each stat column heading to sort the values. Just make sure that none of the highest values are crazy. You may also want to keep an eye out for incorrect ilvls and enhance lvls.

* If everything looks good, then congratulations! You're ready to start optimizing your gear.

###### Using in the Future

1. In the future when you want to refresh your gear, you should first check this github again to see if I updated ``E7 Gear OCR.ipynb``. If I did, download it and replace your old copy.

2. Then all you need to do is to copy your new screenshots into the screenshots folder, open ``E7 Gear OCR.ipynb`` in ``JupyterLab`` (via ``Anaconda Navigator``), then ``Run > Run All Cells``. This will give you your new json file.

3. Finally, when you go to import your new json into the optimizer you have a choice:

    * If you **don't** want to keep the heroes you previously added to the optimizer, then just import the json as above.
    
    * If you **do** want to keep your heroes, I suggest that you first delete all the items in the optimizer (go to the Inventory tab, highlight all the items, click the ``-`` button). Then on the General tab click the ``Append`` button (instead of ``Import``) and load your new json. This will add your up to date gear into the optimizer while keeping your heroes.
