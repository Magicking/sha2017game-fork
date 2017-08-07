import sys
UhPDr=range
UhPDA=True
UhPDv=OSError
UhPDf=False
UhPDu=len
UhPDX=open
UhPLF=sys.path
import gc
UhPLC=gc.collect
import network
UhPLt=network.WLAN
UhPLa=network.STA_IF
UhPLI=network.AP_IF
import machine
UhPLm=machine.unique_id
import usocket as socket
UhPLV=socket.getaddrinfo
UhPLp=socket.socket
import badge
UhPLc=badge.nvs_set_str
UhPLo=badge.nvs_get_str
UhPLN=badge.nvs_erase_key
import ugfx
UhPLO=ugfx.BLACK
UhPLE=ugfx.clear
UhPLB=ugfx.input_attach
UhPLn=ugfx.string
UhPLe=ugfx.WHITE
UhPLT=ugfx.flush
UhPLR=ugfx.BTN_A
UhPLq=ugfx.BTN_B
UhPLk=ugfx.input_init
import appglue
UhPLQ=appglue.start_app
UhPLz=appglue.home
import time
UhPLS=time.sleep
import dialogs
UhPLg=dialogs.prompt_boolean
UhPLl=dialogs.prompt_text
import machine
UhPLm=machine.unique_id
UhPLF.append('/lib/SHA2017Game')
import game_common
UhPLy=game_common.determineLeague
import callsign
UhPDL=callsign.callsign
UhPLD=["red","fuchsia","blue","green","yellow","orange"]
def shift_fragments(i):
 for n in UhPDr(i,26):
  UhPLr=UhPLo('SHA2017Game',"fragment_%d"%(n+1))
  if UhPLr:
   UhPLc('SHA2017Game',"fragment_%d"%n,UhPLr)
  else:
   UhPLN('SHA2017Game',"fragment_%d"%n)
   return
def remove_duplicate_initial_fragment():
 UhPLA=UhPLo('SHA2017Game',"fragment_0")
 if UhPLA:
  for i in UhPDr(1,25):
   UhPLv=UhPLo('SHA2017Game',"fragment_%d"%i)
   if UhPLv and UhPLv.strip()==UhPLA.strip():
    shift_fragments(i)
    return
def get_fragments():
 UhPLf=[]
 for i in UhPDr(0,25):
  UhPLv=UhPLo('SHA2017Game',"fragment_%d"%i)
  if UhPLv:
   UhPLf.append(UhPLv.replace('\n','').replace('\r',''))
 return UhPLf
def add_fragment(newfragment):
 for i in UhPDr(0,25):
  UhPLv=UhPLo('SHA2017Game',"fragment_%d"%i)
  if UhPLv:
   if UhPLv.strip()==newfragment.strip():
    return
  else:
   UhPLc('SHA2017Game',"fragment_%d"%i,newfragment)
   return
def leaguename():
 UhPLu=UhPLy()
 return UhPLD[UhPLu]
def receiveData(UhPLX,cb,errcb):
 w=UhPLt(UhPLI)
 w.active(UhPDA)
 w.config(essid=UhPLX,channel=11)
 s=UhPLp()
 ai=UhPLV("0.0.0.0",2017)
 print("Bind address info:",ai)
 UhPLb=ai[0][-1]
 s.bind(UhPLb)
 s.listen(5)
 print('Listening at',UhPLX)
 s.settimeout(120)
 try:
  UhPLH=s.accept()
  UhPLs=UhPLH[0]
  UhPLw=UhPLH[1]
  print("Client address:",UhPLw)
  print("Client socket:",UhPLs)
  UhPLK=UhPLs
  print("Request:")
  UhPLx=UhPLK.readline()
  print(UhPLx)
  UhPLK.send('OK\r\n')
  UhPLJ=cb(UhPLx)
  UhPLK.close()
  print("Done.")
 except UhPDv:
  print("Error")
  UhPLJ=errcb()
 s.close()
 w.active(UhPDf)
 if UhPLJ:
  UhPLQ('SHA2017Game')
