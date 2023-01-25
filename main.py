from googleapiclient.discovery import build
import os
import re
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('API_KEY')

youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_all_comments(youtube, video_id):
    all_comments = []
    request = youtube.commentThreads().list(part='snippet', videoId=video_id, maxResults=100)
    while request:
        response = request.execute()
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            text = re.sub(r'<[^<]+?>', '', comment)
            all_comments.append(text)
            print(item['snippet']['topLevelComment']['snippet']['textDisplay'])
            if 'totalReplyCount' in item['snippet']['topLevelComment']['snippet'] and item['snippet']['topLevelComment']['snippet']['totalReplyCount'] > 0:
                replies_request = youtube.comments().list(
                    part='snippet',
                    parentId=item['snippet']['topLevelComment']['id'],
                    maxResults=100
                )
                while replies_request:
                    replies_response = replies_request.execute()
                    for reply in replies_response['items']:
                        reply_text = re.sub(r'<[^<]+?>', '', reply['snippet']['textDisplay'])
                        all_comments.append(reply_text)
                    replies_request = youtube.comments().list_next(replies_request, replies_response)
        request = youtube.commentThreads().list_next(request, response)
    return all_comments


text_comments = get_all_comments(youtube, 'cO5BV8QaL-4')

print(len(text_comments))

for comment in text_comments:
    print(comment)

