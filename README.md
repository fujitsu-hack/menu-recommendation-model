# 献立推薦モデル
担当者，編集者：森雅也

## 目的
- 食材画像から作れそうな料理の大まかなクラスを予測するモデルを構築する
- 予測したクラスから楽天レシピAPIを用いることで料理の詳細を返すコードを書く

## モデルの概要
- モデルはresnetを転移学習せることで構築する
- しかし出力のノードが一致しないので，一部構成を変更しfine-tuningをする
- 出力(献立クラス)は4つ
  - class1：定番の肉料理(肉類＋野菜類)
  - class2：定番の魚料理(魚類＋野菜類)
  - class3：鍋料理(肉類＋魚類＋野菜類)
  - class4：サラダ(野菜類)

- 入力画像(学習データ)は2000枚(テストデータは別で用意する)
  - originalが10枚
  - 120度回転が10枚
  - 240度回転が10枚
  - 左右反転が30枚
  - コントラスト調整が240枚
  - ガウシアンノイズが60枚
  - 拡大が70枚
  - 縮小が70枚
  - 上記500枚×クラス数 = 2000枚

## やること(予定)
1. 食材のアノテーション(データセットがなかった…)
1. モデル(resnet)の学習
1. テストする
1. APIの作成(from 画像 to 1クラス)
1. 楽天レシピAPIから献立のURLを返す

## 参考資料
### 作品に関して
- [【機械学習】Custom Visionを使用して食材の写真を送ると自動で料理を提案してくれるLINEBOTを作成してみた【画像認識】](https://qiita.com/Naru0607/items/16c42a242ddc90009a30)
- [冷蔵庫の余った食材からレシピを提案するボットをリリースしました](https://qiita.com/msh5/items/b2350bab800eddaecad3)
### 献立推薦モデルに関して
- [TensorFlow, KerasでVGG16などの学習済みモデルを利用](https://note.nkmk.me/python-tensorflow-keras-applications-pretrained-models/)
- [TensorFlow, Kerasの基本的な使い方（モデル構築・訓練・評価・予測）](https://note.nkmk.me/python-tensorflow-keras-basics/)
- [TensorFlow, Kerasで転移学習・ファインチューニング（画像分類の例）](https://note.nkmk.me/python-tensorflow-keras-transfer-learning-fine-tuning/)
- [TensorFlow, Kerasでレイヤー、モデルのtrainable属性を設定（Freeze / Unfreeze）](https://note.nkmk.me/python-tensorflow-keras-trainable-freeze-unfreeze/)
- [tf.keras.applications.ResNet50](https://www.tensorflow.org/api_docs/python/tf/keras/applications/ResNet50?authuser=0&hl=ja)
- [ResNetをFine Tuningして自分が用意した画像を学習させる](https://pchun.work/resnet%E3%82%92fine-tuning%E3%81%97%E3%81%A6%E8%87%AA%E5%88%86%E3%81%8C%E7%94%A8%E6%84%8F%E3%81%97%E3%81%9F%E7%94%BB%E5%83%8F%E3%82%92%E5%AD%A6%E7%BF%92%E3%81%95%E3%81%9B%E3%82%8B/#i-2)
- [TensorFlow 2.0のDockerコンテナをGPU+Python3+Jupyterで使う](https://qiita.com/hrappuccino/items/fe76e2ed014c16171e47#tensorflow-docker%E3%82%B3%E3%83%B3%E3%83%86%E3%83%8A%E3%81%AE%E8%B5%B7%E5%8B%95)
- [TensorFlow Docker](https://www.tensorflow.org/install/docker?hl=ja#tensorflow_docker_requirements)
- [Pythonの画像処理ライブラリPillow(PIL)の使い方](https://note.nkmk.me/python-pillow-basic/)
- [Tensorflow/modelsのdata augmentationの動きを確認する](https://blog.imind.jp/entry/2019/07/20/132143)
- [RuntimeError: JupyterLab failed to build](https://github.com/jupyterlab/jupyterlab-github/issues/97)
### APIに関して
- [APIテストフォーム](https://webservice.rakuten.co.jp/explorer/api/Recipe/CategoryList/)
