from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

from get_replies_comments import get_replies_comments
from get_top_comments import get_top_comments
from comment_analysis import comment_analysis
from translate_comments import translate_comments
from score_analysis import score_analysis   

load_dotenv()
API_KEY = os.environ.get('API_KEY')
youtube = build('youtube', 'v3', developerKey=API_KEY)

def main():
    video_id = input('Enter video ID: ')

    all_comments = []
    
    retrieved_top_comments = get_top_comments(youtube, video_id)
    
    if len(retrieved_top_comments) == 0:
        print('Error: no comments found')
        return None
    
    all_comments.extend(retrieved_top_comments)
    
    all_comments.extend(get_replies_comments(youtube, video_id))
    
    len(all_comments)
    
    translated_array = translate_comments(all_comments)
    
    list_of_sentiments = comment_analysis(translated_array)
    
    overall_sentiment = score_analysis(list_of_sentiments)
    
    print(overall_sentiment)
    
if __name__ == '__main__':
    main()

