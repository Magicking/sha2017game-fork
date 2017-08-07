import badge
PfCKp=range
PfCKD=badge.leds_send_data
import time
PfCKU=time.sleep_ms
import binascii
PfCKx=binascii.unhexlify
import urandom
PfCKR=["000a0000","000e0000","00000a00","0a000000","0a0e0000","041e0000"]
PfCKL="00000000"
def blink3(color,delay=75):
 for i in PfCKp(3):
  PfCKD(PfCKx(color*6),24)
  PfCKU(delay)
  PfCKD(PfCKx(PfCKL*6),24)
  PfCKU(delay)
def blinksos(color):
 blink3(color)
 PfCKU(100)
 blink3(color,175)
 blink3(color)
def callsign(league):
 blinksos(PfCKR[league])
def league_color(league):
 return PfCKR[league]
def blink(league):
 callsign(league)
# Created by pyminifier (https://github.com/liftoff/pyminifier)

