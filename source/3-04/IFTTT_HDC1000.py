# -*- encoding:utf8 -*-
from akilib import AKI_I2C_HDC1000
#akilibライブラリのAKI_I2C_HDC1000を使用することを宣言
import time
#timeライブラリ
import requests
#HTTPでアクセスする際に便利なライブラリ

hdc1k = AKI_I2C_HDC1000(1)
#HDC1000をEdisonのI2C_1で使用する事を宣言
hdc1k.Config()
#HDC1000特有の初期化処理を行います。
while 1:
    #無限ループ文 終了するときはキーボードでCtrl+Cを押します。
    print "%d 'C" % hdc1k.Temperature()
    #温度を取得します。表記は℃
    print "%d %%" % hdc1k.Humidity()
    #湿度を取得します。表記は％


    event = "Edison-IFTTT"
    #IFTTTで設定したトリガー名
    secret_key = "xxxxxxxxxxxxxxxxx"
    #IFTTTのシークレットキーを入力
    str = "Temp:%d,Humi:%d%%" % (hdc1k.Temperature(),hdc1k.Humidity())
    #通知を行う文面
    URL = "http://maker.ifttt.com/trigger/%s/with/key/%s" % (event,secret_key)
    #IFTTTのURL生成（特に変更不要)
    print "Event Name :" + event
    print "Send Value :" + str
    print URL
    print requests.post(URL, json={"value1": str})
    #IFTTTに出力構文
