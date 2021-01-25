from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
import random
import math


class Img:
    def __init__(self, text, width, height, background=(255, 255, 255), text_color=(0, 0, 0)):
        self.text = text
        self.height = height
        self.width = width
        self.background = background
        self.text_color = text_color
        self.initialize()

    def initialize(self):
        img = Image.effect_noise((self.width, self.height), 100)
        img = img.convert("RGB")
        for x in range(img.width):
            for y in range(img.height):
                coord = (x, y)
                r = random.randrange(0, 255) * img.getpixel((x, y))[0]
                g = random.randrange(0, 255) * img.getpixel((x, y))[1]
                b = random.randrange(0, 255) * img.getpixel((x, y))[2]
                img.putpixel(coord, (r, g, b))

        img = img.filter(ImageFilter.GaussianBlur(1))
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype("Tests/fonts/NotoSans-Regular.ttf", int(0.6*self.height))
        d.text((self.width//2, self.height//2), self.text,anchor="mm", font=font, fill=self.text_color)

        for _ in range(35):
            x1 = random.randrange(0, self.width)
            y1 = random.randrange(0, self.height)
            x2 = random.randrange(0, self.width)
            y2 = random.randrange(0, self.height)
            d.line([x1, y1, x2, y2], fill=(100, 100, 100),width=int(self.width*0.01))

        self.img = img

    def show(self):
        self.img.show()

    def save(self, file):
        self.img.save(file)


class Math:
    def __init__(self):
        self.initialize()

    def initialize(self):
        random.seed()
        self.term_a = random.randrange(1, 9)
        self.term_b = random.randrange(1, 9)
        self.op = random.choice(
            ['+', 'x']
        )
        self.result = self.term_a + self.term_b if self.op == '+' else self.term_a * self.term_b


class Text:
    def __init__(self, size):
        self.initialize()

    def initialize(self):
        random.seed()
        STR = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        text = ''
        for _ in range(4):
            text += random.choice(STR)
        self.text = text


class Captcha:
    def __init__(self, test_type, text_size=4, img_width=200, img_height=100, debug=False):
        self.type = test_type
        self.text_size = text_size
        self.img_width = img_width
        self.img_height = img_height
        self.debug = debug
        self.generate()

    def generate(self):
        if self.type == "math":
            self.captcha = Math()
            self.text = str(self.captcha.term_a)+" " + \
                str(self.captcha.op) + " " + str(self.captcha.term_b)
            self.result = self.captcha.result
            self.img = Img(self.text, self.img_width, self.img_height)

        if self.type == "text":
            self.captcha = Text(self.text_size)
            self.text = self.captcha.text
            self.result = self.captcha.text
            self.img = Img(self.text, self.img_width, self.img_height)

    def display(self):
        if self.type == "math":
            self.img.show()
            if self.debug:
                print("Captcha = "+str(self.text))
            if self.debug:
                print("Result = "+str(self.result))
        if self.type == "text":
            self.img.show()
            if self.debug:
                print("Result = "+str(self.result))

    def save(self, file="test.png"):
        self.img.save(file)