def gotOracleData(data):
 UhPLc('SHA2017Game','fragment_0',data)
 return UhPDA
def listenForOracle(leaguename):
 UhPLE(UhPLe)
 UhPLn(0,0,"Find the oracle!","PermanentMarker22",UhPLO)
 UhPLn(0,30,"Welcome, brave traveller of league %s. Your quest"%leaguename,"Roboto_Regular12",UhPLO)
 UhPLn(0,50,"starts once you have found the oracle. When you are","Roboto_Regular12",UhPLO)
 UhPLn(0,70,"near she will call out for you and provide further","Roboto_Regular12",UhPLO)
 UhPLn(0,90,"instructions. You have 30 seconds per attempt.","Roboto_Regular12",UhPLO)
 UhPLT()
 receiveData('OracleSeeker',gotOracleData,UhPLz)
def send_to(recv):
 UhPLE(UhPLe)
 UhPLn(0,0,"Share your fragments!","PermanentMarker22",UhPLO)
 UhPLn(0,30,"Connecting to other player...","Roboto_Regular12",UhPLO)
 UhPLT()
 n=0
 try:
  w=UhPLt(UhPLa)
  w.active(UhPDA)
  ap="Gamer %s %s"%(leaguename(),recv)
  print('Connecting to',ap)
  w.connect(ap)
  while not w.isconnected()and n<30:
   UhPLS(1)
   n=n+1
 except msg:
  print("error!",msg)
  UhPLn(0,50,"Error connecting to other player...","Roboto_Regular12",UhPLO)
  UhPLT()
  UhPLk()
  UhPLB(UhPLR,lambda pressed:UhPLQ('SHA2017Game')if pressed else 0)
  return
 if n==30:
  print('No connection after sleeping 30 seconds')
  UhPLn(0,50,"Error connecting to other player...","Roboto_Regular12",UhPLO)
  UhPLT()
  UhPLk()
  UhPLB(UhPLR,lambda pressed:UhPLQ('SHA2017Game')if pressed else 0)
  return
 UhPLn(0,50,"Sending fragments...","Roboto_Regular12",UhPLO)
 UhPLT()
 s=UhPLp()
 ai=UhPLV("192.168.4.1",2017)
 UhPLb=ai[0][-1]
 s.connect(UhPLb)
 s.send('#'.join(get_fragments()))
 s.send("\r\n")
 s.readline()
 s.close()
 w.active(UhPDf)
 print('Done sending')
 UhPLn(0,70,"Sent fragments. Press A.","Roboto_Regular12",UhPLO)
 UhPLT()
 UhPLk()
 UhPLB(UhPLR,lambda pressed:UhPLQ('SHA2017Game')if pressed else 0)
def gotFragmentData(data):
 print('Got fragment data: ',data)
 for UhPLv in data.decode().split('#'):
  add_fragment(UhPLv.replace('\n','').replace('\r',''))
 UhPLW=get_fragments()
 if UhPDu(UhPLW)>=25:
  UhPLQ('SHA2017Game')
 UhPLn(0,70,"You now own %d unique fragments, %d to go!"%(UhPDu(UhPLW),25-UhPDu(UhPLW)),"Roboto_Regular12",UhPLO)
 UhPLn(5,113,"B: Back to home                                A: Share fragments","Roboto_Regular12",UhPLO)
 UhPLT()
 UhPLk()
 UhPLB(UhPLq,lambda pressed:UhPLz()if pressed else 0)
 UhPLB(UhPLR,lambda pressed:UhPLQ('SHA2017Game')if pressed else 0)
 return UhPDf;
def receive_fragments_failed():
 UhPLn(0,70,"Failed to receive fragments. Press A.","Roboto_Regular12",UhPLO)
 UhPLT()
 UhPLk()
 UhPLB(UhPLR,lambda pressed:UhPLQ('SHA2017Game')if pressed else 0)
