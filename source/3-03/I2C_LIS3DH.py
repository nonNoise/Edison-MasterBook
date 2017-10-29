# -*- encoding:utf8 -*-
import time
#timeライブラリ
from akilib import AKI_I2C_LIS3DH
#akilibのAKI_I2C_LIS3DHを使用する事を宣言

LIS3DH = AKI_I2C_LIS3DH(1)
#AKI_I2C_LIS3DをI2C_1で使用する事を宣言
time.sleep(0.01)
LIS3DH.WhoAmI()
LIS3DH.Init()
#LIS3D特有の初期化処理を行います。
while 1:
    xg = LIS3DH.X()
    #X軸の加速度を取得
    yg = LIS3DH.Y()
    #Y軸の加速度を取得
    zg = LIS3DH.Z()
    #Z軸の加速度を取得
    print "X:%f Y:%f Z:%f" % (xg,yg,zg)
    #取得した加速度を表示
    time.sleep(0.1)
    #0.1秒待つ
