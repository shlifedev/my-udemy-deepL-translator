import os
import glob

from srtranslator import SrtFile
from src.CustomTranslators.SRTGoogleTranslator import GoogleTranslator

class TranslateProccessor():
    def __init__(self, translator, folder):
        self.translator = translator
        self.folder = folder

    def DeleteExistingKoSrtFiles(self):
        for filepath in glob.glob(os.path.join(self.folder, "**/*_ko.srt"), recursive=True):
            os.remove(filepath)

    def Translate(self):
        self.DeleteExistingKoSrtFiles()
        for filepath in glob.glob(os.path.join(self.folder, "**/*.srt"), recursive=True):
            if os.path.getsize(filepath) > 0:
                # translator = DeeplApi(api_key="c7e92de7-9e1c-2c62-4ad7-b5a175b1054c")
                # translator = DeeplTranslator()
                # translator = GoogleTranslator("credential.json", "sigma-crawler-409122")



                print(f"Translating {filepath}")
                srt = SrtFile(filepath)
                srt.translate(self.translator, "en", "ko")
                srt.wrap_lines()
                srt.save(f"{os.path.splitext(filepath)[0]}_ko.srt")
                self.translator.quit()









