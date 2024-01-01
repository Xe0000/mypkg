# ros 2のマイパッケージ
* このリポジトリを使うにはros2のインストールが必要です
![test](https://github.com/Xe0000/mypkg/actions/workflows/test.yml/badge.svg)
## 概要
* このパッケージは、ROS 2を使用して、特定のトピック（countup）を介してメッセージを送受信するtalkerとlistenerという2つのノードを提供。ROS 2の基本的なパブリッシャとサブスクライバの概念を学ぶことができる。

## 説明
### talker.py
* 数字をカウントして(`/countup`)を通じて送信
    * メッセージの型は１６ビット符号付き整数
    * n,2n,n^2の順で送信
### listener.py
* (`/countup`)からメッセージをもらって表示
## トピックの説明
### countup
* 16ビットの符号付き整数をカウントアップする

## インストール方法と準備
* ディレクトリを移動
```bash
cd ~/ros2_ws/src
```
* このリポジトリをクローン
```bash
git clone git@github.com:Xe0000/mypkg.git
```
* ワークスペースに移動
```bash
cd ~/ros2_ws
```
* ワークスペースをビルド
```bash
colcon build
```
* ビルドされたパッケージをソース
```bash
source ~/.bash
```

## 実行方法
### 実行方法１
* ros2 launchでの実行
```bash
ros2 launch mypkg talk_listen.launch.py
```
* 実行結果
```bash
[INFO] [launch]: All log files can be found below /home/yuta1075/.ros/log/2023-12-30-22-32-30-396122-LAPTOP-RCB6ATE5-12494
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [12496]
[INFO] [listener-2]: process started with pid [12498]
[listener-2] [INFO] [1703943151.325279802] [listener]: Listen : 0,0,0
[listener-2] [INFO] [1703943151.829179103] [listener]: Listen : 1,2,1
[listener-2] [INFO] [1703943152.299199943] [listener]: Listen : 2,4,4
[listener-2] [INFO] [1703943152.809494103] [listener]: Listen : 3,6,9
[listener-2] [INFO] [1703943153.330667045] [listener]: Listen : 4,8,16
[listener-2] [INFO] [1703943153.828359144] [listener]: Listen : 5,10,25
[listener-2] [INFO] [1703943154.328948855] [listener]: Listen : 6,12,36
[listener-2] [INFO] [1703943154.800346069] [listener]: Listen : 7,14,49
[listener-2] [INFO] [1703943155.295333804] [listener]: Listen : 8,16,64
[listener-2] [INFO] [1703943155.831788851] [listener]: Listen : 9,18,81
[listener-2] [INFO] [1703943156.328677685] [listener]: Listen : 10,20,100
```
* 終了は`Ctrl＋C`

### 実行方法２
* ros2 runでの実行
* 以下を端末を２つ使い実行
```bash
端末1$ ros2 run mypkg talker
端末2$ ros2 run mypkg listener
```
* 実行結果
```bash
[INFO] [1703981199.132193643] [listener]: Listen : 0,0,0
[INFO] [1703981199.616718103] [listener]: Listen : 1,2,1
[INFO] [1703981200.141864033] [listener]: Listen : 2,4,4
[INFO] [1703981200.634339358] [listener]: Listen : 3,6,9
[INFO] [1703981201.118360392] [listener]: Listen : 4,8,16
[INFO] [1703981201.634679984] [listener]: Listen : 5,10,25
[INFO] [1703981202.108209742] [listener]: Listen : 6,12,36
[INFO] [1703981202.614653446] [listener]: Listen : 7,14,49
```
* 終了は`Ctrl＋C`

## 必要なソフトウェア
* ROS 2
* Python
    * テスト済み:3.7~3.10
## テスト環境
* Ubuntu22.04
* ROS2 foxy

## 権利関係
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードは，大部分を下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    * [https://ryuichiueda/my_slides robosys_2022/lesson8.html#/](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson8.html#/)
    * [https://ryuichiueda/my_slides robosys_2022/lesson9.html#/](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson9.html#/)
    * [https://ryuichiueda/my_slides robosys_2022/lesson10.html#/](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson10.html#/)
* © 2023 Yuta Sekino
