import random
import tweepy
import requests
import os


TWITTER_CONSUMER_API_KEY = os.environ['TWITTER_CONSUMER_API_KEY']
TWITTER_CONSUMER_API_SECRET = os.environ['TWITTER_CONSUMER_API_SECRET']
TWITTER_BEARER_TOKEN =  os.environ['TWITTER_BEARER_TOKEN']
TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

# Twitter APIの認証とAPIオブジェクトの取得
auth = tweepy.OAuthHandler(TWITTER_CONSUMER_API_KEY, TWITTER_CONSUMER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


'''
参考：
https://techacademy.jp/magazine/51411
https://kurozumi.github.io/tweepy/api.html
https://docs.tweepy.org/en/stable/api.html

Tweet Object (https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet)
(必要な分の抜粋)
{
    "created_at": "Sun Aug 22 11:21:21 +0000 2021",
    "id": 1429403312298680300,
    "id_str": "1429403312298680330",
    "text": "自画像 https://t.co/ptBe9hyX0e",
    "display_text_range": [
        0,
        3
    ],
    "entities": {
        "hashtags": [],
        "urls": [],
        "user_mentions": [],
        "symbols": [],
        "media": [
            {
                "id": 1429403224478417000,
                "id_str": "1429403224478416901",
                "indices": [
                    4,
                    27
                ],
                "media_url": "http://pbs.twimg.com/media/E9ZCqMvVgAUQjdy.jpg",
                "media_url_https": "https://pbs.twimg.com/media/E9ZCqMvVgAUQjdy.jpg",
                "url": "https://t.co/ptBe9hyX0e",
                "display_url": "pic.twitter.com/ptBe9hyX0e",
                "expanded_url": "https://twitter.com/fukurousaboten/status/1429403312298680330/photo/1",
            }
        ]
    },
    "favorited": false,
    "retweeted": false,
    "possibly_sensitive": false,
    "filter_level": "low",
    "lang": "ja",
    "timestamp_ms": "1629631281338"
    }

'''


def get_tweet_image_url(json_tweet):

    '''
    Statue (Tweet)に添付されている画像を取得する。
    jsonn_tweet:  Tweet Object
    returns: 画像データ（URL）
    '''
    # 画像があった場合、画像のbinaryを取得する。
    medias = json_tweet['entities']['media']
    if len(medias) > 0:
        media = medias[0]  # 1つ目の添付画像のみ取得する
    else:
        media = None
    
    # MediaのURLから画像のバイナリを朱徳する
    if media:
        url = media['media_url']
        return url
    else:
        return None


def get_tweet_image_binary(json_tweet):
    '''
    Statue (Tweet)に添付されている画像を取得する。
    jsonn_tweet:  Tweet Object
    returns: 画像データ（バイナリ）
    '''
    url = get_tweet_image_url(json_tweet)
    if url:
        image = requests.get(url).content
        return image
    else:
        return None



def reply_to_tweet(in_reply_to_status_id, status_text):
    '''
    Status(Tweet)に対してリプライする。
    in_reply_to_status_id: replyを返す対象のTweetのID
    status_text: Replyのメッセージ
    '''
    status = api.update_status(status=status_text, in_reply_to_status_id=in_reply_to_status_id, auto_populate_reply_metadata='true')
    return status


def generate_tweet_text(json_info_orig, fukurou_name, confidence, max):
    '''
    json_info_orig : 以下の例に示すjson。
    fukurou_name : フクロウの名前. ex. オナガフクロウ属
    confidence: 判定の確かさ ex. 90.9
    max: 出力の最大文字数 (tweetの投稿の最大 = 140)
    {
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
    
    returns: 'これは90.9%で「オナガフクロウ属」だね。学名はSurnia。昼行性。一属一種　日本にはいない。人気は普通。尾羽が長い。'
    '''

    json_info = json_info_orig.copy()  # 元のオブジェクトが変更されないようコピーする
    required = []  # 必ず含める項目
    ignored = ['id', '_rid', '_self', '_etag', '_attachments', '_ts', '日本語名']  # 含めない項目。日本語名は、個別に受け取っている。
    subject_ignored = ['活動', '鳴き方', 'レア（希少）度', '飛び方', '豆知識', '豆知識2', '豆知識3', '人気', '模様の特徴']   # 項目名を含めない

    tweet = ''

    # まず、ignored項目を省く
    for key in ignored:
        json_info.pop(key, None)

    # 日本語名部分
    tweet += f'これは{confidence:.1f}%で「{fukurou_name}」だね。'

    # 必須項目を使う
    for key in required:
        value = json_info[key]
        if key in subject_ignored:
            tweet += f'{value}。'
        else:
            tweet += f'{key}は{value}。'
        json_info.pop(key, None)
    
    # それ以降はランダムで使う。
    keys = json_info.keys()
    for key in random.sample(keys, len(keys)):

        value = json_info[key]
        
        if value and len(value) > 0:   # 項目に値が設定されている場合のみ
            sentence = ''
            if key in subject_ignored:
                sentence += f'{value}。'
            else:
                sentence += f'{key}は{value}。'
            
            # 文字数を超過しそうなら、追加をやめる
            if len(tweet + sentence) > max:
                break
            else:
                tweet += sentence 

    return tweet

