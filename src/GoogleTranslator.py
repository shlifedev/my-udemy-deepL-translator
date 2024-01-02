
from srtranslator.translators.base import Translator
from google.oauth2 import service_account
from google.cloud import translate_v3beta1 as translate
class GoogleTranslator(Translator):
    max_char = 1500
    def __init__(self, credential_path, project_id):
        print("try")
        self.project_id = project_id
        self.credential_path = credential_path
        self.credential = service_account.Credentials.from_service_account_file(self.credential_path)

    def translate(self, text: str, source_language: str, destination_language: str):
        print("try")
        client = translate.TranslationServiceClient(credentials=self.credential)
        location = "global"
        parent = f"projects/{self.project_id}/locations/{location}"
        #glossary = client.glossary_path(self.project_id, "global", "loco_translator_glossary");
        #glossary_config = translate.TranslateTextGlossaryConfig(glossary=glossary)
        response = client.translate_text(
            request={
                "parent": parent,
                "contents": [text],
                "mime_type": "text/plain",  # mime types: text/plain, text/html
                "source_language_code": "en-US",
                "target_language_code": "ko-KR",

            }
        )

        translated = "";
        for translation in response.translations:
            print(f"Translated text: {translation.translated_text}")
            translation = translation.translated_text

        return translation