#made by nk.recieve data from cloud

from RPLCD import CharLCD
import time

lcd = CharLCD(pin_rs=26, pin_e=24, pins_data=[22, 18, 16, 12])

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json

def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


url = ("https://dweet.io/get/latest/dweet/for/sudopaths")

newstr=str(get_jsonparsed_data(url))
def find_str(s, str):
    index = 0

    if str in s:
        c = str[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(str)] == str:
                    return index

            index += 1

    return -1
sh=find_str(newstr,"shit")
loc=sh+9
last=newstr[loc:loc+36]
print(last)
#use variable last as ur input sequence


#made by sk. analytics of the data from cloud
signal_str=last
start=str(signal_str[0:2]);
end=str(signal_str[34:36]);
if ((start=="aa")&(end=="zz")):
    lat_deci=float(signal_str[2:4]);
    lat_poin=float(signal_str[4:10]);
    lat_dir=float(signal_str[10]);
    long_deci=float(signal_str[11:14]);
    long_poin=float(signal_str[14:20]);
    long_dir=float(signal_str[20]);
    traffic=float(signal_str[21]);
    time_hh=float(signal_str[22:24]);
    time_mm=float(signal_str[24:26]);
    velocity=float(signal_str[26:29]);
    bearing=float(signal_str[29:32]);
    sos_signal=float(signal_str[32]);
    emergency=float(signal_str[33]);
                
lat=(lat_deci)+(lat_poin/1000000);
lon=(long_deci)+(long_poin/1000000);
if lat_dir==0:
    lat=lat*(-1);
if long_dir==0:
    lon=lon*(-1);

if traffic==1:


    lcd.clear();
    lcd.write_string(u'Traffic detected at Latitude=');
    lcd.write_string(str(lat));
    lcd.write_string(u'  Longitude=');
    lcd.write_string(str(lon));
    time.sleep(3);
    lcd.clear();
    lcd.write_string(u'Rerouting.');
    time.sleep(1);
    lcd.clear();
    lcd.write_string(u'Rerouting..');
    time.sleep(1);
    
    lcd.clear();
    lcd.write_string(u'Rerouting...');
    time.sleep(1);
    
    
    
    #jerrin_scodetake lat and lon and find alternate route
    lcd.clear();
    lcd.write_string(u'Reroute Successful!');
    time.sleep(4);
time1=time_hh+(time_mm/100);
print time1
my_bear=input("enter bearing")
lcd.clear();
lcd.write_string(u'Getting current     bearing+');
time.sleep(1);
lcd.clear();
lcd.write_string(u'Getting current     bearingX');
time.sleep(1);
lcd.clear();
lcd.write_string(u'Getting current     bearing+');
time.sleep(1);
lcd.clear();
lcd.write_string(u'Getting current     bearingX');
time.sleep(1);
lcd.clear();
lcd.write_string(u'Getting current     bearing+');
time.sleep(1);
lcd.clear();
lcd.write_string(u'Getting current     bearingX');
time.sleep(1);
lcd.clear();
lcd.write_string(u'current bearing=');
lcd.write_string(str(my_bear));
time.sleep(4);
if ((time1>18)&(time1<23.59))|((time1>0)&(time1<5)):
      if abs(my_bear-bearing)>=170:
          lcd.clear();
          lcd.write_string(u'There\'s a vehicle coming in the oposite direction');
          time.sleep(2);
          lcd.clear();
          lcd.write_string(u'Please Dim the lights');
          time.sleep(2);
          lcd.clear();
          lcd.write_string(u'There\'s a vehicle coming in the oposite direction');
          time.sleep(2);
          lcd.clear();
          lcd.write_string(u'Please Dim the lights');
          time.sleep(2);
          
          print "There's a vehicle coming opposite....Please dim lights";
      lcd.clear();
      lcd.write_string(u'Its night time pls drive carefully');
      
      print "Its night time pls drive carefully";

check=0;
if sos_signal==1:
    lcd.clear();
    lcd.write_string(u'Detecting SOS Signal+');
    time.sleep(1);
    lcd.clear();
    lcd.write_string(u'Detecting SOS SignalX');
    time.sleep(1);
    lcd.clear();
    lcd.write_string(u'Detecting SOS Signal+');
    time.sleep(1);
    lcd.clear();
    lcd.write_string(u'Detecting SOS SignalX');
    time.sleep(1);
    lcd.clear();
    lcd.write_string(u'Detecting SOS Signal+');
    time.sleep(1);
    lcd.clear();
    lcd.write_string(u'Detecting SOS SignalX');
    time.sleep(1);
    lcd.clear();
    lcd.write_string(u'Another user having an Emergency        ');
    lcd.write_string(u'Lattitude');
    lcd.write_string(str(lat));
    lcd.write_string(u'  Longitude');
    lcd.write_string(str(lon));
    time.sleep(4);
    lcd.clear();

    print "another user is having an emergency";
    #pin the location and askfor reroute
if (emergency==1)&(abs(my_bear-bearing)<=10):
    lcd.clear();
    lcd.write_string(u'Detecting Emergency Signal+');
    time.sleep(1);
    lcd.clear();
    lcd.write_string(u'Detecting Emergency SignalX');
    time.sleep(1);
    lcd.clear();
    lcd.write_string(u'Detecting Emergency Signal+');
    time.sleep(1);
    lcd.clear();
    lcd.write_string(u'Detecting Emergency SignalX');
    time.sleep(1);
    lcd.clear();
    lcd.write_string(u'Detecting Emergency Signal+');
    time.sleep(1);
    lcd.clear();
    lcd.write_string(u'Detecting Emergency SignalX');
    time.sleep(1);
    lcd.clear();
    lcd.write_string(u'An Ambulance is on the way..Pleasereduce speed and let it through');
    time.sleep(4);
    lcd.clear();
    print "An ambulance is on the way...Reduce speed and please let it through";
    



