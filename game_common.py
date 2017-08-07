import machine
kGIVd=machine.unique_id
def determineLeague():
 return(kGIVd()[5]>>1)%6
# Created by pyminifier (https://github.com/liftoff/pyminifier)

