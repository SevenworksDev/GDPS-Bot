from proxpy import request, dlprox
import threading, time

dlprox("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all").get()
r = request()

print("GDPS Like/Dislike Bot - By: Sevenworks")
print("Made using my wonderful ProxPy library! :)")
print("____________________________________________")

serverurl = input("Server URL: ")
lvl = input("Level ID: ")
likes = input("0 (Dislike) or 1 (Like): ")

def botter():
  r.load()
  data = {
    "secret": "Wmfd2893gb7",
    "itemID": lvl,
    "type": 1,
    "like": likes
  }
  req = r.post(serverurl+"/likeGJItem211.php", data=data, headers={"User-Agent":""}, proxyInfo=True)
  if req:
    print("Success")
  else:
    print("Proxy Failed")

while True:
  try:
    t=threading.Thread(target=botter)
    t.start()
  except:
    print("Crashed, restarted process.")
