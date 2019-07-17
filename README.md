# 5W1HGameSite
5W1Hゲームができるサイト

## Require
* docker
* docker-compose


## Try

```
docker-compose up -d

# Open http://localhost:8000 in browser

```


# API

`base_url` は適宜変えてください。
> localで実行する場合は、`localhost:8000`

### words

#### Get random words
  | method | endopoint          |
  | :----: | ------------------ |
  |  GET   | `base_url/api/all` |
  
ランダムで全ての要素のワードを返すエンドポイント

* response body sample:
  * success `200 OK`
  ```json
  [
    {
      "id": 2,
      "word": "hogefuga"
    }
  ]
  ```

#### Get random word
  | method | endopoint               |
  | :----: | ----------------------- |
  |  GET   | `base_url/api/:element` |
  
ランダムでワードを返すエンドポイント
`:element` は、`all` `when` `where` `what` `why` `who` `how` を指定する。

* response body sample:
  * success `200 OK`
  ```json
  {
    "id": 2,
    "word": "hogefuga"
  }
  ```