def receive_fragments():
 receiveData("Gamer %s %03d%03d"%(leaguename(),UhPLm()[4],UhPLm()[5]),gotFragmentData,receive_fragments_failed)
def send_or_recv(send):
 if send:
  UhPLE(UhPLe)
  UhPLl("Receiver address:",cb=send_to)
 else:
  UhPLE(UhPLe)
  UhPLn(0,0,"Share your fragments!","PermanentMarker22",UhPLO)
  UhPLn(0,30,"Tell the other player of your league your address,","Roboto_Regular12",UhPLO)
  UhPLn(0,50,"which is %03d%03d. Waiting..."%(UhPLm()[4],UhPLm()[5]),"Roboto_Regular12",UhPLO)
  UhPLT()
  receive_fragments()
def initiate_sharing():
 UhPLE(UhPLe)
 UhPLn(0,0,"Share your fragments!","PermanentMarker22",UhPLO)
 UhPLg("Do you want to send or receive?",true_text="Send",false_text="Receive",height=100,cb=send_or_recv)
def won():
 UhPLE(UhPLe)
 UhPLn(0,0,"Congratulations!","PermanentMarker22",UhPLO)
 UhPLn(0,30,"Cool! You've unlocked your league's secret. As a reward","Roboto_Regular12",UhPLO)
 UhPLn(0,50,"the signal shown by your badge LEDs will now sparkle.","Roboto_Regular12",UhPLO)
 UhPLn(0,70,"Is this the end? That is up to you! Contact raboof for","Roboto_Regular12",UhPLO)
 UhPLn(0,90,"the game code and design new challenges!","Roboto_Regular12",UhPLO)
 UhPLn(5,113,"B: Back to home                                A: Share fragments","Roboto_Regular12",UhPLO)
 UhPLT()
 UhPLk()
 UhPLB(UhPLq,lambda pressed:UhPLz()if pressed else 0)
 UhPLB(UhPLR,lambda pressed:initiate_sharing()if pressed else 0)
