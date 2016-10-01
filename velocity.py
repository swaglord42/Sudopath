#made by nk.recieve data from cloud

from RPLCD import CharLCD

import time
lcd = CharLCD(pin_rs=26, pin_e=24, pins_data=[22, 18, 16, 12])
check = 0
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

    lat_dir=float(signal_str[11]);

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





my_vel=input("enter your velocity");

lcd.clear();

lcd.write_string(u'current velocity+');

time.sleep(1);

lcd.clear();

lcd.write_string(u'current velocityX');

time.sleep(1);

lcd.clear();

lcd.write_string(u'current velocity+');

time.sleep(1);

lcd.clear();

lcd.write_string(u'current velocityX');

time.sleep(1);

lcd.clear();

lcd.write_string(u'current velocity+');

time.sleep(1);
lcd.clear();
lcd.write_string(u'Current velocity=');

lcd.write_string(str(my_vel));

time.sleep(4);

lcd.clear();

my_bear=input("enter bearing")

lcd.clear();

    

if (my_vel<25)&(my_vel>=0):

    lcd.clear();

    lcd.write_string(u'checking for traffic in your area.');

    time.sleep(1);

    lcd.clear();

    lcd.write_string(u'checking for traffic in your area..');

    time.sleep(1);

    lcd.clear();

    lcd.write_string(u'checking for traffic in your area...');

    time.sleep(1);

    lcd.clear();

    lcd.write_string(u'checking for traffic in your area....');

    time.sleep(1);

    lcd.clear();

    lcd.write_string(u'checking for traffic in your area.....');

    time.sleep(1);



    print "checking for traffic in your area.....";

    if (velocity<20)&(velocity>0)&(abs(my_bear-bearing==0)):

        print "theres traffic in your area....\nAlerting other users....";

        lcd.clear();

        lcd.write_string(u'Detected traffic in your area....');

        lcd.write_string(u'       Alerting other users');

        time.sleep(4);

        check=1;
	
        #jerrin uses the lat and lon to ping the area

    if check==0:

        lcd.clear();

        lcd.write_string(u'No traffic in your area');

        time.sleep(4);

        lcd.clear();

        print "No traffic";


