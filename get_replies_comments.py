import re

def get_replies_comments(youtube, video_id):
    retrieved_replies_comments = []
    reply_request = youtube.commentThreads().list(part='replies', videoId=video_id, maxResults=100)
    while reply_request:
        response = reply_request.execute()
        for item in response['items']:
            if 'replies' in item:
                for reply in item['replies']['comments']:
                    text = re.sub(r'<[^<]+?>', '', reply['snippet']['textDisplay'])
                    retrieved_replies_comments.append(text)
        reply_request = youtube.commentThreads().list_next(reply_request, response)
    return retrieved_replies_comments



