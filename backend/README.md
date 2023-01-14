# Backend

## Getting started

### 開発環境の起動/停止
backend開発用dockerコンテナ起動
```sh
cd /backend
docker compose up --build
```
別terminalでdockerコンテナ内のbashに入る
```sh
docker exec -it chankari-backend bash
```
dockerコンテナを停止
```sh
docker stop chankari-backend
```

### 依存関係のインストール
`pip install`で依存関係をインストールした場合は`requirements.txt`へ書き込み (**dockerコンテナ内で実行する**)
```sh
pip freeze > requirements.txt
```