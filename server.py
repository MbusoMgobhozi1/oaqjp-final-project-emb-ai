from flask import Flask, request, render_template, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/emotionDetector", methods=["Post"])
def emotion_detection():
    data = request.get_json()
    text_to_analyze = data.get('text', 'I love my life')

    result = emotion_detector(text_to_analyze)

    return jsonify({'emotion': result})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
