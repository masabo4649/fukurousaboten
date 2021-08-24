import os
import requests
import json

CUSTOM_VISION_PREDICTION_ENDPOINT_URL = os.environ["CUSTOM_VISION_PREDICTION_ENDPOINT_URL"]
CUSTOM_VISION_PREDICTION_KEY = os.environ["CUSTOM_VISION_PREDICTION_KEY"]

def predict_image(image_url):
    '''
    returns: prediction resultを返す。
    参考: https://southcentralus.dev.cognitive.microsoft.com/docs/services/Custom_Vision_Prediction_3.1/operations/5eb37d24548b571998fde5f5
    '''

    headers = {
        "Prediction-key": CUSTOM_VISION_PREDICTION_KEY, 
        "content-type": "application/json"
    }
    body = {
        "Url" : image_url
    }

    result = requests.post(url=CUSTOM_VISION_PREDICTION_ENDPOINT_URL, data=json.dumps(body), headers=headers )
    return json.loads(result.text)


def get_best_prediction(prediction_result):
    '''
    returns: (tagName:str,  confidence: float)の結果を返す。Predictionに失敗した場合には None を返す。
    '''
    predictions = prediction_result["predictions"]
    if predictions and len(predictions) > 0:
        return (predictions[0]['tagName'], predictions[0]['probability'])
    else:
        return None

