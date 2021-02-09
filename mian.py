#           /^\/^\
#         _|__|  O|
# \/     /~     \_/ \
# \____|__________/  \
#         \_______      \
#               `\     \                 \
#                   |     |                  \
#                 /      /                    \
#                 /     /                       \\
#               /      /                         \ \
#             /     /                            \  \
#           /     /             _----_            \   \
#           /     /           _-~      ~-_         |   |
#         (      (        _-~    _--_    ~-_     _/   |
#           \      ~-____-~    _-~    ~-_    ~-_-~    /
#             ~-_           _-~          ~-_       _-~   
#               ~--______-~                ~-___-~

################
#PotatoMan 2021#
#RCJ - python  #
################

from m5stack import *
from m5stack_ui import *
from uiflow import *
import module
import i2c_bus
import time

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xff7300)


go_plus_2 = module.get(module.GOPLUS2)

# 注册显示部件
touch_button0 = M5Btn(text='START', x=125, y=105, w=70, h=30, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)

# 运动函数部分
def motorGo(l,r): # 电动机基本转动 -127 --- 127
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
		
def stop(): # 电动机停止
	motorGo(0,0)

def turnRight(): # 右转
	aim = getDirection() * 90
	kp = 1
	ki = 1
	v = 127
	err = 0
	la = now
	if(aim == 0):
		aim = 359
    
	while True:
		now = getAngle()
		if(now >= aim):
			break;
		elif(aim == 359 and mow >= 0):
			break;
		
		# pid部分
		err = now - la
		v = kp * (aim - now)
		v = v + ki * err
		la = now
		
		motorGo(v,-v)
	
	stop()
		
#辅助类函数
def getDirection(): # 判断方向
	angle = getAngle()
	if(angle <= 45 or angle >= 315):
		return 0
	  
	elif(angle >= 45 and angle <= 135):
		return 1
	  
	elif(angle >= 135 and angle <= 225):
		return 2
	  
	elif(angle >= 225 and angle <= 315):
		return 3
  

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
	turnRight()
  
# 按钮启动
def touch_button0_pressed():
	main() # 执行程序
  
touch_button0.pressed(touch_button0_pressed)

# main()