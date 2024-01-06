import os
import glob 

class BaseTranslator():
    
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    
    def __init__(self, translator, folder):
        self.translator = translator
        self.folder = folder
    
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
        return None


    

    