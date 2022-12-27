import os
import shutil
import urllib.request
from urllib.request import urlopen, Request


##- 예비용 구문 
#up = "PASTE URL HERE"
#sneak = urlopen(Request(up, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'})).info()
#print(sneak)


##- 재생 이후의 리퀘스트를 찾아낸 다음 파트를 찾아 분리시켜야 한다.
s = "PASTE URL PART 1"
se = "PASTE URL PART 2"
#- 다 다르지만 니코동을 예로 들자면 다음과 같은 형태를 가진다. 찾아내는 방법은 여기까지 왔다면 그걸 모를리가
# https://pf051d5ba7e.dmc.nico/hlsvod/ht2_nicovideo/nicovideo-sm22942402_06d690c8564bde16f5d726dfb2492aa89fc0f9d76312d21314113aec552b6b0e/2/ts/10.ts?ht2_nicovideo=6-MDeU6TWKWt_1638075869351.w4dar147qo_r39nl6_w6l2re7vzujd
#s = "https://pf051d5ba7e.dmc.nico/hlsvod/ht2_nicovideo/nicovideo-sm22942402_06d690c8564bde16f5d726dfb2492aa89fc0f9d76312d21314113aec552b6b0e/2/ts/"
#se = ".ts?ht2_nicovideo=6-MDeU6TWKWt_1638075869351.w4dar147qo_r39nl6_w6l2re7vzujd"


e = "Incoming"
try:
    shutil.rmtree(e)#cleanup
except:
    print("exception : 굴러 이놈아")
os.makedirs(e)
os.chdir(e)
print ("- all green")


np = 10000 #뜰때까지 대충 처리
mpath = open("ABP.mp4",'ab')
for i in range(1, np):    
    try:
        px = urllib.request.urlopen(s+str(i)+se)
        
    except Exception as h:
        print("err : seq - %d" %i)
        break
    print("segment %d" %i)
    mpath.write(px.read())
mpath.close()
print(" - 완료")
