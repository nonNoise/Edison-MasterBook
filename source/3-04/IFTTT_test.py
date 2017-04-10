# -*- encoding:utf8 -*-
import requests
#HTTPでアクセスする際に便利なライブラリ

event = "Edison-IFTTT"
#IFTTTで設定したトリガー名
secret_key = "dn4NBcXkBOzW3rZ8MfJ-Z0"
#IFTTTのシークレットキーを入力
str = "Hello IFTTT" 
#通知を行う文面
URL = "http://maker.ifttt.com/trigger/%s/with/key/%s" % (event,secret_key)
#IFTTTのURL生成（特に変更不要)
print "Event Name :" + event
print "Send Value :" + str
print URL
print requests.post(URL, json={"value1": str})
