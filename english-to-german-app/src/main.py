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
    """
    Main function for the English to German Translator application.

    This function serves as the entry point for the application. It welcomes the user,
    prompts them to input English phrases for translation, and displays the corresponding
    German translations. The user can exit the application by typing 'exit'.

    Workflow:
    1. Displays a welcome message.
    2. Continuously prompts the user for an English phrase.
    3. Translates the input phrase to German using the `translate_to_german` function.
    4. Displays the German translation.
    5. Exits the loop and terminates the program when the user types 'exit'.

    Note:
    - The `translate_to_german` function must be implemented for this function to work correctly.

    Raises:
    - No exceptions are explicitly raised in this function, but errors may occur if
        `translate_to_german` is not defined or behaves unexpectedly.
    """
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