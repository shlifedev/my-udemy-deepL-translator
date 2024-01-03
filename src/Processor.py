import os
import glob
from pathlib import Path

from srtranslator import SrtFile 

class TranslateProccessor():
    def __init__(self, translator, folder):
        self.translator = translator
        self.folder = folder

    # def DeleteExistingKoSrtFiles(self):
    #     for filepath in glob.glob(os.path.join(self.folder, "**/*_ko.srt"), recursive=True):
    #         os.remove(filepath)


    def clean_up_files(self):
        for filepath in glob.glob(os.path.join(self.folder, "*_ko.srt")):
            basename = os.path.basename(filepath).rsplit(".", 1)[0]  # Get filename without extension
            counts = basename.count("_ko")
            if counts > 1:
                os.remove(filepath)
                print(f'Removed incorrect file "{filepath}"')


    def CountAlreadyTranslated(self):
        count = 0
        for filepath in glob.glob(os.path.join(self.folder, "**/*.srt"), recursive=True):
            if '_ko' in os.path.splitext(os.path.basename(filepath))[0]:
                count = count + 1
        return count


    def SRTCount(self):
        filepaths = [f for f in glob.glob(os.path.join(self.folder, "**/*.srt"), recursive=True) if
                     '_ko' not in os.path.basename(f)]
        return len(filepaths)

    def Translate(self):

        filepaths = [f for f in glob.glob(os.path.join(self.folder, "**/*.srt"), recursive=True) if
                     '_ko' not in os.path.basename(f)]


        for filepath in filepaths:
            print(f"{filepath} 차례입니다.")


            srtCouunt = self.SRTCount()
            translated = self.CountAlreadyTranslated()
            print(f"남은 SRT 파일 갯수: {translated}/{srtCouunt}")

            # Skip if filename contains _ko



            ko = filepath.replace(".srt", "_ko.srt");

            if os.path.exists(ko):
                 print(f'File "{filepath}" 이미 번역됨.')
                 continue
            else:
                 print(f"번역을 시작합니다. {filepath}")
                 srt = SrtFile(filepath)
                 srt.translate(self.translator, "en", "ko")
                 srt.wrap_lines()
                 srt.save(f"{os.path.splitext(filepath)[0]}_ko.srt")
                 print(f"{os.path.splitext(filepath)[0]}_ko.srt 저장되었습니다.")
                 self.translator.quit()