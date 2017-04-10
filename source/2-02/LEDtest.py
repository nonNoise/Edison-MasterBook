# -*- encoding:utf8 -*-
import mraa
# EdisonのIO周りを扱うmraaライブラリの使用を宣言
import time
# 時間に関するライブラリの使用宣言
print "LED Test!"
# コマンドラインに文字を表示
x = mraa.Gpio(13)
# xという変数でGPIO13番を扱うことが出来る
x.dir(mraa.DIR_OUT)
# xのdir関数でGPIOを出力モードにする
x.write(1)
# x(GPIO13番の事)に１を書き込み、Hiレベルにする
time.sleep(1)
# time.sleep関数で、1秒待つ※ここで0.1とすると100ms待つ事が出来る
x.write(0)
# x(GPIO13番の事)に0を書き込み、Lowレベルにする
time.sleep(1)
# time.sleep関数で、1秒待つ
