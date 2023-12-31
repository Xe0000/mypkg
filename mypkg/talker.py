# SPDX-FileCopyrightText: 2023 Yuta Sekino
# SPDX-License-Identifier: BSD-3-Clause

import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16MultiArray

rclpy.init()
node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成）
pub = node.create_publisher(Int16MultiArray, "countup", 10)  #パブリッシャのオブジェクト作成
n1, n2, n3 = 0, 0, 0  # カウント用変数を初期化

def cb():          #コールバック関数
    global n1, n2, n3      
    msg = Int16MultiArray()  #メッセージの「オブジェクト」
    msg.data = [n1, n2, n3]
    pub.publish(msg)        #pubの持つpublishでメッセージ送信
    n1 += 1
    n2 = 2 * n1
    n3 = n1 * n1

node.create_timer(0.5, cb)  #タイマー設定
rclpy.spin(node)
