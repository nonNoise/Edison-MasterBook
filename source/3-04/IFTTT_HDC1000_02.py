# -*- encoding:utf8 -*-
from akilib import AKI_I2C_HDC1000
#akilibライブラリのAKI_I2C_HDC1000を使用することを宣言
import time
#timeライブラリ
import requests
#URLでアクセスする際に便利なライブラリ

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

    oldTemp = int(hdc1k.Temperature())
    oldHumi = int(hdc1k.Humidity())
    time.sleep(2)
    nowTemp = int(hdc1k.Temperature())
    nowHumi = int(hdc1k.Humidity())
    #2秒間ずれたデータを取得
    if( (nowTemp!=oldTemp) or (nowHumi !=oldHumi)):
        #2秒間の間で変化があったかどうか比較　変化があった場合以下を実行
        event = "Edison-IFTTT"
        secret_key = "d_h2herFLWgqjiiHEWAwoe"
        str = "Temp:%d,Humi:%d%%" % (hdc1k.Temperature(),hdc1k.Humidity())
        URL = "http://maker.ifttt.com/trigger/%s/with/key/%s" % (event,secret_key)
        #IFTTTに通知用の設定構文
        print "Event Name :" + event
        print "Send Value :" + str
        print URL
        print requests.post(URL, json={"value1": str})
        #IFTTTに出力構文
        time.sleep(10)
        #10秒待つ
