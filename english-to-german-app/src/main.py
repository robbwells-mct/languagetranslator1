from googletrans import Translator

def translate_to_german(english_phrase):
    # Use googletrans to translate the phrase
    translator = Translator()
    try:
        translation = translator.translate(english_phrase, src='en', dest='de')
        return translation.text
    except Exception as e:
        return f"Error during translation: {e}"

def main():
    print("Welcome to the English to German Translator!")
    while True:
        english_phrase = input("Enter an English phrase to translate (or type 'exit' to quit): ")
        if english_phrase.lower() == 'exit':
            print("Exiting the translator. Goodbye!")
            break
        german_translation = translate_to_german(english_phrase)
        print(f"German translation: {german_translation}")

if __name__ == "__main__":
    main()