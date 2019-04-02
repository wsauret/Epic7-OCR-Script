"""
Copyright (r) by CompeAnansi

Export gear using OCR for E7

"""

from PIL import Image
from pytesseract import image_to_string
import pytesseract
from glob import glob
from string import ascii_lowercase, digits
import random
import cv2
import json
from matplotlib import pyplot as plt

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
TESSDATA_PREFIX = 'C:\Program Files (x86)\Tesseract-OCR'


def process(k, img):
    if k == 'level' or k == 'plus':
        thresh = cv2.THRESH_BINARY
        low = 50
        proc = cv2.cvtColor(cv2.medianBlur(
            cv2.threshold(~cv2.cvtColor(cv2.resize(img, (0, 0), fx=5, fy=5), cv2.COLOR_BGR2GRAY), low, 255, thresh)[1],
            3), cv2.COLOR_GRAY2RGB)
        data = image_to_string(Image.fromarray(proc), lang='eng', config='--psm 7')
        if not any(i.isdigit() for i in data):
            low = 100
            proc = cv2.cvtColor(cv2.medianBlur(
                cv2.threshold(~cv2.cvtColor(cv2.resize(img, (0, 0), fx=5, fy=5), cv2.COLOR_BGR2GRAY), low, 255, thresh)[
                    1], 3), cv2.COLOR_GRAY2RGB)
            data = image_to_string(Image.fromarray(proc), lang='eng', config='--psm 7')
            if not any(i.isdigit() for i in data):
                low = 125
                proc = cv2.cvtColor(cv2.medianBlur(
                    cv2.threshold(~cv2.cvtColor(cv2.resize(img, (0, 0), fx=5, fy=5), cv2.COLOR_BGR2GRAY), low, 255,
                                  thresh)[1], 3), cv2.COLOR_GRAY2RGB)
                data = image_to_string(Image.fromarray(proc), lang='eng', config='--psm 7')
    else:
        thresh = cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU
        low = 0
        proc = cv2.cvtColor(cv2.medianBlur(
            cv2.threshold(cv2.cvtColor(cv2.resize(img, (0, 0), fx=5, fy=5), cv2.COLOR_BGR2GRAY), low, 255, thresh)[1],
            3), cv2.COLOR_GRAY2RGB)
        data = image_to_string(Image.fromarray(proc), lang='eng', config='--psm 6')
    return data


def stat_converter(stat):
    result = ''
    if 'attack' in stat.lower():
        result = 'Atk'
        if '%' in stat:
            result += 'P'
    if 'health' in stat.lower():
        result = 'HP'
        if '%' in stat:
            result += 'P'
    if 'defense' in stat.lower():
        result = 'Def'
        if '%' in stat:
            result += 'P'
    if 'speed' in stat.lower():
        result = 'Spd'
    if 'chance' in stat.lower():
        result = 'CChance'
    if 'damage' in stat.lower():
        result = 'CDmg'
    if 'effectiveness' in stat.lower():
        result = 'Eff'
    if 'resistance' in stat.lower():
        result = 'Res'
    return result


def digit_filter(val):
    return int(''.join(filter(str.isdigit, val)))


def char_filter(val):
    return ''.join(filter(str.isalpha, val)).capitalize()


# Format for optimizer
export = {"processVersion": "1", "heroes": [
    {"devotion": "", "artifactStats": {"atk": 0, "hp": 0}, "count": 1, "name": "Angelica 1", "level": 60, "awakened": 5,
     "baseHeroId": "angelica", "equipment": {}, "id": "jtm1cdd3"},
    {"devotion": "", "artifactStats": {"atk": 0, "hp": 0}, "count": 1, "name": "Baal & Sezan 1", "level": 60,
     "awakened": 5, "baseHeroId": "baalsezan", "equipment": {}, "id": "jtm1ctbp"},
    {"devotion": "", "artifactStats": {"atk": 0, "hp": 0}, "count": 1, "name": "Zeno 1", "level": 60, "awakened": 4,
     "baseHeroId": "zeno", "equipment": {}, "id": "jtm1ebse"},
    {"devotion": "", "artifactStats": {"atk": 0, "hp": 0}, "count": 1, "name": "Sigret 1", "level": 60, "awakened": 4,
     "baseHeroId": "sigret", "equipment": {}, "id": "jtm1fodz"},
    {"devotion": "", "artifactStats": {"atk": 0, "hp": 0}, "count": 1, "name": "Schuri 1", "level": 50, "awakened": 4,
     "baseHeroId": "schuri", "equipment": {}, "id": "jtx9kicn"}], "items": []}

