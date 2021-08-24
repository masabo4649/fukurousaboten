
def test_prediction():
    
    import webhook_twitter.customvision as vision
    import json

    
    result = vision.predict_image("https://pbs.twimg.com/media/E9ZCqMvVgAUQjdy.jpg")
    print (f'result = \n{result}')
    
    tagname, confidence = vision.get_best_prediction(result)
    print (f'tagname={tagname}, confidence={confidence}')

if __name__ == '__main__':

    #　Local実行用の環境変数をセットする
    from testtools import local_settings_helper as helper

    helper.import_to_env()

    # Http RequestをVerboseで実行する
    import http.client as http_client
    import logging
    http_client.HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


    test_prediction()
    
