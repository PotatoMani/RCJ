from m5stack import *
from m5stack_ui import *
from uiflow import *
import module
import i2c_bus
import time

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xe9aa41)


go_plus_2 = module.get(module.GOPLUS2)

# 注册显示部件
label0 = M5Label('Text', x=145, y=113, color=0x000, font=FONT_MONT_14, parent=None)

# 运动函数部分
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

# 传感函数部分
def getAngle():
	i2c0 = i2c_bus.easyI2C((32, 33), 80, freq = 100000)
	tempjd = i2c0.read_mem_data(63, 2, i2c_bus.UINT8LE)
	return int((((tempjd[-1] * 256 + tempjd[0]) / 65535) * 360))
	
def getS(ID):
  address = [0,86,82,85,83,81,84,87,88]
  i2c0 = i2c_bus.easyI2C((32, 33), address[ID], freq = 100000)
  tempjl = i2c0.read_mem_data(80, 2, i2c_bus.UINT8LE)
  return int(tempjl[0] * 256 + tempjl[-1])

# 主函数
def main():
  
main()
		
