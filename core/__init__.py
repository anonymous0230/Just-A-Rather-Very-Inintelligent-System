import random
import webbrowser
import pyttsx3
import os
import webbrowser
import datetime
import math
from deep_translator import GoogleTranslator
import pyaudio
import json
import pyttsx3
engine = pyttsx3.init()

# A class to return system info.

 
class SystemInfo:
    def __init__(self):
        pass
    
    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'The time now is {} {}'.format(now.hour, now.minute)
        return answer

    @staticmethod
    def get_date():
        now = datetime.datetime.now()
        answer = 'Today is {} {}  {}'.format(now.strftime('%B'), now.day, now.year)
        return answer

    @staticmethod
    def get_year():
        now = datetime.datetime.now()
        answer = 'The date is day {} month {} and year {}'.format(now.month, now.day, now.year)
        return answer

    @staticmethod
    def get_month():
        now = datetime.datetime.now()
        answer = 'The month is  {} '.format(now.month)
        return answer




class input:
    def __init__(self):
        pass

    @staticmethod
    def translate(text,some_variable_words):
        text_classisication = read_csv('word_clasification.csv')
        SearchMe = text
        County_word_A = (SearchMe.find(text_classisication))
        County_word_B = (SearchMe.rfind(text_classisication))
        if County_word_A == County_word_B:
            b = (County_word_A)
        
        output_translate = GoogleTranslator(source='auto', target=County_word_C).translate(text)
        return output_translate
    
    #@staticmethod

   #def math_calculate():



'''
a+b	{\displaystyle a+b\,}a+b\,	addition
a-b	{\displaystyle a-b\,}a-b\,	subtraction
a*b	{\displaystyle a\times b\,}a\times b\,	multiplication
a/b	{\displaystyle a\div b\,}a\div b\,	division (see note below)
a//b	{\displaystyle \lfloor a\div b\,\rfloor }\lfloor a\div b\,\rfloor 	floor division (e.g. 5//2=2) - Available in Python 2.2 and later
a%b	{\displaystyle a~{\bmod {~}}b\,}a~{\bmod  ~}b\,	modulo
-a	{\displaystyle -a\,}-a\,	negation
abs(a)	{\displaystyle |a|\,}|a|\,	absolute value
a**b	{\displaystyle a^{b}\,}a^{b}\,	exponent
math.sqrt(a)	{\displaystyle {\sqrt {a}}\,}{\sqrt  {a}}\,	square root
'''