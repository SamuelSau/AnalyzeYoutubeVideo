from googletrans import Translator

def translate_comments(comments):
    translator = Translator()
    translated_comments = []
    for comment in comments:
        translation = translator.translate(comment, dest='en')
        translated_comments.append(translation.text)
    print(translated_comments)
    return translated_comments








