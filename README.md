# PyCNC-Web
PyCNC with Web interface
Original version by Nikolay-Kha/PyCNC

This cloned version is being transformed to support web interface to control a multiaxis CNC machine.
In order to be used as a Laser Cutter/Engraver the code will support a new axis to control a Laser diode.

Required:
  Install WebIOPi follow instructions http://webiopi.trouch.com/INSTALL.html

Configure the WebIOPi server /etc/webiopi/config.    

In the /PyCNC-master/htdocs folder you will find the web site files accessible in the browser address:
  http://raspberrypi:8000/


copy the file PyCNC-master/extra/pycnc.conf to /etc/pycnc.conf

The /usr/local/lib/python2.7/dist-packages/cnc/script.py is the python code that makes the interface with the web.
GPIO 17 has a Led connected to test web commands.

Note:
  Append those paths with the correct folders inside the script.py so that
  python can import code. This one was tricky to find.

  sys.path.append('/home/pi/Desktop/PyCNC/PyCNC-master')<br>
  sys.path.append('/home/pi/Desktop/PyCNC/PyCNC-master/cnc/hal_raspberry')


<img src="https://github.com/eirasys/PyCNC-with-WEB/blob/master/PyCNC-Web_02.png?raw=true">