# Iterate through the files
filenames = glob(r'C:\Users\Matthew\Documents\python scripts\screenshots\*')
# filenames = ["screenshots/Screenshot_20190327-090940.jpg"]
for name in filenames:
    # Because the height of the item boxes changes depending on the length of the item and set descriptions, we have to
    # crop the top and bottom info separately in order to ensure the OCR boxes within these areas stay fixed.

    img = cv2.imread(name)
    # print(name)

    # Top Box
    temp_top = cv2.imread('e7/top.jpg', 0)
    _, _, _, max_loc = cv2.minMaxLoc(
        cv2.matchTemplate(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), temp_top, cv2.TM_CCOEFF_NORMED))
    # Fixed width, then crop 160 pixels from top triangle
    top_box = img[max_loc[1]:max_loc[1] + 160, 740:1190]
    # cv2.imwrite('e7/top_box.jpg', top_box)

    # Bottom Box
    temp_bot = cv2.imread('e7/bottom.jpg', 0)
    _, _, _, max_loc = cv2.minMaxLoc(
        cv2.matchTemplate(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), temp_bot, cv2.TM_CCOEFF_NORMED))
    # Fixed width, shift down 25 from divider, then crop 335 pixels deep
    bottom_box = img[max_loc[1] + 25:max_loc[1] + 360, 740:1190]
    # cv2.imwrite('e7/bottom_box.jpg', bottom_box)

    # Setup item dictionary
    id_num = "jt" + "".join(random.choice(digits + ascii_lowercase) for _ in range(6))
    item = {"locked": False, "efficiency": 0, "id": id_num}

    # Process top image
    top_coords = {'type': [[20, 70], [172, 432]],
                  'level': [[19, 44], [37, 66]],
                  'plus': [[11, 34], [139, 168]]}
    for k in top_coords.keys():
        data = process(k, top_box[top_coords[k][0][0]:top_coords[k][0][1], top_coords[k][1][0]:top_coords[k][1][1]])
        # print(data)
        if k == 'type':
            item["rarity"] = char_filter(data.split(' ')[0])
            item["slot"] = char_filter(data.split(' ')[1].split('\n')[0])
        if k == 'level':
            item["level"] = digit_filter(data.replace('S', '5').replace('B', '8').replace('a', '8'))
        if k == 'plus':
            item["ability"] = digit_filter(data.replace('S', '5').replace('B', '8').replace('a', '8'))

    # Process bottom image
    bot_coords = {'main': [[8, 70], [65, 435]],
                  'subs': [[98, 255], [25, 435]],
                  'set': [[280, 340], [76, 435]]}
    for k in bot_coords.keys():
        data = process(k, bottom_box[bot_coords[k][0][0]:bot_coords[k][0][1], bot_coords[k][1][0]:bot_coords[k][1][1]])
        if k == 'main':
            # print(data)
            stat = stat_converter(data)
            val = digit_filter(data)
            item["mainStat"] = [stat, val]
        if k == 'subs':
            # print(data.split('\n'))
            for n, entry in enumerate(data.split('\n')):
                stat = stat_converter(entry)
                val = digit_filter(entry.replace('T%', '7%'))
                item['subStat' + str(n + 1)] = [stat, val]
        if k == 'set':
            # print(data)
            item["set"] = char_filter(data.split(' Set')[0])
    export["items"].append(item)
    # print(item)
    print(len(export['items']), len(filenames))

# export["heroes"].append(chars)

# Export to json for importing into optimizer: https://eseo-8a854.firebaseapp.com/
with open('e7/endure.json', 'w') as fp:
    json.dump(export, fp)

"""
# TROUBLESHOOTING

img = cv2.imread('screenshots/Screenshot_20190327-091811.jpg')
temp_top = cv2.imread('e7/top.jpg', 0)
_, _, _, max_loc = cv2.minMaxLoc(
    cv2.matchTemplate(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), temp_top, cv2.TM_CCOEFF_NORMED))
top_box = img[max_loc[1]:max_loc[1] + 160, 740:1190]

top_coords = {'type': [[20, 70], [172, 432]],
              'level': [[19, 44], [37, 66]],
              'plus': [[11, 34], [139, 168]]}
k = 'plus'
img = top_box[top_coords[k][0][0]:top_coords[k][0][1], top_coords[k][1][0]:top_coords[k][1][1]]
thresh = cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU
low = 0
proc = cv2.cvtColor(cv2.medianBlur(
    cv2.threshold(cv2.cvtColor(cv2.resize(img, (0, 0), fx=5, fy=5), cv2.COLOR_BGR2GRAY), low, 255, thresh)[1], 3),
                    cv2.COLOR_BGR2RGB)
plt.imshow(proc)
plt.show()
image_to_string(Image.fromarray(proc), lang='eng', config='--psm 6')

# TROUBLESHOOTING

img = cv2.imread('screenshots/Screenshot_20190327-091811.jpg')
temp_bot = cv2.imread('e7/bottom.jpg', 0)
_, _, _, max_loc = cv2.minMaxLoc(
    cv2.matchTemplate(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), temp_bot, cv2.TM_CCOEFF_NORMED))
bottom_box = img[max_loc[1] + 25:max_loc[1] + 360, 740:1190]

bot_coords = {'main': [[8, 70], [65, 435]],
              'subs': [[98, 255], [25, 435]],
              'set': [[280, 330], [76, 435]]}
k = 'subs'
img = bottom_box[bot_coords[k][0][0]:bot_coords[k][0][1], bot_coords[k][1][0]:bot_coords[k][1][1]]
thresh = cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU
low = 0
proc = cv2.cvtColor(cv2.medianBlur(
    cv2.threshold(cv2.cvtColor(cv2.resize(img, (0, 0), fx=5, fy=5), cv2.COLOR_BGR2GRAY), low, 255, thresh)[1], 3),
                    cv2.COLOR_BGR2RGB)
plt.imshow(proc)
plt.show()
image_to_string(Image.fromarray(proc), lang='eng', config='--psm 6')
"""
