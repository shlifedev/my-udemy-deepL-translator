import os
import glob

from srtranslator import SrtFile
from srtranslator.translators.deepl_api import DeeplApi
from srtranslator.translators.deepl_scrap import DeeplTranslator
from GoogleTranslator import GoogleTranslator

def DeleteExistingKoSrtFiles(folder):
    for filepath in glob.glob(os.path.join(folder, "**/*_ko.srt"), recursive=True):
        os.remove(filepath)

def Translate(folder):
    DeleteExistingKoSrtFiles(folder)
    for filepath in glob.glob(os.path.join(folder, "**/*.srt"), recursive=True):
        if os.path.getsize(filepath) > 0:
            # translator = DeeplApi(api_key="c7e92de7-9e1c-2c62-4ad7-b5a175b1054c")
            # translator = DeeplTranslator()

            ko_filepath = f"{os.path.splitext(filepath)[0]}_ko.srt"
            if os.path.exists(ko_filepath):
                os.remove(ko_filepath)


            translator = GoogleTranslator("credential.json","sigma-crawler-409122")
            srt = SrtFile(filepath)
            srt.translate(translator, "en", "ko")
            srt.wrap_lines()
            srt.save(f"{os.path.splitext(filepath)[0]}_ko.srt")
            translator.quit()






