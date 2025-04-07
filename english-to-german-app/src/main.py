from googletrans import Translator

def translate_to_german(english_phrase):
    """
    Translates an English phrase to German using the googletrans library.

    Args:
        english_phrase (str): The English phrase to translate.

    Returns:
        str: The translated German phrase, or an error message if translation fails.
    """
    translator = Translator()
    try:
        translation = translator.translate(english_phrase, src='en', dest='de')
        return translation.text
    except Exception as e:
        return f"Error during translation: {e}"

def main():
    """
    Entry point for the English to German Translator application.

    This function welcomes the user, prompts for English phrases, translates them to German,
    and displays the results. The user can exit the application by typing 'exit'.
    """
    print("Welcome to the English to German Translator!")
    print("Type 'exit' to quit the application.\n")

    while True:
        english_phrase = input("Enter an English phrase to translate: ").strip()
        if english_phrase.lower() == 'exit':
            print("Exiting the translator. Goodbye!")
            break
        if not english_phrase:
            print("Please enter a valid phrase.")
            continue
        german_translation = translate_to_german(english_phrase)
        print(f"German translation: {german_translation}\n")

if __name__ == "__main__":
    main()
    