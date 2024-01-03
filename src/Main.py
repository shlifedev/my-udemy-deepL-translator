from Processor import TranslateProccessor
from srtranslator.translators.deepl_scrap import DeeplTranslator
from srtranslator.translators.deepl_api import DeeplApi
#from CustomTranslators.SRTDeepLXTranslator import DeepLXTranslator
#from CustomTranslators.SRTDeepLXTranslator2 import DeepLXTranslator2
from CustomTranslators.SRTDeeplLocalTranslator import DeepLLocalTranslator
from selenium import webdriver

#model = DeepLXTranslator2("http://dugtaybf.cloud.sealos.io/translate")
 
#file_path = input('Enter a file path: ')
file_path = r"Y:\Sync\Udemy Hub\Kotlin Coroutines for Android Masterclass"
#print(file_path)
#model = DeeplTranslator(driver=webdriver.Chrome())
#model = DeepLLocalTranslator("http://127.0.0.1:5000/translate")
model = DeeplApi("?")
processor = TranslateProccessor(model, rf"{file_path}")
processor.Translate()