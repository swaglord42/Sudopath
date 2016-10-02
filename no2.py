import webbrowser
dweetIO = "https://dweet.io/dweet/for/"
myName = "sudopaths"
myKey = "some_shit"

rawlat=raw_input("enter latitude")
print rawlat
lat=rawlat[0:2]+rawlat[3:9]

if ((rawlat[9]=="N")|(rawlat[9]=="n")):
	latdir=str("1")
elif ((rawlat[9]=="S")|(rawlat[9]=="s")):
        latdir=str("0")

rawlong=raw_input("enter longitude")
print rawlong
long=rawlong[0:3]+rawlong[4:10]

if ((rawlong[10]=="E")|(rawlong[10]=="e")):
        longdir=str("1")
elif ((rawlong[10]=="W")|(rawlong[10]=="w")):
        longdir=str("0")

traffic=str("1") #set for simplicity
time=str("2040") #hhmm=8:40pm
speed=str("010")  #kmph
speeddir=str("180") #bearing 180deg
sos=str("1") #simulation set
emergency=str("1") #ambulance prescence



temp="aa"+lat[0:8]+latdir+long[0:9]+longdir+traffic+time+speed+speeddir+sos+emergency+"zz"
print temp
rqsString = dweetIO+myName+'?'+myKey+'='+str(temp)
webbrowser.open(rqsString)

