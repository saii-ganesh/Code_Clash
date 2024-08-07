pip install googletrans==4.0.0-rc1
# Install the googletrans library


from googletrans import LANGUAGES
print(LANGUAGES)


from googletrans import Translator, LANGUAGES

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated.text
def main():
    # Display all available languages
    print("Available languages:")
    for lang_code, lang_name in LANGUAGES.items():
        print(f"{lang_code}: {lang_name}")

    # Get user input for the text to be translated
    text_to_translate = input("Enter the text you want to translate: ")

    # Get user input for the source and destination languages
    src_lang = input("Enter the source language code (e.g., 'en' for English): ").strip()
    dest_lang = input("Enter the destination language code (e.g., 'es' for Spanish): ").strip()

    # Translate the text
    translated_text = translate_text(text_to_translate, src_lang, dest_lang)

    # Display the result
    print(f"\nOriginal text ({src_lang}): {text_to_translate}")
    print(f"Translated text ({dest_lang}): {translated_text}")

if __name__ == "__main__":
    main()
