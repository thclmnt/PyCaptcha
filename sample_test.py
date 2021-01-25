import PYCAPTCHA as PC
import random
import os

FOLDER="./CAPTCHA/"
try:
    os.mkdir(FOLDER)
except:
    pass

for i in range(10):
    PC.Captcha(random.choice(("math","text")),debug=True).save(FOLDER+str(i)+".png")