from googletrans import Translator
import easyocr
import PIL

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from PIL import ImageDraw
from gtts import gTTS

reader = easyocr.Reader(['ta'])
translator = Translator()

im = PIL.Image.open("/Users/gauravsrivastava/PycharmProjects/OcrTTS/data/ocrTest.jpg")


