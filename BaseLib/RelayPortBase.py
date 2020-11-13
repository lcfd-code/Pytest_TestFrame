#coding=utf-8
import serial
import binascii,codecs
from Common.meter_config import *

'''
** 函数功能: 向串口 发送 指定 长度 的 数据
** 入口参数:  pBuffer:要发送的数据list
** 出口参数:
'''

def RelayPort_SendBuffer(com,pBuffer):
    pSendStr=""  # 初始化要发送的数据
    for i in range(len(pBuffer)):
      pSendStr += '%.2x'%(pBuffer[i])
    #print pSendStr
    #************   发送串口 数据  ************
    m_CurUartPort=serial.Serial(com, 9600, timeout=0.5)
    m_CurUartPort.close()  ### 关闭串口

    m_CurUartPort.open()   ### 打开串口
    m_CurUartPort.write(codecs.decode(pSendStr,'hex')) ### 发送数据
    m_CurUartPort.close()  ### 关闭串口

'''
** 函数功能: 将命令打包成固定格式，并发送到指定串口
** 入口参数:
   pAddress:设备地址
   pCmd:指令
   pCmdType：指令类型
   pMotorType：电机类型
   pValue：参数值
** 出口参数:
'''
def  RelayPort_SendFrameCmd(com,pHead,pAddress,pCmd,pVal1,pVal2,pVal3,pNum):
    # 设备数据头,地址，指令，参数值
    pBuffer=[int(pHead,16),int(pAddress,16),int(pCmd,16),int(pVal1,16),int(pVal2,16),int(pVal3,16),int(pNum,16)]
    #***********    计算校验位   *********
    pXOR=0
    for i in range(0,7):
      pXOR+=int(pBuffer[i])
    pBuffer.append(pXOR&0xFF)
    #************   发送串口 数据  ************
    RelayPort_SendBuffer(com,pBuffer)

'''
** 函数功能:吸合某一路继电器
** 命令 内容 格式: 指令+12+第几路
** 入口参数:  第几路
** 出口参数:
'''
def RelDev_Open(com,pNumber):
    RelayPort_SendFrameCmd(com,'0x55','0x01','0x12','0x00','0x00','0x00',pNumber)

'''
** 函数功能:断开某一路继电器
** 命令 内容 格式: 指令+11+第几路
** 入口参数:  第几路
** 出口参数:
'''
def RelDev_Close(com,pNumber):
    RelayPort_SendFrameCmd(com,'0x55','0x01','0x11','0x00','0x00','0x00',pNumber)

'''
** 函数功能:组命令
** 命令 内容 格式: 指令+13+
** 入口参数:  二进制O关1开 0101 1和3路开
** 出口参数:
'''
def RelDev_GroupCmd(pNumber):
    pstr=hex(int(pNumber,2))
    RelayPort_SendFrameCmd('0x55','0x01','0x13','0x00','0x00','0x00',pstr)


def RelayPort_sendread(pBuffer):
    pSendStr=""  # 初始化要发送的数据
    for i in range(len(pBuffer)):
      pSendStr += '%.2x'%(pBuffer[i])
    #print pSendStr
    #************   发送串口 数据  ************
    CurUartPort=serial.Serial(com_relay, 9600, timeout=0.5)
    CurUartPort.close()  ### 关闭串口
    CurUartPort.open()   ### 打开串口
    CurUartPort.write(pSendStr.decode("hex")) ### 发送数据
    n=CurUartPort.inWaiting()
    if n:
      re= str(binascii.b2a_hex(CurUartPort.read(n)))#[0:-1]
    CurUartPort.close()  ### 关闭串口
    return re

if __name__=='__main__':
       RelDev_Open('01')

       '''RelDev_GroupCmd('0b0000')
        RelDev_Open('01')
       '''
