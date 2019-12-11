from fbchat import Client,log
from fbchat.models import *
from urllib.request import urlopen
import urllib
import time
import random
import json
import datetime

def getTime():

    while True:
        try:
            res = urlopen('http://just-the-time.appspot.com/')
            result = res.read().strip()
            break
        except:
            print('get time error')
            continue

    t = result.decode('utf-8').split(" ")
    Date = list(map(int,t[0].split("-")))
    Time = list(map(int,t[1].split(":")))
    Time[0] += 8
    if(Time[0]>=24):
        Time[0] -= 24
        nextDay = datetime.datetime(Date[0], Date[1], Date[2]) + datetime.timedelta(days=1)
        day = nextDay.strftime('%Y-%m-%d').split("-")
        Date[0] = int(day[0])
        Date[1] = int(day[1])
        Date[2] = int(day[2])
    return Date+Time


def getweather():
    auth_token = "CWB-524FE466-16F7-4607-B342-93EAE3A4B2B2"
    data_id = "F-D0047-005"
    location = urllib.parse.quote("中壢區")
    res = urlopen("https://opendata.cwb.gov.tw/api/v1/rest/datastore/"+data_id+"?Authorization="+auth_token+"&format=JSON&locationName="+location)
    data = json.loads(res.read())
    #print(data['records']['locations'][0]['location'][0]['weatherElement'][6]['time'])
    return data['records']['locations'][0]['location'][0]['weatherElement'][6]['time']


username = ''
pwd = ''
client = Client(username, pwd)
lastHour = getTime()[3]
#lastHour = 13

phrase = [
'一聲問候，溫暖在心。言語雖少，真情無限!',
'美好的一天沒有你就更好了。',
'今天覺得如何呢?夢想是不是又離你更遙遠了呢?',
'當你停下來休息時，別忘了別人還在奔跑。記得絆倒他後再休息。',
'反正人生總會跌倒，不如一開始就趴在地上吧!',
'有夢最美，所以繼續睡吧!',
'不順利嗎?多照照鏡子，你就會明白原因了!',
'努力並不是沒有用，只是因為你的能力太差了，努力也就顯得微不足道。',
'今天解決不了的事，別著急了。因為明天也解決不了。',
'世上無難事，只要肯放棄!',
'比你優秀的人都在努力，那你努力有個屁用^^',
'難過的時候，不要哭！哭了也不會有人在乎你。',
'想不開的話，就去跳樓吧。反正這個世界也不差你一個人。',
'只要是石頭，到哪裡都不會發光。',
'又是個一事無成的一天吧!',
'覺得累嗎？躺上床，閉上眼睛，一天就過去囉！',
'機會是留給準備好的人! 只是，有人一出生就準備好了',
'你之所以認為金錢不能買到所有東西，別懷疑~其實只是你太窮而已',
'怕長太矮脫不了魯嗎? 別擔心，長太高也只是凸顯你的醜而已',
'別嘗試減肥了，因為重點是你的臉。',
'我知道你是個只開個頭就會想要持續下去的人，就像是只要一放假你就會想要一直放下去。',
'覺得你今天累得跟狗一樣嗎? 這可誤會大了! 狗都沒你那麼累。',
'不用太在意別人的眼光，因為根本就沒人在關心你^^',
'人生苦海，回頭是岸。不用回頭了~ 因為你的船早就沉了。',
'如果說知識是一片深沉的汪洋大海，學霸是浪濤上的衝浪者，而你是溺斃的那個人。',
'每個成功的男人，背後都有一條脊椎',
'有些人感慨:自己歲數不小了，都還沒有成熟起來。 其實你們已經成熟起來了，你們成熟起來就這樣。',
'你這麼努力，忍受那麼多寂寞和糾結，我們也沒有覺得你有多優秀。',
]

