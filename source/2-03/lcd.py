# -*- encoding:utf8 -*-
from akilib import AKI_GPIO_SC1602BSLB
#ライブラリのインポート
LCD = AKI_GPIO_SC1602BSLB(8,9,4,5,6,7)
#SC1602BSLBを使用するよと宣言します。カッコの中はピンの指定です。
LCD.LCD_Init()
#LCDを初期化します。
LCD.DisplayON()
#LCDを表示状態にします。
LCD.ClearDisplay()
#LCDの表示をクリアします。
LCD.WritePos(0,0)
#０行目の０番地にカーソルを合わせます。
LCD.WriteStr("Hello Edison!")
#合わせたカーソルから文字を表示します。
LCD.WritePos(1,2)
#1行目の2番地にカーソルを合わせます。
LCD.WriteStr("Hello World!")
#合わせたカーソルから文字を表示します。
