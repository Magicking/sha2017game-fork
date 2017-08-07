import sys
VPMXW=False
VPMXy=sys.path
import time
import badge
VPMXy.append('/lib/SHA2017Game')
import game_common
VPMXK=game_common.determineLeague
try:
 import sparkle as callsign
except:
 import callsign
def setup():
 return VPMXW
def loop():
 VPMXp=VPMXK()
 callsign.blink(VPMXp)
 return 25*60*1000
# Created by pyminifier (https://github.com/liftoff/pyminifier)

