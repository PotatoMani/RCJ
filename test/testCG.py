from m5stack import *
from m5stack_ui import *
from uiflow import *
import module
import i2c_bus
import time

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


go_plus_2 = module.get(module.GOPLUS2)

# 注册显示部件
label0 = M5Label('Text', x=145, y=113, color=0x000, font=FONT_MONT_14, parent=None)
label1 = M5Label('Text', x=44, y=213, color=0x000, font=FONT_MONT_14, parent=None)
label2 = M5Label('Text', x=19, y=181, color=0x000, font=FONT_MONT_14, parent=None)
label3 = M5Label('Text', x=19, y=43, color=0x000, font=FONT_MONT_14, parent=None)
label4 = M5Label('Text', x=44, y=12, color=0x000, font=FONT_MONT_14, parent=None)
label5 = M5Label('Text', x=241, y=12, color=0x000, font=FONT_MONT_14, parent=None)
label6 = M5Label('Text', x=277, y=43, color=0x000, font=FONT_MONT_14, parent=None)
label7 = M5Label('Text', x=277, y=181, color=0x000, font=FONT_MONT_14, parent=None)
label8 = M5Label('Text', x=241, y=213, color=0x000, font=FONT_MONT_14, parent=None)

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
  while True:
    label0.set_text(str(getAngle()))
    label1.set_text(str(getS(1)))
    label2.set_text(str(getS(2)))
    label3.set_text(str(getS(3)))
    label4.set_text(str(getS(4)))
    label5.set_text(str(getS(5)))
    label6.set_text(str(getS(6)))
    label7.set_text(str(getS(7)))
    label8.set_text(str(getS(8)))
    wait_ms(10)
  
main()
		
