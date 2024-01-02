from Processor import TranslateProccessor
from srtranslator.translators.deepl_scrap import DeeplTranslator
from srtranslator.translators.deepl_api import DeeplApi
from CustomTranslators.SRTDeepLXTranslator import DeepLXTranslator
deepLx = DeepLXTranslator("34.125.92.47", "1188")
processor = TranslateProccessor(deepLx, r"H:\Tera\udemy\Shader Development from Scratch for Unity with Cg\01 Introduction")
processor.Translate()
Error
