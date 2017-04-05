# -*- encoding:utf8 -*-
from akilib import AKI_I2C_HDC1000
#akilibライブラリのAKI_I2C_HDC1000を使用することを宣言
from akilib import AKI_I2C_LPS25H
#akilibのAKI_I2C_LPS25Hを使用する事を宣言
from akilib import AKI_I2C_S11059
#akilibのAKI_I2C_S11059を使用する事を宣言

import time
# 時間に関するライブラリの使用宣言
import datetime
#日時に関するライブラリの使用宣言

hdc1k = AKI_I2C_HDC1000(1)
hdc1k.Config()
#HDC1000の初期化
LPS25H = AKI_I2C_LPS25H(1)
LPS25H.Init()
#LPS25Hの初期化
S11059 = AKI_I2C_S11059(1)
S11059.Init()
#S11059の初期化

while 1:
    print "%d 'C" % hdc1k.Temperature()
    #温度を取得します。表記は℃
    print u"%d %%" % hdc1k.Humidity()
    #湿度を取得します。表記は％
    print "P:%d hPa" % LPS25H.Press()
    #気圧データを取得します。単位はhPa(ヘクトパスカル)
    print "T:%d 'C'" % LPS25H.Temp()
    #温度データを取得します。単位は℃
    print "RED = 0x%02X" % S11059.RED()
    #赤色の光の強さを測定します
    print "GREEN = 0x%02X" % S11059.GREEN()
    #緑色の光の強さを測定します
    print "BLUE = 0x%02X" % S11059.BLUE()
    #青色の光の強さを測定します
    print "IR = 0x%02X" % S11059.IR()
    #赤外線の光の強さを測定します
    print "------------"
    time.sleep(1)
