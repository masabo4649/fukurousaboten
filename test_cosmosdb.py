
def test_list_db():

    import webhook_twitter.cosmosdb as cosmosdb

    client = cosmosdb.client
    cosmosdb.list_databases(client)
    db = cosmosdb.get_database(client, "fukurousaboten")
    cosmosdb.list_Containers(db)
    

def test_insert_tweet():

    import webhook_twitter.cosmosdb as cosmosdb
    import json

    r_tweet = r'{"for_user_id":"1424621424304XX9408","tweet_create_events":[{"created_at":"Sun Aug 15 13:32:13 +0000 2021","id":14268995303XX733308161,"id_str":"1426899530XX7330816","text":"\uff12\u3064\u76ee\u306e\u6295\u7a3f","source":"\u003ca href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\"\u003eTwitter Web App\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":1424621424304529408,"id_str":"1424621424304529408","name":"fukurousaboten","screen_name":"fukurousaboten","location":"\u30b3\u30fc\u30d2\u30fc\u30ab\u30c3\u30d7","url":null,"description":"\u30d5\u30af\u30ed\u30a6\u306f\u30b5\u30dc\u30c6\u30f3\u306f\u30d5\u30af\u30ed\u30a6\u306b\u6fc0\u3057\u304f\u61a7\u308c\u3066\u3044\u308b\u30b5\u30dc\u30c6\u30f3\u3067\u3059\u3002\u65e5\u3005\u30d5\u30af\u30ed\u30a6\u306e\u3053\u3068\u3092\u7814\u7a76\u3057\u3066\u3044\u308b\u306e\u3067\u3001\u3042\u308b\u7a0b\u5ea6\u8a73\u3057\u3044\u3067\u3059\u3002\u597d\u304d\u306a\u30d5\u30af\u30ed\u30a6\u306f\u30b3\u30ce\u30cf\u30ba\u30af\u3068\u30b5\u30dc\u30c6\u30f3\u30d5\u30af\u30ed\u30a6\u3002","translator_type":"none","protected":false,"verified":false,"followers_count":0,"friends_count":0,"listed_count":0,"favourites_count":0,"statuses_count":1,"created_at":"Mon Aug 09 06:39:59 +0000 2021","utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":null,"contributors_enabled":false,"is_translator":false,"profile_background_color":"F5F8FA","profile_background_image_url":"","profile_background_image_url_https":"","profile_background_tile":false,"profile_link_color":"1DA1F2","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/1426415905806831616\/iRJn5LLC_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/1426415905806831616\/iRJn5LLC_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/1424621424304529408\/1628918831","default_profile":true,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null,"withheld_in_countries":[]},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"quote_count":0,"reply_count":0,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[],"urls":[],"user_mentions":[],"symbols":[]},"favorited":false,"retweeted":false,"filter_level":"low","lang":"ja","timestamp_ms":"1629034333198"}]}'
    b_tweet = r_tweet.encode()
    j_tweet = json.loads(b_tweet)
    if j_tweet['tweet_create_events']:
        j_tweet['id'] = str(j_tweet['tweet_create_events'][0]['id'])   
        cosmosdb.insert_tweet(j_tweet)

def test_query_items():

    # テストを実行する際は、IDを実際のものに置き換える必要ある。
    import webhook_twitter.cosmosdb as cosmosdb

    client = cosmosdb.client
    db = cosmosdb.get_database(client, "fukurousaboten")
    tweet_container = cosmosdb.get_Container(db, 'tweet')
    
    items = cosmosdb.query_items(tweet_container, '1424362142430XX29X408')
    items = list(tweet_container.read_all_items(max_item_count=10))

def test_get_fukurou_info():

    import webhook_twitter.cosmosdb as cosmosdb
    onagafukurou = cosmosdb.get_fukuro_info("onagafukurou")
    print (onagafukurou)

def test_dictionary():
    
    test_dict = {
        "key1": "value1",
        "key2": "value2"
    }
    if test_dict['key1']:
        print (test_dict['key1'])
    elif test_dict['key2']:
        print (test_dict['key2'])

    if not 'key3' in test_dict.keys():
        print ("key3 does not exist")


if __name__ == '__main__':

    from testtools import local_settings_helper as helper
    helper.import_to_env()

    test_dictionary()

