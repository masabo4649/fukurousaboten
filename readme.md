Twitterに投稿された画像を判別し、判別結果をリプライするアプリケーション。

## 使用しているサービス
- Azure Functions
- Azure CosmosDB (SQL/Core)
    - Tables
        - tweet - Webhookで受け取ったツイートを保存する
        - fukurou-info - ツイート文を生成するために使う情報
- Axure Custom Vision
- Twitter API

## 環境変数一覧
アプリケーションの稼働には、それぞれのサービスの認証情報とエンドポイントが必要。 
ローカルで実行する場合、`local.settings.json`に設定しておく。
Azure Functionsで実行する場合、「構成」で設定する。
- COSMOS_ACCOUNT_URI
- COSMOS_ACCOUN_KEY
- TWITTER_CONSUMER_API_KEY
- TWITTER_CONSUMER_API_SECRET
- TWITTER_BEARER_TOKEN
- TWITTER_ACCESS_TOKEN
- TWITTER_ACCESS_TOKEN_SECRET
- CUSTOM_VISION_PREDICTION_ENDPOINT_URL
- CUSTOM_VISION_PREDICTION_KEY
