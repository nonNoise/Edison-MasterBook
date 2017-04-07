# -*- encoding:utf8 -*-
from akilib import AKI_GPIO_SG12864ASLB
#akilibからAKI_GPIO_SG12864ASLBライブラリの使用を宣言
from PIL import Image, ImageDraw,ImageFont
#画像描画ライブラリ PILを使用する宣言
g = AKI_GPIO_SG12864ASLB(13,12,11,10,9,8,7,6,5,4,3,2,1,0)
#EdisonとSG12864ASLBの信号の宣言
g.SetUp()
#SG12864ASLBを初期化する関数
g.Clear()
#画面をまっさらにする
g.Test()
#テスト用の画面を出力（シマシマ模様）
font = ImageFont.truetype('ipag.ttf', 12)
#文字を出力したいのでフォントデータを指定、文字サイズは12pt
g.draw.text((1, 10), u'こんにちは、Edison。', font=font, fill='#000')
#文字を出力　座標を指定してそこから文字を表示する。
g.draw.text((1, 25), u'新しい世界へようこそ', font=font, fill='#000')
#文字を出力　座標を指定してそこから文字を表示する。
g.Uplode()
#文字を画面に描画
