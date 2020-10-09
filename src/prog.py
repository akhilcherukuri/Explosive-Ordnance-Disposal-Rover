import RPi.GPIO as GPIO
from time import sleep
import cgi, cgit

in1 = 05
in2 = 06
in3 = 13
in4 = 19
arm1 = 16
arm2 = 18
arm3 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(arm1,GPIO.OUT)
GPIO.setup(arm2,GPIO.OUT)

GPIO.setup(arm3,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
GPIO.output(arm1,GPIO.LOW)
GPIO.output(arm2,GPIO.LOW)
GPIO.output(arm3,GPIO.LOW)
p=GPIO.PWM(en,1000)
q=GPIO.PWM(en,1000)
p.start(25)
q.start(50)

while(1):
x=raw_input()

if x=='s':
print("stop")
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
x='z'
exec(open("/var/www/cgi-bin/stop.cgi").read())

elif x=='fowr':
print("forward")
GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.HIGH)
GPIO.output(in4,GPIO.LOW)
x='z'
exec(open("/var/www/cgi-bin/forward.cgi").read())

elif x=='back':
print("backward")
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.HIGH)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.HIGH)
x='z'
exec(open("/var/www/cgi-bin/reverse.cgi").read())

elif x=='left':
print("left")
GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.HIGH)
x='z'
exec(open("/var/www/cgi-bin/left.cgi").read())

elif x=='right':
print("right")
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.HIGH)
GPIO.output(in3,GPIO.HIGH)
GPIO.output(in4,GPIO.LOW)
x='z'
exec(open("/var/www/cgi-bin/right.cgi").read())

elif x=='lowspeed':
print("low")
p.ChangeDutyCycle(25)
x='z'

elif x=='mediumspeed':
print("medium")
p.ChangeDutyCycle(50)
x='z'

elif x=='highspeed':
print("high")
p.ChangeDutyCycle(75)
x='z'

elif x=='centertilt':
GPIO.output(arm1,GPIO.HIGH)
print("center")
q.ChangeDutyCycle(5)
time.sleep(1)
x='z'
exec(open("/var/www/cgi-bin/centertilt.cgi").read())

elif x=='righttilt':
GPIO.output(arm1,GPIO.HIGH)
print("right tilt")
q.ChangeDutyCycle(2.5)
time.sleep(1)
x='z'
exec(open("/var/www/cgi-bin/righttilt.cgi").read())

elif x=='lefttilt':
GPIO.output(arm1,GPIO.HIGH)
print("lef tilt")
q.ChangeDutyCycle(7.5)
time.sleep(1)
x='z'
exec(open("/var/www/cgi-bin/lefttilt.cgi").read())

elif x=='centerpan':

GPIO.output(arm2,GPIO.HIGH)
print("center pan")
q.ChangeDutyCycle(5)
time.sleep(1)
x='z'
exec(open("/var/www/cgi-bin/centerpan.cgi").read())

elif x=='rightpan':
GPIO.output(arm2,GPIO.HIGH)
print("right pan")
q.ChangeDutyCycle(2.5)
time.sleep(1)
x='z'
exec(open("/var/www/cgi-bin/rightpan.cgi").read())

elif x=='leftpan':
GPIO.output(arm2,GPIO.HIGH)
print("left pan")
q.ChangeDutyCycle(7.5)
time.sleep(1)
x='z'
exec(open("/var/www/cgi-bin/leftpan.cgi").read())

elif x=='armopen':
GPIO.output(arm3,GPIO.HIGH)
print("arm open")
q.ChangeDutyCycle(0.5)
time.sleep(1)
x='z'
exec(open("/var/www/cgi-bin/openarm.cgi").read())

elif x=='armclose':
GPIO.output(arm3,GPIO.HIGH)
print("arm close")

q.ChangeDutyCycle(2.5)
time.sleep(1)
x='z'
exec(open("/var/www/cgi-bin/closearm.cgi").read())

elif x=='clean':
print("GPIOs have been cleaned")
GPIO.cleanup()
break
