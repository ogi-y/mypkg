# mypkg
このリポジトリはROS2のパッケージです。srcディレクトリでgit cloneすればパッケージとして利用できます。

## 依存関係
このパッケージを利用するためには[color_msgsパッケージ](https://github.com/ogi-y/color_msgs)が必要です。

## 各ノードの説明
* talker
    * red green blueに0から255の間で乱数を生成し、color_msgsパッケージのColor型を利用してメッセージを送信します。
* listener
    * Color型から受け取ったメッセージを表示します。
* changer
    * Queryサービスからred green blueの3つの値を受け取り、カラーコードに変換して返します。
* service
    * 直前に受け取ったColor型のメッセージをそれぞれred green blueに代入し、Queryサービスを利用してその値をchangerへ渡します。

## 各launchファイルの説明
*  talk_listen.launch.py
    * talkerとlistenerを実行します。
*  rgbChange_service.launch.py
    * talkerとchangerとserviceを実行します。

## テスト環境
* Ubuntu 22.04.1 LTS

## 権利表記
* このソフトウェアパッケージは、[3条項BSDライセンス](https://opensource.org/licenses/BSD-3-Clause)の下、再頒布および使用が許可されます。
* © 2022 Yoshihiro Ogishima