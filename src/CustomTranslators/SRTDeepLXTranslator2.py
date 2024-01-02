 
import requests 
import json
from srtranslator.translators.base import Translator

class DeepLXTranslator2(Translator):
    max_char = 1500
    def __init__(self, url):
        self.url = url 
    def translate(self, text: str, source_language: str, destination_language: str): 
        payload = {
            "text": f"{text}",
            "source_lang": f"{source_language}",
            "target_lang": F"{destination_language}"
        } 
        headers = {
            "Content-Type": "application/json"
        } 
        try: 
            response = requests.post(self.url, data=json.dumps(payload), headers=headers)  
            responseJson = json.loads(response.text) 
            return responseJson["data"]
        except Exception as e:
            print("오류발생")
            