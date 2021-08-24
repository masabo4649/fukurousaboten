import logging
from webhook_twitter import twitter_crc_response, cosmosdb, tweet, customvision
import azure.functions as func
import json


def main(req: func.HttpRequest) -> func.HttpResponse:

    if req.method == "GET":
        crc_token = req.params.get('crc_token')
        if crc_token:
            response_str = twitter_crc_response.get_response(crc_token)
        else:
            response_str = "crc_token is empty"
        return func.HttpResponse(response_str)
    else:
        webhook_data = req.get_body()
        j_event = json.loads(webhook_data)

        # 受け取ったTweetの通知に対して一連の処理を行う
        process_event(j_event)
        return func.HttpResponse("POST Response")


def process_event(j_event):

    # 新規Tweetのイベントの場合のみ、処理を行う。
    if 'tweet_create_events' in j_event.keys():

        j_tweet = j_event['tweet_create_events'][0]
        logging.info(f"Python HTTP trigger function processed webhook_twitter POST tweet_create_events Status_ID = : { j_tweet['id'] }")

        # Eventをデータベースに保存しておく
        cosmosdb.insert_tweet(j_event)

        # Tweetから画像URLを朱徳する
        image_url = tweet.get_tweet_image_url(j_tweet)

        # 画像URLがある場合、画像判別する
        if image_url:
            prediction_result = customvision.predict_image(image_url)
            tagname, confidence = customvision.get_best_prediction(prediction_result)

            # 判別結果から、フクロウの情報をデータベースから検索する
            fukurou_info = cosmosdb.get_fukuro_info(tagname)

            # 判別結果からツイート文を作成する
            text = tweet.generate_tweet_text(fukurou_info, fukurou_info['日本語名'], confidence * 100, 140)

            # ツイートに返信する
            status = tweet.reply_to_tweet(j_tweet['id'], text)
            return status
    
    else:
        logging.info(f"Python HTTP trigger function processed webhook_twitter POST: { j_event.keys() }")
        return None

    
