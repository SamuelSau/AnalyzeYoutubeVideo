import torch
from transformers import pipeline

def comment_analysis(all_comments):
    
    result_array = []
    # Create a pipeline object for sentiment analysis
    pipe = pipeline(task="sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
    # Pass comments to the pipeline object and append to array
    result = pipe(all_comments)

    result_array.append(result)
    
    return result_array

