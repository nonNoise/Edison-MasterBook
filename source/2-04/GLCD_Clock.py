# -*- encoding:utf8 -*-
from akilib import AKI_GPIO_SG12864ASLB
#akilibからAKI_GPIO_SG12864ASLBライブラリの使用を宣言
from PIL import Image, ImageDraw,ImageFont
#画像描画ライブラリ PILを使用する宣言
import datetime
#日付や日時を出力するライブラリ

g = AKI_GPIO_SG12864ASLB(13,12,11,10,9,8,7,6,5,4,3,2,1,0)
g.SetUp()
g.Clear()
g.Test()
font = ImageFont.truetype('ipag.ttf', 12)
g.draw.text((1, 10), u'こんにちは、Edison。', font=font, fill='#000')
g.draw.text((1, 25), u'新しい世界へようこそ', font=font, fill='#000')
g.Uplode()
g.Clear()

#ここまでは同じ

while 1:
#while文による無限ループ（終了するときはキーボードのCtrl-Cを押して止めます）
    d = datetime.datetime.today()
    #datatimeライブラリを使って今日の日時を取得します。
    font = ImageFont.truetype('ipag.ttf', 12)
    #ipagフォントを設定します。文字の大きさは12px
    g.draw.text((1, 5),u'%s月%s日' % (d.month, d.day) , font=font, fill='#000')
    #文字を書き出します。　(1, 5)は座標です。　その後テキストを指定し、フォントと色を受け渡します。
    font = ImageFont.truetype('ipag.ttf', 20)
    #ipagフォントを設定します。文字の大きさは12px
    g.draw.text((1, 25),u'%s時%s分%s秒' % (d.hour, d.minute, d.second,), font=font, fill='#000')
    #同じく文字を書き出します。　日付の時の下に時間を表示します。
    g.Uplode()
    #バッファに書き込まれた画像を実際にグラフィック液晶に描画します。
