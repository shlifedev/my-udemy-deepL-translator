import os
import glob  
from BaseTranslator import BaseTranslator
from srtranslator import SrtFile 

 
     
    
    
class FreeTranslator(BaseTranslator):
    def __init__(self, translator, folder):
        self.translator = translator
        self.folder = folder 
        
    def translate(self):

        filepaths = [f for f in glob.glob(os.path.join(self.folder, "**/*.srt"), recursive=True) if
                     '_ko' not in os.path.basename(f)]


        for filepath in filepaths:  
            ko = filepath.replace(".srt", "_ko.srt"); 
            if os.path.getsize(filepath) == 0:
                print(f"{self.WARNING} 파일 사이즈가 0인 경우 번역할 수 없습니다. => {filepath} 를 건너띕니다. {self.ENDC}")
                continue
            if os.path.exists(ko):
                 print(f'{self.WARNING}{filepath}"(은)는이미 번역됨. {self.ENDC}')
                 continue 
            if str.__contains__(filepath, "_vi.srt"): 
                 print(f'{self.WARNING}{filepath}"(은)는 베트남어 입니다. {self.ENDC}')
                 continue
            else:
                 try:
                     
                     # print remain count
                     srtCouunt = self.getSrtFileCount()
                     translated = self.getTranslatedCount()
                     print(f"남은 SRT 파일 갯수:  {self.OKGREEN}{translated}/{srtCouunt} {self.ENDC}")
                     
                     
                     print(f"{self.HEADER}번역을 시작합니다. {filepath} {self.ENDC}")  
                     
                     # start translate
                     srt = SrtFile(filepath)
                     srt.translate(self.translator, "en", "ko")
                     srt.wrap_lines()
                     srt.save(f"{os.path.splitext(filepath)[0]}_ko.srt")
                     print(f"{self.BOLD}{os.path.splitext(filepath)[0]}_ko.srt {self.ENDC} {self.OKGREEN}저장되었습니다. {self.ENDC}")
                     self.translator.quit()
                     return None
                 except Exception as e:
                     print(f"{filepath} 에 오류가 발생하여 번역에 실패했습니다.: {e}")
                     self.translator.quit()
                     return None