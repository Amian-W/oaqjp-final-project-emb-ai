import requests
import json

# Define a function named sentiment_analyzer that takes a string input (text_to_analyse) 
def emotion_detector(text_to_analyse):
    '''
    This function takes a string input (text_to_analyse)
    and returns response as a text
    '''
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Set the headers with the required model ID for the API
    header ={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    #Convert the response text into a dictionary using the json library functions 
    formatted_response = json.loads(response.text)
    
    emotionPredictions = formatted_response["emotionPredictions"]
    emotion_dict = emotionPredictions[0]
    emotions = emotion_dict.get("emotion")
    # Get the dominant value
    dominant_value = max(emotions.values())
    
    # Get the dominant emotion
    for key, value in emotions.items():
        if value == dominant_value:
            dominant_emotion = key
    
    # Append dominant emotion to emotions dict 
    emotions["dominant_emotion"] = dominant_emotion
    
    return emotions
