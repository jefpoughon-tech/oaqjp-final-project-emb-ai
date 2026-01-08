from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route("/emotionDetector")
def emotion_detect():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        formatted_string = "<b>Invalid text! Please try again!.</b>"
    else:
        formatted_string = "For the given statement, the system response is {}. The dominant emotion is <b>{}</b>.".format(response, response['dominant_emotion'])
    
    return formatted_string

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