images = [
'https://imgur.dcard.tw/XDXZNao.jpg',
'https://truth.bahamut.com.tw/s01/201512/8da19c5847a5fe15762fb8fa4b012d3e.JPG',
'https://truth.bahamut.com.tw/s01/201512/d6e443440faeafe5393581f376ab4256.JPG',
'https://imgur.dcard.tw/0rdTONt.jpg',
'https://imgur.dcard.tw/ahlv8Tr.jpg',
'https://imgur.dcard.tw/Kb2elvS.jpg',
'https://truth.bahamut.com.tw/s01/201611/3e7c005513a388e0dd960351fad29371.JPG',
'https://host.easylife.tw/pics/author/ireneko/files.rei/files.rei09.jpg',
'https://truth.bahamut.com.tw/s01/201611/2279f235839c0211f7acc3aae19d1a50.JPG',
'https://img.appledaily.com.tw/images/ReNews/20150927/640_a411bc09e82cc11968e488acf2948e75.jpg',
'https://img.appledaily.com.tw/images/ReNews/20150927/640_1848418c936ee207461faf101f0d76e8.jpg',
'https://attach.setn.com/newsimages/2015/09/25/344779-PH.jpg',
'https://images.plurk.com/6dzBIzYFYly2bTvGy0zyQB.jpg',
'http://img.ltn.com.tw/Upload/liveNews/BigPic/600_phpuxb5wT.jpg',
'https://i.ytimg.com/vi/--oO-HUbbpc/maxresdefault.jpg',
'https://cdn-images-1.medium.com/max/799/1*7Ds7nPI79FWhhd4dPk_dLQ.png',
'http://i.imgur.com/OElrPtB.jpg',
'http://blog.eztable.com/wp-content/uploads/2016/06/LINE_P20160622_085939224.jpg',
'https://66.media.tumblr.com/93fe4cd98ba6d4af58117707673debe6/tumblr_inline_o70ey6QaSa1t6ecng_500.jpg',
'https://c1.staticflickr.com/1/727/31804750080_61686e5418_k.jpg',
'https://truth.bahamut.com.tw/s01/201703/ea41cc8555541bb26dbde239a28b70bf.JPG',
'https://blog.zerozero.com.tw/wp-content/uploads/2017/06/event-5.jpg',
'https://img.eservice-hk.net/upload/2018/10/11/004344_6f32e3a4faeb27e64d275ffeb7948f97.png',
'https://cdntwrunning.biji.co/808_995cf012011825ff19258e814fc7e03531fefc0e570cb3860f2a6d4b38c6490d.JPG',
'https://img.eservice-hk.net/upload/2018/02/15/194224_a96ca37f61d36882f7f8702c0d491ee5.png',
'https://cc.tvbs.com.tw/img/upload/2016/20160110/11951325_976330585764619_8102093614571396851_n.jpg',
'https://c.share.photo.xuite.net/suin1023/1c0d5f4/5114615/1106379005_l.jpg',
'https://truth.bahamut.com.tw/s01/201509/bb85e38c9594b5cdb2eb820fa5ac4892.JPG',
'https://truth.bahamut.com.tw/s01/201808/93e41e41fe9558e67ba680a6be78cbb9.JPG',
'https://truth.bahamut.com.tw/s01/201808/58bd652e3f7bede8980e6327a80962c6.JPG',
'https://www.mrplayer.tw/photos/shares/fun_201711022/5a0041baa6a13.jpg',
'http://image.knowing.asia/9e7d7bc6-ef4e-4d40-bd7a-6cdb80f6ff6f/f891af218ec285e818a906604294f38e.png',
'https://stickershop.line-scdn.net/stickershop/v1/product/3039215/LINEStorePC/main@2x.png',
'http://2.bp.blogspot.com/-GmCImYSOu1c/VO6qlBh4QiI/AAAAAAAAJgc/YxPGR3q6PVc/s1600/o0515044113227523992.jpg',
'http://i.imgur.com/pTQX5oM.jpg',
'http://blog-imgs-65.fc2.com/d/g/d/dgdg875/anime_wallpaper_Kantai_Collection_shigure_Roichi-116217.jpeg'
]

target = [
#i100003927872696, #阿里山
#100001903972688, #01#
100003213613762, #148
100003209663210, #家好
#100004608154866, #子翔
#100004125039254, #10
100002918768240  #10同學
]

#target=[100000324823811]



while True:
    #if not log in
    while True:
        try:
            if(client.isLoggedIn() == False):
                while True:
                    try:
                        client = Client(username,pwd)
                        break
                    except:
                        print("facebook login error")
                        continue
            break
        except:
            print("check login error")
            continue

    nowTime = getTime()
    nowHour = nowTime[3]
    print(nowTime)

    #整點
    if(lastHour != nowHour):
        #update new hour
        lastHour = nowHour
        #寧靜時段
        if((nowHour >= 7 and nowHour <= 23) or nowHour == 0):

            weathers = getweather()

            #make a string of time use to match the weacher prediction
            timestr = [str(nowTime[0]),'','','','','']
            matchtime3HR = ['00','00','00','03','03','03','06','06','06','09','09','09','12','12','12','15','15','15','18','18','18','21','21','21']

            for i in range(1,6):
                if(nowTime[i]<10):
                    timestr[i] = '0'+ str(nowTime[i])
                else:
                    timestr[i] = str(nowTime[i])

            startTime = timestr[0] +"-" +timestr[1] + "-" + timestr[2] + " " + matchtime3HR[nowTime[3]] + ":00:00"



            for w in weathers:
                if w['startTime'] == startTime:
                    endTime = w['endTime']
                    current_weather = w['elementValue'][0]['value']

            weatherStr = "桃園市中壢區從"+startTime+"到"+endTime+"的天氣概況是:" + current_weather

            if(nowHour >= 6 and nowHour <= 11):
                greetStr = "早安，您好！"
            elif(nowHour >= 12 and nowHour <= 18 ):
                greetStr = "午安，您好！"
            elif(nowHour >=19 and nowHour <= 24):
                greetStr = "晚安，您好！"
            elif(nowHour >=0 and nowHour <= 5):
                greetStr = "嗨嗨！時間不早囉～"

            timeStr = "現在時間是"+str(nowHour)+"點整！"
            lastStr = '我是何宜融的邊緣人關懷機器人，希望收到這封訊息的你，能讓這份溫暖繼續流傳在人間!'

            hintStr=""

            if(nowHour == 0):
                hintStr="提醒您，清晨0點至上午7點為安寧時段，這段時間內看不到我哦！"

            for i in range(len(target)):
                while True:
                    try:
                        rand_image = random.randint(0,len(images)-1)
                        rand_phrase = random.randint(0,len(phrase)-1)

                        sentence1 = greetStr + timeStr + phrase[rand_phrase]
                        sentence2 = weatherStr
                        sentence3 = lastStr + hintStr

                        client.send(Message(text=sentence1), thread_id=target[i], thread_type=ThreadType.USER)
                        client.send(Message(text=sentence2), thread_id=target[i], thread_type=ThreadType.USER)
                        client.send(Message(text=sentence3), thread_id=target[i], thread_type=ThreadType.USER)
                        #client.sendRemoteImage(images[rand_image], thread_id=target[i], thread_type=ThreadType.USER)

                        print("send to "+str(target[i]))
                        time.sleep(1)
                        break
                    except:
                        print("sent messages error!")
                        continue

    time.sleep(1)


