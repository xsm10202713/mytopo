#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

# import mininet.net
from mininet.cli import CLI
from mininet.log import setLogLevel, info,error
from mininet.net import Mininet
from mininet.link import Intf
from mininet.topolib import TreeTopo
from mininet.util import quietRun
from mininet.node import RemoteController, OVSKernelSwitch,Controller

def checkIntf(intf):
    #make sure intface exists and is not configured.
    if(' %s:'% intf) not in quietRun('ip link show'):
        error('Error:', intf, 'does not exist!\n' )
        exit(1)
    ips = re.findall( r'\d+\.\d+\.\d+\.\d+', quietRun   ( 'ifconfig ' + intf ) )
    if ips:
        error("Error:", intf, 'has an IP address,'
            'and is probably in use!\n')
        exit(1)

if __name__ == "__main__":
    setLogLevel("info")
    OVSKernelSwitch.setup()
    intfName_1 = "enp2s0:2"     #将虚拟机eth2赋值给为变量intfName_1
    intfName_3 = "enp2s0:3"
    # info("****checking****", intfName_1, '\n')
    # checkIntf(intfName_1)    #检查是否可用
    # info("****checking****", intfName_3, '\n')
    # checkIntf(intfName_3)

    info("****creating network****\n")
    # net = Mininet(listenPort = 6653)  #创建一个Mininet的实例，端口为6633
    #
    # mycontroller = RemoteController('Controller',ip = "202.117.15.122",port=6653)#创建远程控制器，ip=192.168.0.1，端口是6633。

    net = Mininet(controller=Controller, autoSetMacs=True)
    #    n1 = RemoteController('c1', ip='11.0.0.12', port=6633)
    mycontroller = RemoteController('c2', ip='202.117.15.122', port=6653)
    switch_1 = net.addSwitch('s1')   #在net里添加交换机s1,mininet中规则为：如果不填充dpid参数，则dpid参数默认取sn的n.即s1的dpid为1。
    switch_2 = net.addSwitch('s2')
    switch_3 = net.addSwitch('s3')
    switch_4 = net.addSwitch('s4')

    net.controllers = [mycontroller] #将远程控制器添加到网络中
    #

    net.addLink(switch_1, switch_2, 2, 1)# node1,   node2, port1, port2
    net.addLink(switch_2, switch_3, 2, 1)#将s2的2端口跟s3的1端口连接起来。（物理连接）
    net.addLink(switch_1, switch_4, 3, 1)


    info("*****Adding hardware interface ",     intfName_1, "to switch:" ,switch_1.name, '\n')
    info("*****Adding hardware interface ",     intfName_3, "to switch:" ,switch_3.name, '\n')

    _intf_1 = Intf(intfName_1, node = switch_1, port =  1)#将intfName_1和s1的端口1相连，形成一个接口_intf_1
    _intf_3 = Intf(intfName_3, node = switch_3, port =  2)

    net.addLink(switch_4, switch_3, 2, 3)#为什么放在这里呢？因为mininet中允许的端口分配方式是从小到大分配，所以，s3的3端口的配置应该放在s3的2端口之后，虽然难看，但是必须这么做，当然你也可以从新分配端口，只要保证端口是从小到大分配就好了。

    info("Node: you may need to reconfigure the     interfaces for the Mininet hosts:\n",   net.hosts, '\n')
    net.build()
    mycontroller.start()
    switch_1.start([mycontroller])
    switch_2.start([mycontroller])
    switch_3.start([mycontroller])
    switch_4.start([mycontroller])
    # net.start()
    CLI(net)
    net.stop()
