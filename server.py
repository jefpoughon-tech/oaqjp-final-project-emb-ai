"""
Final project to analyse emotion
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route("/emotionDetector")
def emotion_detect():
    """
    Analyzes the provided text and returns a formatted string of emotions.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    # Check for valid analysis results
    if response.get('dominant_emotion') is None:
        return "<b>Invalid text! Please try again!.</b>", 200

    # Extract dominant emotion for clarity
    dominant_emotion = response['dominant_emotion']

    # Build a clean response using f-strings (Python 3.6+)
    return (
        f"For the given statement, the system response is {response}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )

@app.route("/")
def render_index_page():
    """
    Entry point of website 
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
