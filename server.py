from flask import Flask, request, render_template, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/emotionDetector", methods=["Get"])
def emotion_detection():
    data = request.get_json()
    text_to_analyze = data.get('text', '')

    result = emotion_detector(text_to_analyze)
    dominant_emotion = result.get("dominant_emotion")
    result.pop("dominant_emotion")

    return f"For the given statement, the system response is {result}. The dominant emotion is {dominant_emotion}"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
