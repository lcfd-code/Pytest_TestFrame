#coding=utf-8
import serial,time
from Common.meter_config import *

'''
** 函数功能: 向串口 发送 指定 长度 的 数据
** 入口参数:  pBuffer:要发送的数据list
** 出口参数:
'''
def TMCLPort_SendBuffer(pBuffer):
    #************   发送串口 数据  ************
    m_CurUartPort=serial.Serial(com_motor, 9600, timeout=0.5)
    m_CurUartPort.close()  ### 关闭串口
    m_CurUartPort.open()   ### 打开串口
    m_CurUartPort.write(pBuffer) ### 发送数据
    #print  pBuffer
    m_CurUartPort.close()  ### 关闭串口


def TMCLDev_MovePositon(invtime):
    #TMCLPort_SendBuffer('cfg spd=30000\n')#速度
    TMCLPort_SendBuffer('ena\n')
    TMCLPort_SendBuffer('mov\n')
    time.sleep(invtime)
    TMCLPort_SendBuffer('stp\n')


if __name__=='__main__':
    #TMCLDev_MovePositon(20)
    #TMCLPort_SendBuffer('mov\n')
    #TMCLPort_SendBuffer('stp\n')
    #TMCLPort_SendBuffer('cfg spd=-35000\n')
    #TMCLPort_SendBuffer('ena\n')
    TMCLPort_SendBuffer('mov\n'.encode('utf-8'))
    #TMCLPort_SendBuffer("sav\n")
    TMCLPort_SendBuffer('stp\n'.encode('utf-8'))