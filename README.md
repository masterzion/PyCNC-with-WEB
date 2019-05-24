# PyCNC-Web
PyCNC with Web interface
Original version by Nikolay-Kha/PyCNC

This cloned version is being transformed to support web interface to control a multiaxis CNC machine.
In order to be used as a Laser Cutter/Engraver the code will support a new axis to control a Laser diode.

Required:
1)  Install WebIOPi follow instructions http://webiopi.trouch.com/INSTALL.html

2) copy the file PyCNC-master/extra/pycnc.conf to /etc/pycnc.conf

3) Configure the WebIOPi server /etc/webiopi/config.
myscript = /usr/local/lib/python3.4/dist-packages/cnc/script.py
doc-root=/usr/local/lib/python3.4/dist-packages/cnc/webiopi/

4) restart the service:
sudo /etc/init.d/webiopi restart

The webservcer address:
http://raspberrypi:8000/

GPIO 17 has a Led connected to test web commands.



http://hostname:8000/



Note:
  Append those paths with the correct folders inside the script.py so that
  python can import code. This one was tricky to find.

  sys.path.append('/home/pi/Desktop/PyCNC/PyCNC-master')<br>
  sys.path.append('/home/pi/Desktop/PyCNC/PyCNC-master/cnc/hal_raspberry')


<img src="https://github.com/eirasys/PyCNC-with-WEB/blob/master/PyCNC-Web_02.png?raw=true">
