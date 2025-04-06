class Translator:
    def __init__(self):
        self.translations = {
            "hello": "hallo",
            "goodbye": "auf Wiedersehen",
            "please": "bitte",
            "thank you": "danke",
            "yes": "ja",
            "no": "nein",
            "cat": "Katze",
            "dog": "Hund",
            "friend": "Freund",
            "love": "Liebe"
        }

    def translate_to_german(self, english_phrase):
        return self.translations.get(english_phrase.lower(), "Translation not found")