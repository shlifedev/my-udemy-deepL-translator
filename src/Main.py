from BasicTranslator import TranslateProccessor  
from FreeTranslator import FreeTranslator
from srtranslator.translators.deepl_api import DeeplApi   
from srtranslator.translators.deepl_scrap import DeeplTranslator   
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
# from CustomTranslators.SRTDeeplLoc
# alTranslator import DeepLLocalTranslator
# from selenium import webdriver  
#model = DeepLXTranslator2("http://dugtaybf.cloud.sealos.io/translate")ㅁㅈㄷ
 
#file_path = input('Enter a file path: ')

file_paths = [rf"/Users/shlifedev/Documents/rclone/nas/Shared folders/Sync/Y Hub/Sebastian Lague"]
 
def createDriver():  
    options = Options() 
    options.headless = True
    driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()), options=options)
    return driver  


def run(filePath):
    model = DeeplTranslator(createDriver()) 
    processor = FreeTranslator(model, rf"{filePath}")
    srtCouunt = processor.getSrtFileCount()
    translated = processor.getTranslatedCount()
    
    if(srtCouunt != translated):
        processor.translate()
        run(path)

 
    
def run_api(filePath, api):  
    model = DeeplApi(api) 
    processor = TranslateProccessor(model, rf"{filePath}")
    srtCouunt = processor.getSrtFileCount()
    translated = processor.getTranslatedCount()
    
    if(srtCouunt != translated):
        processor.translate() 

# run_api(rf"Z:\home\Sync\Udemy Hub\Complete Blender Creator Learn 3D Modelling for Beginners")


 
for path in file_paths:
    try:
        run(path)
    except:
        time.sleep(5)
        run(path)
        
        
        
  