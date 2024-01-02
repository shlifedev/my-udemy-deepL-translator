from Processor import Processor;
from srtranslator.translators.deepl_scrap import DeeplTranslator
from srtranslator.translators.deepl_api import DeeplApi


processor = Processor(DeeplTranslator(), r"H:\Tera\udemy\Shader Development from Scratch for Unity with Cg\01 Introduction")
processor.Translate()