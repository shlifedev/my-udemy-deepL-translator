from BasicTranslator import TranslateProccessor  
from FreeTranslator import FreeTranslator
from srtranslator.translators.deepl_api import DeeplApi   
from srtranslator.translators.deepl_scrap import DeeplTranslator   
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import time
# from CustomTranslators.SRTDeeplLoc
# alTranslator import DeepLLocalTranslator
# from selenium import webdriver  
#model = DeepLXTranslator2("http://dugtaybf.cloud.sealos.io/translate")
 
#file_path = input('Enter a file path: ')

file_paths = [rf"Z:\home\Sync\Udemy Hub\Mathematics for Computer Games Development using Unity", rf"Z:\home\Sync\Udemy Hub\Ultimate Unity Overview (70+ Tools and Features Explained!)", rf"Z:\home\Sync\Udemy Hub\Complete Blender Creator Learn 3D Modelling for Beginners"]
file_path = rf"Z:\home\Sync\Udemy Hub\Modern Unity UI with UI Toolkit\Modern Unity UI with UI Toolkit"  
def createDriver(): 
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe' 
    driver = webdriver.Chrome(executable_path=r"C:\Program Files\Mozilla Firefox\geckodriver.exe", options=options) 
    return driver

def run():  
    model = DeeplTranslator(createDriver()) 
    processor = TranslateProccessor(model, rf"{file_path}")
    srtCouunt = processor.SRTCount()
    translated = processor.CountAlreadyTranslated()
    
    if(srtCouunt != translated):
        processor.Translate() 


def run_single(filePath):
    model = DeeplTranslator(createDriver()) 
    processor = FreeTranslator(model, rf"{filePath}")
    srtCouunt = processor.SRTCount()
    translated = processor.CountAlreadyTranslated()
    
    if(srtCouunt != translated):
        processor.Translate()
        run_single(path)

 
    
for path in file_paths:
    try:
        run_single(path)
    except:
        time.sleep(5)
        run_single(path)