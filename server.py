"""Emotion Detector Application, Detects Emotion On Input"""

import logging

from flask import Flask, request, render_template, jsonify
from EmotionDetection import emotion_detector

log = logging.getLogger()
app = Flask(__name__)

@app.route('/')
def index():
    """Renders the template of the application"""
    return render_template('index.html')

@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detection():
    """Emotion Detector Based On Input Test"""
    text_to_analyze = request.values.get('textToAnalyze', '')
    log.info("Received text to analyze: %s", text_to_analyze)

    response = emotion_detector(text_to_analyze)
    anger = response.get("anger")
    disgust = response.get("disgust")
    fear = response.get("fear")
    joy = response.get("joy")
    sadness = response.get("sadness")
    dominant_emotion = response.get("dominant_emotion")

    if not dominant_emotion:
        return jsonify({'message': 'Invalid text! Please try again!'})

    return f"For the given statement, the system response is " \
       f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, " \
       f"'joy': {joy}, and 'sadness': {sadness}.\nThe dominant emotion is {dominant_emotion}."


if __name__ == '__main__':
    # To run this application in pycharm debugger remove the debug parameter
    app.run(port=5000, debug=True)
