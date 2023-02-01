import re
from googleapiclient.errors import HttpError

def get_top_comments(youtube, video_id):
    retrieved_top_comments = []
    i = 0
    try:
        request = youtube.commentThreads().list(part='snippet', videoId=video_id, maxResults=100)
        while request and i <= 100:
            response = request.execute()
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                text = re.sub(r'<[^<]+?>', '', comment)
                retrieved_top_comments.append(text)
                i += 1
                if i == 100:
                    return retrieved_top_comments
            request = youtube.commentThreads().list_next(request, response)
    except HttpError as err:
        if err.resp.status:
            print('Error:', err.resp.status)
            return retrieved_top_comments
    return retrieved_top_comments