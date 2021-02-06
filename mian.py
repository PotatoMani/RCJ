from m5stack import *
from m5stack_ui import *
from uiflow import *
import module
import i2c_bus
import time

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xffccff)


go_plus_2 = module.get(module.GOPLUS2)

makeUl()
main()

def makeUl():
	label0 = M5Label('Text', x=145, y=113, color=0x000, font=FONT_MONT_14, parent=None)

def motorGo(l,r):
	if(r >= 0):
		if(r > 127):
			r = 127
		go_plus_2.set_motor_speed(go_plus_2.MA, -r)
	else:
		if(r < -127):
			r = -127
		go_plus_2.set_motor_speed(go_plus_2.MA, r)
	
	if(l >= 0):
		if(l > 127):
			l = 127
		go_plus_2.set_motor_speed(go_plus_2.MB, -l)
	else:
		if(l < -127):
			l = -127
		go_plus_2.set_motor_speed(go_plus_2.MB, l)

def getAngle():
	i2c0 = i2c_bus.easyI2C((32, 33), 80, freq=100000)
	tmpjd = i2c0.read_mem_data(63, 2, i2c_bus.UINT8LE)
	return int((((tmpjd[-1] * 256 + tmpjd[0]) / 65535) * 360))

def main():
	while True:
		wait(200)
		label0.set_text(str(getAngle()))
