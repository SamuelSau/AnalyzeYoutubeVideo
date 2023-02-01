#Import libraries and modules
from googleapiclient.discovery import build
import os
import re
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

#Create an instance of the FastAPI class
app = FastAPI()

# import modules from other files
from get_replies_comments import get_replies_comments
from get_top_comments import get_top_comments
from comment_analysis import comment_analysis
from translate_comments import translate_comments
from score_analysis import score_analysis   

#Load the API key from the .env file
load_dotenv()
API_KEY = os.environ.get('API_KEY')
youtube = build('youtube', 'v3', developerKey=API_KEY)

#Create a class to define the data model
class VideoData(BaseModel):
    url: str

#Create a route
@app.post("/")
async def sentiment_analysis(data: VideoData):
    
    url = data.url

    match = re.search(r"v=([\w-]+)", url)

    if match:
        video_id = match.group(1)
    else:
    
        return {"Error": "Invalid URL"}
    
    all_comments = []
    
    retrieved_top_comments = get_top_comments(youtube, video_id)
    
    if len(retrieved_top_comments) == 0:
        return {'Error': 'no comments found or no video found'}
    
    all_comments.extend(retrieved_top_comments)
    
    replies_comments = get_replies_comments(youtube, video_id)

    #Video is valid even if there are no replies
    all_comments.extend(replies_comments)
    
    translated_array = translate_comments(all_comments)
    
    if len(translated_array) == 0:
        return {'Error': 'No comments were translated'}

    list_of_sentiments = comment_analysis(translated_array)
    
    overall_sentiment = score_analysis(list_of_sentiments)
    
    return {"Sentiment": overall_sentiment}
