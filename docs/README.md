# ドキュメント確認方法
## PlantUML 起動
ER図やシーケンス図の確認時に下記を実行

起動 (UML描画前に起動)
```sh
docker run -d --rm -p 12345:8080 --name plantuml plantuml/plantuml-server
```
`*.pu`ファイルを開き、描画
* Mac: opt + d
* Windows: alt + d

UMLの確認後にdockerコンテナを終了させる
```sh
docker stop plantuml
```