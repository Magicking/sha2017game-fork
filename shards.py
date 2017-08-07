import shards
HSePK=int
HSePr=zip
HSePu=range
HSePw=len
HSePM=None
HSePz=ValueError
HSePg=divmod
HSePY=reversed
HSePD=isinstance
HSePb=list
HSePx=tuple
HSePF=str
HSePG=set
HSePL=(HSePK)
HSePh='0123456789abcdef'
HSePt='0123456789abcdef'
def egcd(a,b):
 u,u1=1,0
 v,v1=0,1
 g,g1=a,b
 while g1:
  q=g//g1
  u,u1=u1,u-q*u1
  v,v1=v1,v-q*v1
  g,g1=g1,g-q*g1
 return(g,u,v)
def mod_inverse(k,HSePv):
 k=k%HSePv
 if k<0:
  r=egcd(HSePv,-k)[2]
 else:
  r=egcd(HSePv,k)[2]
 return(HSePv+r)%HSePv
def modular_lagrange_interpolation(x,HSePU,HSePv):
 HSePV,HSePp=HSePr(*HSePU)
 HSePC=0
 for i in HSePu(HSePw(HSePU)):
  HSePn,HSePk=1,1
  for j in HSePu(HSePw(HSePU)):
   if i==j:
    continue
   HSePn=(HSePn*(x-HSePV[j]))%HSePv
   HSePk=(HSePk*(HSePV[i]-HSePV[j]))%HSePv
  HSePl=HSePn*mod_inverse(HSePk,HSePv)
  HSePC=(HSePv+HSePC+(HSePp[i]*HSePl))%HSePv
 return HSePC
def calculate_mersenne_primes():
 HSePi=[2,3,5,7,13,17,19,31,61,89,107,127,521,607,1279]
 HSePa=[]
 for HSePI in HSePi:
  HSePv=1
  for i in HSePu(HSePI):
   HSePv*=2
  HSePv-=1
  HSePa.append(HSePv)
 return HSePa
HSePJ=(2**256+297)
HSePj=(2**320+27)
HSePR=(2**384+231)
HSePA=calculate_mersenne_primes()+[HSePJ,HSePj,HSePR]
HSePA.sort()
def get_large_enough_prime(batch):
 HSePa=HSePA
 for HSePv in HSePa:
  HSePq=[i for i in batch if i>HSePv]
  if HSePw(HSePq)==0:
   return HSePv
 return HSePM
def int_to_charset(HSePN,HSePT):
 if not HSePN>=0:
  raise HSePz('"val" must be a non-negative integer.')
 if HSePN==0:
  return HSePT[0]
 HSePQ=""
 while HSePN>0:
  HSePN,HSePX=HSePg(HSePN,HSePw(HSePT))
  HSePQ+=HSePT[HSePX]
 return ''.join(HSePY(HSePQ))
def charset_to_int(s,HSePT):
 HSePQ=0
 for HSePf in s:
  HSePQ=HSePQ*HSePw(HSePT)+HSePT.index(HSePf)
 return HSePQ
def points_to_secret_int(HSePU,prime=HSePM):
 if not HSePD(HSePU,HSePb):
  raise HSePz("Points must be in list form.")
 for HSePW in HSePU:
  if not HSePD(HSePW,HSePx)and HSePw(HSePW)==2:
   raise HSePz("Each point must be a tuple of two values.")
  if not(HSePD(HSePW[0],HSePL)and HSePD(HSePW[1],HSePL)):
   raise HSePz("Each value in the point must be an int, got %d and %d."%(HSePW[0],HSePW[1]))
 HSePV,HSePp=HSePr(*HSePU)
 if not prime:
  prime=get_large_enough_prime(HSePp)
 HSePs=modular_lagrange_interpolation(0,HSePU,prime)
 HSePE=HSePs 
 return HSePE
def share_string_to_point(share_string,HSePT):
 if '-' in HSePT:
  raise HSePz('The character "-" cannot be in the supplied charset.')
 if not HSePD(share_string,HSePF)and share_string.count('-')==1:
  raise HSePz('Share format is invalid.')
 HSePm,HSePO=share_string.split('-')
 if(HSePG(HSePm)-HSePG(HSePT))or(HSePG(HSePO)-HSePG(HSePT)):
  raise HSePz("Share has characters that aren't in the charset.")
 x=charset_to_int(HSePm,HSePT)
 y=charset_to_int(HSePO,HSePT)
 return(x,y)
def key_from_shards(shards):
 HSePU=[]
 for HSePy in shards:
  HSePU.append(share_string_to_point(HSePy,HSePt))
 HSePE=points_to_secret_int(HSePU)
 HSePc=int_to_charset(HSePE,HSePh)
 return HSePc
# Created by pyminifier (https://github.com/liftoff/pyminifier)

