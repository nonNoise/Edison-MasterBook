# -*- coding: utf-8 -*-
import datetime
#日時に関するライブラリの使用宣言
import time
# 時間に関するライブラリの使用宣言
from akilib import AKI_I2C_SO1602AWYB
#akilibよりAKI_I2C_SO1602AWYBを使用することを宣言
oled = AKI_I2C_SO1602AWYB(6)
#AKI_I2C_SO1602AWYBを使用する宣言()の中にはI2Cのポート番号を指定しています。
oled.Init_OLED()
#OLEDの初期化関数
t = 10
#文字を出力する時間を調節
oled.WritePos(0,0)
oled.WriteStr((u"Edison"),t)
#1行目に表示する文字を設定
oled.WritePos(1,0)
oled.WriteStr((u"ｷﾄﾞｳ ｼﾏｼﾀ").encode('shift_JIS'),t)
#2行目に表示する文字を設定
#（半角カタカナを記述し、shift_JISにエンコードします）
time.sleep(1)
oled.NewClearDisplay(0,t)
#1行目クリア
oled.NewClearDisplay(1,t)
#2行目クリア

while 1 :
    d = datetime.datetime.today()
    #日時データの取得
    oled.WritePos(0,0)
    oled.WriteStr((u"ﾎﾝｼﾞﾂ ﾊ").encode('shift_JIS'),t)
    #1行目に表示する文字を設定
    #（半角カタカナを記述し、shift_JISにエンコードします）
    oled.WritePos(1,2)
    oled.WriteStr(str(d.strftime("%Y/%m/%d")),t)
    #2行目を選択。フォーマットが"%Y/%m/%d"なので 2016/10/14
    time.sleep(1)
    oled.NewClearDisplay(0,t)
    #1行目クリア
    oled.NewClearDisplay(1,t)
    #2行目クリア
    d = datetime.datetime.today()
    #日時データの取得
    oled.WritePos(0,0)
    oled.WriteStr((u"ﾀﾀﾞｲﾏﾉｼﾞｶﾝ").encode('shift_JIS'),t)
    #1行目に表示する文字を設定
    #（半角カタカナを記述し、shift_JISにエンコードします）
    oled.WritePos(1,0)
    oled.WriteStr(str(d.strftime("%H:%M:%S")))
    #2行目を選択。フォーマットが"%H:%M:%S"なので 12:35:40　といった形です
    time.sleep(1)
    oled.NewClearDisplay(0,t)
    #1行目クリア
    oled.NewClearDisplay(1,t)
    #2行目クリア
