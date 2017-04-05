# -*- encoding:utf8 -*-
from akilib import AKI_I2C_SO1602AWYB
#akilibよりAKI_I2C_SO1602AWYBを使用することを宣言
import time
# 時間に関するライブラリの使用宣言
oled = AKI_I2C_SO1602AWYB(6)
#AKI_I2C_SO1602AWYBを使用する宣言()の中にはI2Cのポート番号を指定しています。
oled.Init_OLED()
#OLEDの初期化関数
oled.ClearDisplay()
#OLEDに表示された文字を消す際の関数
oled.WritePos(0,0)
#OLEDの文字を出力するポジション設定　(縦、横)
oled.WriteStr("Hello World.")
#OLEDに表示する文字
time.sleep(2)
#0.5秒待つ
oled.WritePos(1,3)
#OLEDの文字を出力するポジション設定　(縦、横)
oled.WriteStr("Hello Edison.")
#OLEDに表示する文字
