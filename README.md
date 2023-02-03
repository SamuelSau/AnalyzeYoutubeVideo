# AnalyzeYoutubeVideo

This program serves to read the URL of a Youtube video and compute the sentiment analysis based on the given comments.
The backend comprises of formatting the URL to extract the video id and collect all the top and reply comments for a video.
Then, perform language translation and using Google's BERT pretrained transformer model for NLP, rate each comment using stars and output the majority of the sentiment.  
