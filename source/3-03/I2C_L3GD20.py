# -*- encoding:utf8 -*-
import time
#timeライブラリ
from akilib import AKI_I2C_L3GD20
#akilibのAKI_I2C_L3GD20を使用する事を宣言
L3GD20 = AKI_I2C_L3GD20(1)
#AKI_I2C_L3GD20をI2C_1で使用する事を宣言
time.sleep(0.01)
L3GD20.WhoAmI()
L3GD20.Init()
#L3GD20特有の初期化処理を行います。
while 1:
    xdps = L3GD20.X()
    #X軸の角速度を取得
    ydps = L3GD20.Y()
    #Y軸の角速度を取得
    zdps = L3GD20.Z()
    #Z軸の角速度を取得
    print "X:%f Y:%f Z:%f" % (xdps,ydps,zdps)
    #取得した角速度を表示
    time.sleep(0.1)
    #0.1秒待つ
