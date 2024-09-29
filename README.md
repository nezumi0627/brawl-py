# nezu_brawl

## 概要
`nezu_brawl` は Brawl Stars の公式 API にアクセスするための Python ライブラリです。

## 環境設定

### Brawl Stars API キーの取得

1. Brawl Stars の開発者ポータルにアクセスします: [Brawl Stars Developer Portal](https://developer.brawlstars.com/#/login)
2. アカウントを作成するために、必要な情報を入力します。
3. アカウント作成後、ログインします。
4. API キーを生成し、適切に保存します。このキーは API へのリクエストを行う際に必要です。

### 環境変数の設定

1. `.env` ファイルを作成し、次のように API キーを追加します:

   ```plaintext
   BRAWL_STARS_API_KEY=あなたのAPIキー
   ```