# -*- encoding:utf8 -*-
import mraa
import time

print "LED Test !!!"
x = mraa.Gpio(13)
x.dir(mraa.DIR_OUT)
#ここまでは一緒

for  i in range(20):
# forループ文です。iにrange文で1〜20回を指定する
    x.write(1)
    # x(GPIO13番の事)に１を書き込み、Hiレベルにする
    time.sleep(1)
    # time.sleep関数で、1秒待つ※ここで0.1とすると100ms待つ事が出来る
    x.write(0)
    # x(GPIO13番の事)に0を書き込み、Lowレベルにする
    time.sleep(1)
    # time.sleep関数で、1秒待つ
