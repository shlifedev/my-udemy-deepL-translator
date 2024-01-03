 
import requests 
import json
from srtranslator.translators.base import Translator

class DeepLLocalTranslator(Translator):
    max_char = 1500
    def __init__(self, url):
        self.url = url 
    def translate(self, text: str, source_language: str, destination_language: str): 
        payload = {
            "text": f"{text}", 
            "lang": F"{destination_language}"
        }  
        

        headers = {
            "Content-Type": "application/json"
        }

        try: 
            response = requests.post(self.url, data=json.dumps(payload),headers=headers)
            print(response.text)
            responseJson = json.loads(response.text) 
            print(response.text)
            return responseJson["translated_text"]
        except Exception as e:
            print("오류발생")
            