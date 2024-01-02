
import requests 
import json
from srtranslator.translators.base import Translator
class DeepLXTranslator(Translator):
    max_char = 1500
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def translate(self, text: str, source_language: str, destination_language: str):
        url = f"http://{self.ip}:{self.port}/translate"
        print(url)

        payload = {
            "text": f"{text}",
            "source_lang": f"{source_language}",
            "target_lang": F"{destination_language}"
        }

        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            print("responsed")
            responseJson = json.load(response.text)
            print(responseJson)
            return "aaa"
        except Exception as e:
            print("오류발생")
            print(e)
            return ""
        
 