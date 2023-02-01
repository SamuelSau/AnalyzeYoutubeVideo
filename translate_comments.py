from googletrans import Translator
import emoji
import re
import time

def translate_comments(comments):
    translator = Translator()
    translated_comments = []
    url_pattern = re.compile(r'https?://\S+')  # pattern to match URLs
    for comment in comments:
        try:
            no_emoji_comment = emoji.demojize(comment)
            no_url_comment = re.sub(url_pattern, '', no_emoji_comment) 
            formatted_text = re.sub(r":(\w+):", r"\1", no_url_comment)
            translation = translator.translate(formatted_text, dest='en')
            translated_comments.append(translation.text)
        except Exception as e:
            # Handle the exception and log the error message
            print("Error: {}".format(str(e)))
            
    return translated_comments






