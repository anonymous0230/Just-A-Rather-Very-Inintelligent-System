from deep_translator import GoogleTranslator
from deep_translator import MicrosoftTranslator
from deep_translator import PonsTranslator
from deep_translator import LingueeTranslator
from deep_translator import MyMemoryTranslator
from deep_translator import YandexTranslator
from deep_translator import PapagoTranslator
from deep_translator import DeepL
from deep_translator import QCRI
from deep_translator import single_detection
from deep_translator import batch_detection


text = input('what do you wanne translated?')
b =  input('what do you wane translate to')

translated = GoogleTranslator(source='auto', target=b).translate(text=text)
print (translated)
