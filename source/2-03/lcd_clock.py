# -*- encoding:utf8 -*-
from akilib import AKI_GPIO_SC1602BSLB
import time
#時間待ちをするtime.sleep関数を使う為のtimeライブラリ宣言
import datetime
#日時を使う為のdatetimeライブラリ宣言

LCD = AKI_GPIO_SC1602BSLB(8,9,4,5,6,7)

LCD.LCD_Init()
LCD.DisplayON()
LCD.ClearDisplay()

#ここまでは一緒

while 1 :
#whileを使った無限ループ
    LCD.ClearDisplay()
    #毎回　画面をクリアする
    d = datetime.datetime.today()
    # datetime関数を使ってtoday()で今日の日付を取得
    print d.strftime("%Y-%m-%d %H:%M:%S")
    #strftime関数で出力フォーマットを指定
    # %Yは年, %mは月, %dは日, %Hは時間, %Mは分,　%Sは秒
    # この形式だと　2015-03-02 10:15:20 といった形でしょうか
    LCD.WritePos(0,0)
    LCD.WriteStr(str(d.strftime("%Y/%m/%d")))
    #一行目を選択。フォーマットが"%m/%d"なので 10/14
    LCD.WritePos(1,0)
    LCD.WriteStr(str(d.strftime("%H:%M:%S")))
    #二行目を選択。フォーマットが"%H:%M:%S"なので 12:35:40　といった形です
    time.sleep(0.2)
    #time.sleep()で秒単位で指定できます。また、小数点でmsを指定できます。