import requests
import json
import logging

log = logging.getLogger(__name__)

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v2/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_data = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url=url, headers=headers, json=json_data) 
    log.info("Response from the server: %s", response.json())
    if response.status_code != 200:
        return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
    
    json_results = json.loads(response.text)
    response_dict = json_results.get("emotionPredictions")[0].get("emotion")

    dominant_emotion = None
    dominant_value = float(0)

    for emotion, value in response_dict.values():
        if value > dominant_value:
            dominant_value = value
            dominant_emotion = emotion
        
    response_dict["dominant_emotion"] = dominant_emotion

    return response_dict