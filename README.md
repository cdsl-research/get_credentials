# get_credentials

## はじめに
KubernetesクラスタにデプロイされたElasticsearchの認証情報を取得するシンプルなツールです。

## 主な機能
プロジェクトは以下の3つの主要なPythonファイルで構成されています：
### main.py
- プログラムのエントリーポイント
- コマンドライン引数（namespace）の処理
- 結果の表示を担当
### credentials.py
- Elasticsearch認証情報の取得ロジック
- Base64でエンコードされた認証情報のデコード処理
- エラーハンドリング
### k8s_utils.py
- Kubernetes APIクライアントの初期化
- シークレットの取得処理
- Kubernetes関連のユーティリティ関数


## 事前準備
Python3のpipをインストールとKubernetes Pythonクライアントのインストールをする
bash
```
# Python3のpipをインストール
sudo apt install python3-pip

# Pythonクライアントのインストール
pip3 install kubernetes
```
このパッケージにより、PythonからKubernetes APIにアクセスできるようになります。

## 前提条件
- Python 3.6以上
- Kubernetesクラスタへのアクセス権限があること
- kubectl が設定済みであること
- ELK Stackがインストールされていること

## 実行方法
下記のようにユーザーネームとパスワードが表示されるようになります
```
# namespace を指定して実行
python3 main.py -n <namespace>

# または
python3 main.py --namespace <namespace>
```

## 実行結果
下記の画像のように表示される
![image](https://github.com/user-attachments/assets/768adbb3-bf09-494e-afd7-e51189651d32)




注意事項
取得した認証情報は適切に管理してください
クラスタ管理者権限が必要な場合があります
環境によってはプロキシ設定が必要な場合があります
