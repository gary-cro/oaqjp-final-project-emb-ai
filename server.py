"""
Final project: Emotion Detector
"""
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request

# Import emotion detection
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    """
    Calls the EmotionDetection package to return the emotion scores
    for a user text input   
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"""For the given statement, the system response is
    'anger': {response['anger']} , 'disgust': {response['disgust']},
     'fear': {response['fear']}, 'joy': {response['joy']}, 'sadness': {response['sadness']}. 
    The dominant emotion is {response['dominant_emotion']}"""

@app.route("/")
def render_index_page():
    """
    Renders the index html page
    """
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
