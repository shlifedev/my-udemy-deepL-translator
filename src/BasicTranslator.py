import os
import glob 
from srtranslator import SrtFile 
from BaseTranslator import BaseTranslator

class TranslateProccessor(BaseTranslator):
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
                 try:
                     print(f"번역을 시작합니다. {filepath}")
                     srt = SrtFile(filepath)
                     srt.translate(self.translator, "en", "ko")
                     srt.wrap_lines()
                     srt.save(f"{os.path.splitext(filepath)[0]}_ko.srt")
                     print(f"{os.path.splitext(filepath)[0]}_ko.srt 저장되었습니다.")
                     self.translator.quit()
                 except Exception as e:
                     print(f"{filepath} 에 오류가 발생하여 번역에 실패했습니다.: {e}")
                     self.translator.quit()
                     continue