from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

from get_replies_comments import get_replies_comments
from get_top_comments import get_top_comments

load_dotenv()
API_KEY = os.environ.get('API_KEY')
youtube = build('youtube', 'v3', developerKey=API_KEY)

def main():
    video_id = input('Enter video ID: ')
    all_comments = []
    all_comments.extend(get_top_comments(youtube, video_id))
    all_comments.extend(get_replies_comments(youtube, video_id))
    

if __name__ == '__main__':
    main()

