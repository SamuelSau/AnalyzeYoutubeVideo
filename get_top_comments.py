import re

def get_top_comments(youtube, video_id):
    retrieved_top_comments = []
    request = youtube.commentThreads().list(part='snippet', videoId=video_id, maxResults=100)
    while request:
        response = request.execute()
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            text = re.sub(r'<[^<]+?>', '', comment)
            retrieved_top_comments.append(text)
        request = youtube.commentThreads().list_next(request, response)
    return retrieved_top_comments

