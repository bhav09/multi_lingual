import googletrans
from googletrans import Translator

print(list(googletrans.LANGUAGES.values()))
print()
print(len(googletrans.LANGCODES))
#text='je suis'
translator = Translator()
result = translator.translate('Hello Everyone , My name is Bhavishya', dest='fr')

print(result.src)
print(result.dest)
print(result.text)
'''
googletrans.LANGCODES = {value:key for key, value in googletrans.LANGCODES.items()}
print(googletrans.LANGCODES['en'])
'''