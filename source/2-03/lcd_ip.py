# -*- encoding:utf8 -*-
from akilib import AKI_GPIO_SC1602BSLB

LCD = AKI_GPIO_SC1602BSLB(8,9,4,5,6,7)
LCD.LCD_Init()
LCD.DisplayON()
LCD.ClearDisplay()
#ここまでは同じ

import ipget
#ipgetライブラリを使用する事を宣言
p = ipget.ipget()
#ipgetライブラリのipgetを使用する(Python特有の文化)
print p.ipaddr("wlan0")
# wlan0で登録されているipアドレスを表示
ip = p.ipaddr("wlan0")
# wlan0のipアドレスを一旦ip変数に保存
LCD.WritePos(1,0)
LCD.WriteStr(ip)
#LCDにipアドレスを渡す。すると例えば192.168.1.0といった形で表示されます。
