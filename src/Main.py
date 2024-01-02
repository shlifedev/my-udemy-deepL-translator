from Processor import TranslateProccessor
# from srtranslator.translators.deepl_scrap import DeeplTranslator
# from srtranslator.translators.deepl_api import DeeplApi
from CustomTranslators.SRTDeepLXTranslator import DeepLXTranslator
from CustomTranslators.SRTDeepLXTranslator2 import DeepLXTranslator2
print('dd')
model = DeepLXTranslator2("http://dugtaybf.cloud.sealos.io/translate")

#model = DeeplTranslator()
processor = TranslateProccessor(model, r"H:\Tera\Sync\Udemy Hub\Ultimate Unity Overview (70+ Tools and Features Explained!)")
processor.Translate()

