using System;
using Google.Cloud.Translation.V2;

class Program
{
    static string TranslateToGerman(string englishPhrase)
    {
        try
        {
            // Initialize the Google Cloud Translation client
            TranslationClient client = TranslationClient.Create();
            var response = client.TranslateText(englishPhrase, "de", "en");
            return response.TranslatedText;
        }
        catch (Exception e)
        {
            return $"Error during translation: {e.Message}";
        }
    }

    static void Main(string[] args)
    {
        Console.WriteLine("Welcome to the English to German Translator!");
        Console.WriteLine("Type 'exit' to quit the application.\n");

        while (true)
        {
            Console.Write("Enter an English phrase to translate: ");
            string englishPhrase = Console.ReadLine()?.Trim();

            if (string.Equals(englishPhrase, "exit", StringComparison.OrdinalIgnoreCase))
            {
                Console.WriteLine("Exiting the translator. Goodbye!");
                break;
            }

            string germanTranslation = TranslateToGerman(englishPhrase);
            Console.WriteLine($"German translation: {germanTranslation}\n");
        }
    }
}