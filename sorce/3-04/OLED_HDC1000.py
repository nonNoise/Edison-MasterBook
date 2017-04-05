# -*- encoding:utf8 -*-
from akilib import AKI_I2C_HDC1000
#akilibライブラリのAKI_I2C_HDC1000を使用することを宣言
from akilib import AKI_I2C_SO1602AWYB
#akilibよりAKI_I2C_SO1602AWYBを使用することを宣言
import time
# 時間に関するライブラリの使用宣言
import datetime
#日時に関するライブラリの使用宣言

hdc1k = AKI_I2C_HDC1000(1)
#HDC1000をEdisonのI2C_1で使用する事を宣言
hdc1k.Config()
#HDC1000特有の初期化処理を行います。
oled = AKI_I2C_SO1602AWYB(1)
#AKI_I2C_SO1602AWYBを使用する宣言()の中にはI2Cのポート番号を指定しています。
oled.Init_OLED()
#OLEDの初期化関数
oled.ClearDisplay()
#OLEDに表示された文字を消す際の関数


f = open('out.csv', 'w')
#データ出力用CSVファイルを作成
f.write("Day,Date,Temp,Humi\n")
#CSVの１行めをファイルに書き込み
while 1:
    #無限ループ文 終了するときはキーボードでCtrl+Cを押します。
    print "%d 'C" % hdc1k.Temperature()
    #温度を取得します。表記は℃
    print u"%d %%" % hdc1k.Humidity()
    #湿度を取得します。表記は％
    time.sleep(10)
    #1秒待ちます。
    d = datetime.datetime.today()
    #日時データの取得
    day = str(d.strftime("%Y/%m/%d"))
    date = str(d.strftime("%H:%M:%S"))
    #日にちと時間に展開
    S = "%s,%s,%d,%d\n" % (day,date,hdc1k.Temperature(),hdc1k.Humidity())
    #CSVファイルに書き込むフォーマット作成
    f.write(S)
    #CSVファイルに書き込み
    print "Temp:%d'C" % (hdc1k.Temperature())
    print "Humi:%d %%" % (hdc1k.Humidity())
    oled.WritePos(0,0)
    #OLEDの文字を出力するポジション設定　(縦、横)
    oled.WriteStr("Temp:%d'C" % (hdc1k.Temperature()),5)
    #OLEDに表示する文字
    oled.WritePos(1,0)
    #OLEDの文字を出力するポジション設定　(縦、横)
    oled.WriteStr("Humi:%d%%" % (hdc1k.Humidity()),5)
    #OLEDに表示する文字
    time.sleep(10)
    oled.NewClearDisplay(0,5)
    oled.NewClearDisplay(1,5)
    #OLEDの表示をクリア
