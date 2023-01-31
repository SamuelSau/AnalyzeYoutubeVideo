def score_analysis(list_of_sentiments):
    sentiment_count = {
        'Positive': 0,
        'Slightly Positive': 0,
        'Neutral': 0,
        'Slightly Negative': 0,
        'Negative': 0
    }
    labels = []
    for sublist in list_of_sentiments:
        for d in sublist:
            if isinstance(d, dict) and 'label' in d:
                labels.append(d['label'])
    
    for label in labels:
        if label == '5 stars':
            sentiment_count['Positive'] += 1
        elif label == '4 stars':
            sentiment_count['Slightly Positive'] += 1
        elif label == '3 stars':
            sentiment_count['Neutral'] += 1
        elif label == '2 stars':
            sentiment_count['Slightly Negative'] += 1
        elif label == '1 star':
            sentiment_count['Negative'] += 1
        else:
            print('Error: label not found')
    
    highest_sentiment_count = max(sentiment_count['Negative'], sentiment_count['Slightly Negative'], sentiment_count['Neutral'], sentiment_count['Slightly Positive'], sentiment_count['Positive'])
    
    if highest_sentiment_count == sentiment_count['Positive']:
        return 'Positive'
    elif highest_sentiment_count == sentiment_count['Slightly Positive']:
        return 'Slightly Positive'
    elif highest_sentiment_count == sentiment_count['Neutral']:
        return 'Neutral'
    elif highest_sentiment_count == sentiment_count['Slightly Negative']:
        return 'Slightly Negative'
    elif highest_sentiment_count == sentiment_count['Negative']:
        return 'Negative'
    else:
        return 'Error: highest sentiment count not found'
