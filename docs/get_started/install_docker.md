# Dockerインストール
Mac/Windowsなどそれぞれの実行環境に合わせて環境構築するのは面倒なのでDockerを用いた環境を構築する。  
(開発環境用と本番環境用の2つのコンテナイメージを作成する)

## Mac
[Docker公式サイト](https://docs.docker.jp/docker-for-mac/install.html#mac-system-requirementsよりDocker) の説明に従ってDesktopをインストール  

- 正常にインストールされたことをTerminalで確認
  
  バージョン確認 (バージョンは人それぞれ)
  ```sh
  $ docker --version
  Docker version 20.10.17-rd, build c2e4e01
  ```
  サンプルのDockerイメージからコンテナ起動
  ```sh
  $ docker run hello-world
  Unable to find image 'hello-world:latest' locally
  latest: Pulling from library/hello-world
  7050e35b49f5: Pull complete 
  Digest: sha256:faa03e786c97f07ef34423fccceeec2398ec8a5759259f94d99078f264e9d7af
  Status: Downloaded newer image for hello-world:latest  
  Hello from Docker!
  This message shows that your installation appears to be working correctly.
  ~~
  ```

## Windows
### WSL2 インストール
WindowsでDockerを使用するためにはLinux環境が必要なので、[Microsoftのページ](https://learn.microsoft.com/ja-jp/windows/wsl/install)に従い、WSL2を有効化しUbuntuをインストールします。

- Powershellを管理者モードで開く(右クリックで選択)  
  ![](https://chigusa-web.com/wp-content/uploads/2021/12/2021-12-04_14h02_17.png)
- Ubuntu 20.04 LTS をインストール (念のためWSLのバージョンを2にする）
  ```powershell
  wsl --set-default-version 2
  wsl --install -d Ubuntu-20.04
  ```
- PCを再起動
- [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=ja-jp&gl=jp)をインストール
- Terminalを起動し、▼からUbuntuを選択
  ![](https://www.kagoya.jp/howto/wp-content/uploads/202203a_8-1024x562.png)
- DNSの設定
  
  Terminalで下記を実行
  ```sh
  sudo code /etc/wsl.conf
  ```
  VSCodeが開くので、下記を追記して保存(ctrl+s)
  ```
  [network]
  generateResolvConf = false
  ```
  Terminalで下記を実行
  ```sh
  sudo rm /etc/resolv.conf
  sudo sh -c "echo 'nameserver 8.8.8.8' > /etc/resolv.conf"
  sudo chattr +i /etc/resolv.conf
  ```
- Ubuntuのパッケージを更新
  ```sh
  sudo apt update
  sudo apt upgrade
  ```
- WSL2のセットアップは完了。**以後、WSL2環境でアプリケーションは実行します。**  
  GitHubのcloneもWSL上で実施してくだささい。

### Dockerインストール
[Docker公式サイト](https://docs.docker.jp/docker-for-windows/install-windows-home.html#windows-10-home-docker-desktop) の説明に従ってDesktopをインストール  

- 正常にインストールされたことをWindows TerminalからUbuntuを選んで確認
  
  バージョン確認 (バージョンは人それぞれ)
  ```sh
  $ docker --version
  Docker version 20.10.17-rd, build c2e4e01
  ```
  サンプルのDockerイメージからコンテナ起動
  ```sh
  $ docker run hello-world
  Unable to find image 'hello-world:latest' locally
  latest: Pulling from library/hello-world
  7050e35b49f5: Pull complete 
  Digest: sha256:faa03e786c97f07ef34423fccceeec2398ec8a5759259f94d99078f264e9d7af
  Status: Downloaded newer image for hello-world:latest  
  Hello from Docker!
  This message shows that your installation appears to be working correctly.
  ~~
  ```
