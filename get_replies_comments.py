import re
from googleapiclient.errors import HttpError

def get_replies_comments(youtube, video_id):
    retrieved_replies_comments = []
    i = 0
    try:
        reply_request = youtube.commentThreads().list(part='replies', videoId=video_id, maxResults=100)
        while reply_request and i <= 100:
            response = reply_request.execute()
            for item in response['items']:
                if 'replies' in item:
                    for reply in item['replies']['comments']:
                        text = re.sub(r'<[^<]+?>', '', reply['snippet']['textDisplay'])
                        retrieved_replies_comments.append(text)
                        i+=1
                        if i == 100:
                            return retrieved_replies_comments
            reply_request = youtube.commentThreads().list_next(reply_request, response)
    except HttpError as err:
        if err.resp.status in [403, 404, 500, 503]:
            print('Error: ', err.resp.status)
            return retrieved_replies_comments
        #limit number of comments we can retrieve
    return retrieved_replies_comments



