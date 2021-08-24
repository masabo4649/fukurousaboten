

def test_webhook_event():

    import webhook_twitter.__init__ as init
    # テストを実行する際は、IDを実際のものに置き換える必要ある。
    j_event = {
        "for_user_id": "14246214243539408",
        "tweet_create_events": [
            {
                "created_at": "Sun Aug 22 11:21:21 +0000 2021",
                "id": 14246214243539408,
                "id_str": "14246214243539408",
                "text": "自画像 https://t.co/ptBe9hyX0e",
                "display_text_range": [
                    0,
                    3
                ],
                "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
                "quote_count": 0,
                "reply_count": 0,
                "retweet_count": 0,
                "favorite_count": 0,
                "entities": {
                    "hashtags": [],
                    "urls": [],
                    "user_mentions": [],
                    "symbols": [],
                    "media": [
                        {
                            "id": 14246214243539408,
                            "id_str": "14246214243539408",
                            "indices": [
                                4,
                                27
                            ],
                            "media_url": "http://pbs.twimg.com/media/E9ZCqMvVgAUQjdy.jpg",
                            "media_url_https": "https://pbs.twimg.com/media/E9ZCqMvVgAUQjdy.jpg",
                            "type": "photo",
                            "sizes": {
                                "thumb": {
                                    "w": 150,
                                    "h": 150,
                                    "resize": "crop"
                                },
                                "small": {
                                    "w": 680,
                                    "h": 680,
                                    "resize": "fit"
                                },
                                "medium": {
                                    "w": 1200,
                                    "h": 1200,
                                    "resize": "fit"
                                },
                                "large": {
                                    "w": 2048,
                                    "h": 2048,
                                    "resize": "fit"
                                }
                            }
                        }
                    ]
                },
                "filter_level": "low",
                "lang": "ja",
                "timestamp_ms": "1629631281338"
            }
        ],

    }

    status = init.process_event(j_event)
    print (f'status = \n{status}')
    

    

if __name__ == '__main__':

    from testtools import local_settings_helper as helper
    helper.import_to_env()

    test_webhook_event()

    