def main():
 UhPLC()
 UhPLu=UhPLy()
 UhPDL(UhPLu)
 remove_duplicate_initial_fragment()
 if UhPDf:
  UhPLE(UhPLe)
  UhPLn(0,0,"Welcome, early bird!","PermanentMarker22",UhPLO)
  UhPLn(0,30,"Welcome to the SHA2017Game! You are in league","Roboto_Regular12",UhPLO)
  UhPLn(0,50,"%s, as your 'callsign' shows if you soldered on your"%leaguename(),"Roboto_Regular12",UhPLO)
  UhPLn(0,70,"LEDs. The game starts when the oracle is on the field,","Roboto_Regular12",UhPLO)
  UhPLn(0,90,"keep an eye on https://twitter.com/SHA2017Game.","Roboto_Regular12",UhPLO)
  UhPLn(5,113,"B: Back to home","Roboto_Regular12",UhPLO)
  UhPLT()
  UhPLk()
  UhPLB(UhPLq,lambda pressed:UhPLz()if pressed else 0)
  return
 UhPLW=get_fragments()
 print('number of fragments so far',UhPDu(UhPLW))
 UhPLi=UhPDf
 if UhPDu(UhPLW)>=25:
  UhPLc('SHA2017Game','fragment_0',UhPLW[0].strip())
  UhPLE(UhPLe)
  try:
   import os
   os.stat('/lib/SHA2017game/sparkle.py')
   won()
  except:
   import wifi
   import urequests
   import shards
   wifi.init()
   while not wifi.sta_if.isconnected():
    UhPLS(1)
   UhPLd=[]
   for UhPLv in UhPLW:
    UhPLd.append(UhPLv.replace('\n','').replace('\r',''))
   UhPLM=shards.key_from_shards(UhPLd)
   print('Collecting shards.py with key',UhPLM)
   r=urequests.get("http://pi.bzzt.net/%s/sparkle.py"%UhPLM)
   f=UhPDX('/lib/SHA2017game/sparkle.py','w')
   f.write(r.content)
   f.close()
   won()
 elif UhPDu(UhPLW)>1:
  UhPLc('SHA2017Game','fragment_0',UhPLW[0].strip())
  UhPLE(UhPLe)
  UhPLn(0,0,"Share your fragments!","PermanentMarker22",UhPLO)
  UhPLn(0,30,"By sharing you have now brought together %d"%UhPDu(UhPLW),"Roboto_Regular12",UhPLO)
  UhPLn(0,50,"fragments of league %s. Sharing will send them all."%leaguename(),"Roboto_Regular12",UhPLO)
  UhPLn(0,70,"Unlock your league %s key with 25 fragments!"%leaguename(),"Roboto_Regular12",UhPLO)
  UhPLn(5,113,"B: Back to home                                A: Share fragments","Roboto_Regular12",UhPLO)
  UhPLT()
  UhPLk()
  UhPLB(UhPLq,lambda pressed:UhPLz()if pressed else 0)
  UhPLB(UhPLR,lambda pressed:initiate_sharing()if pressed else 0)
 elif UhPDu(UhPLW)==1:
  UhPLE(UhPLe)
  UhPLn(0,0,"Share your fragments!","PermanentMarker22",UhPLO)
  UhPLn(0,30,"The oracle gave you a fragment of a relic of the "+leaguename(),"Roboto_Regular12",UhPLO)
  UhPLn(0,50,"league. 25 such fragments must be brought together","Roboto_Regular12",UhPLO)
  UhPLn(0,70,"to unlock its potential. Find other league members to","Roboto_Regular12",UhPLO)
  UhPLn(0,90,"share fragments along with a story or Mate.","Roboto_Regular12",UhPLO)
  UhPLn(5,113,"B: Back to home                                A: Share fragments","Roboto_Regular12",UhPLO)
  UhPLT()
  UhPLk()
  UhPLB(UhPLq,lambda pressed:UhPLz()if pressed else 0)
  UhPLB(UhPLR,lambda pressed:initiate_sharing()if pressed else 0)
 elif UhPLi:
  def oracle_selection_made(value):
   UhPDL(UhPLu)
   if value:
    listenForOracle(leaguename())
   else:
    UhPLz()
  def dialog_title():
   return "SHA2017Game - you are in league "+leaguename()
  UhPLg('Are you ready to start your quest?',title=dialog_title(),true_text='Search for the oracle',false_text='Back to home screen',height=100,cb=oracle_selection_made)
 else:
  UhPLE(UhPLe)
  UhPLn(0,0,"Retrieving fragment!","PermanentMarker22",UhPLO)
  UhPLn(0,30,"Welcome player of league "+leaguename(),"Roboto_Regular12",UhPLO)
  UhPLn(0,50,"Fetching your initial fragment!","Roboto_Regular12",UhPLO)
  UhPLT()
  import wifi
  import urequests
  wifi.init()
  n=0
  while not wifi.sta_if.isconnected()and n<30:
   UhPLS(1)
   n=n+1
  if n==30:
   UhPLn(0,70,"Failed! Press A.","Roboto_Regular12",UhPLO)
   UhPLk()
   UhPLB(UhPLR,lambda pressed:UhPLQ('SHA2017Game')if pressed else 0)
   return
  UhPLj=(UhPLm()[3]+UhPLm()[4]+UhPLm()[5])%700
  r=urequests.get("http://pi.bzzt.net/oracle/%d/%d"%(UhPLu,UhPLj))
  gotOracleData(r.content)
  UhPLQ('SHA2017Game')
main()
# Created by pyminifier (https://github.com/liftoff/pyminifier)

