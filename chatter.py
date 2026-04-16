#code to access an API & pass it commands
import requests
#from playsound import playsound
import winsound
boyfile = open('boy.txt', 'r') 
boylines = boyfile.read().splitlines()

girlfile = open('girl.txt', 'r') 
girllines = girlfile.read().splitlines()
#print (boylines) #.len
#print (girllines)
print (len(girllines))
print (len(boylines))
poop =len(boylines) + len(girllines) #file.count
print(poop)
#for item in girlfile
range2 = range(len(girllines))
url = "https://talkmodachi.dylanpdx.io/tts"
ext = 'wav'      
pxt = 'output'
payloada1 = {'text': 'piggy camel', 'pitch': '10', 'speed': '10'}
payloada2 = {'text': 'jello world KITTIES'}
for p in range2:
    if p % 2 == 0: #changes the voices
      #print(girllines[p])
      payload2 = {'text': girllines[p], 'pitch': '10', 'speed': '10'}
    else: 
      # print(boylines[p])
       payload2 = {'text': girllines[p]}
    string = f"{pxt}{p}.{ext}" ## iterates the fiename
   # print(string)
    r = requests.get(url, auth=None, params=payload2)
    if r.status_code == 200:
        with open(string, "wb") as f:
            f.write(r.content)
        winsound.PlaySound(string, winsound.SND_FILENAME)
    else:
        print(r.status_code)

#print (r.url)
#print (r)
#print (r.raw)
#if r.status_code == 200:
#    with open("output6.wav", "wb") as f:
#        f.write(r.content)
#winsound.PlaySound('output2.wav', winsound.SND_FILENAME)
#winsound.PlaySound('output3.wav', winsound.SND_FILENAME)
#winsound.PlaySound('output4.wav', winsound.SND_FILENAME)
#winsound.PlaySound('output5.wav', winsound.SND_FILENAME)
#winsound.PlaySound('output6.wav', winsound.SND_FILENAME)