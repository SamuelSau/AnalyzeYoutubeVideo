import torch
from transformers import pipeline

def comment_analysis(all_comments):
    

    # Create a pipeline object for sentiment analysis
    pipe = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")

    # Pass a comment to the pipeline object
    result = pipe(all_comments)

    # Print out the result, which is a list of dictionaries containing labels and scores

    return result

