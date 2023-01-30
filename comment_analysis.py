import torch
from transformers import pipeline

# Create a pipeline object for sentiment analysis
pipe = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Pass a comment to the pipeline object
result = pipe("this is some dog water content XD")

# Print out the result, which is a list of dictionaries containing labels and scores
print(result)
    
