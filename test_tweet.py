
from azure import cosmos


def test_tweet():

    import webhook_twitter.tweet as tweet

    test_json = {
    "id":"onagafukurou",
    "日本語名":"オナガフクロウ属",
    "英語名":"",
    "学名":"Surnia",
    "生息地":"",
    "活動":"昼行性",
    "目の色":"黄色",
    "体の色":"茶色",
    "鳴き方":"",
    "レア（希少）度":"一属一種\u3000日本にはいない",
    "人気":"普通",
    "飛び方":"",
    "豆知識":"尾羽が長い",
    "豆知識2":"",
    "_rid":"4RJyAKEGJPsKAAAAAAAAAA==",
    "_self":"dbs/4RJyAA==/colls/4RJyAKEGJPs=/docs/4RJyAKEGJPsKAAAAAAAAAA==/",
    "_etag":"\"0000aa1f-0000-2300-0000-612105a30000\"",
    "_attachments":"attachments/",
    "_ts":1629554083,
    }
    
    tweet1 = tweet.generate_tweet_text(test_json, "オナガフクロウ属", 90.232, 140)
    tweet2 = tweet.generate_tweet_text(test_json, "オナガフクロウ属", 32.232, 140)
    tweet3 = tweet.generate_tweet_text(test_json, "オナガフクロウ属", 79, 140)

    print (f'tweet1 : {tweet1}')
    print (f'tweet2 : {tweet2}')
    print (f'tweet3 : {tweet3}')

def test_all_fukurou_info():
    '''
    すべてのfukurou_infoでtweet文を生成してみる。
    '''

    import webhook_twitter.tweet as tweet
    import webhook_twitter.cosmosdb as cosmosdb
    import random

    fukurou_list = cosmosdb.read_all_fukurou_info()
    for fukurou in fukurou_list:
        for i in range(10):
            confidence = random.random() * 100
            text = tweet.generate_tweet_text(fukurou, fukurou['日本語名'], confidence, 140)
            print (text)



def test_get_tweet_image_url():

    import webhook_twitter.cosmosdb as cosmosdb
    import webhook_twitter.tweet as tweet

    # テスト用のtweetをDBから朱徳する
    create_event = cosmosdb.get_tweet("1429403312298680330")
    tweet_body = create_event['tweet_create_events'][0]

    url = tweet.get_tweet_image_url(tweet_body)
    print (f'url={url}')


def test_reply_to_tweet():
    
    import webhook_twitter.tweet as tweet
    text = "これは36.5%で「メンフクロウ属」だね。生息地は世界中。農場などで、ネズミ退治に利用されている。夜行性。「ギー」とうるさい。茶色。穏やかな性格でペットに向いている人気者。学名はTyto。音を立てずに美しく飛ぶ。目の色は黒。耳が左右違う位置にあり、獲物の位置を音で把握する。"
    status = tweet.reply_to_tweet("1429403312298680330", text)
    print (f'status = \n{status}')


if __name__ == '__main__':

    #　Local実行用の環境変数をセットする
    from testtools import local_settings_helper as helper

    helper.import_to_env()
    
#    test_tweet()    
#    test_all_fukurou_info()
    test_get_tweet_image_url()
#    test_reply_to_tweet()