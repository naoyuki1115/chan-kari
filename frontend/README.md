# Frontend

## Getting started

### Dockerの起動
"frontend"ディレクトリから、以下のコマンドにてDockerを起動
```
docker-compose up -d --build
```
### React開発用サーバーの立ち上げ
上記で立ち上げたDockerコンテナ内で以下のコマンドを実行
```
cd chan-kari
HOST=0.0.0.0 npm run start
```
開発用サーバーが起動したらブラウザにて、サーバーにアクセスする。
```
http://localhost:3000
```
