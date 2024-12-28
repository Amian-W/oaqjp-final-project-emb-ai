''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion dtection over it using emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response["dominant_emotion"]
    if dominant_emotion is None:
        formatted_response = 'Invalid text! Please try again!'
    else:
        formatted_response = 'For the given statement, the system response is '
        for key,value in response.items():
            formatted_response = formatted_response + f"' {key} ' : {value}" + ', '

    return formatted_response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
