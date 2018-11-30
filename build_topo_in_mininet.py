# -*- coding: utf-8 -*-
"""
Created on Tue May 31 09:51:09 2016

@author: mike
"""
import os
from functools import partial

from mininet.cli import CLI
from mininet.examples.baresshd import cmd
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.node import RemoteController, Host
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."
    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )
        print os.getcwd()
        file_name ='Data_Center_Topo/BCube/TRF/bcube_1_4_24.trf'
        topo_file = open(file_name)

        first_line = topo_file.readline()

        [num_switch, num_link, undefined_arg, num_host] = [int(i) for i in first_line.split(' ')]

        links = []
        for line in topo_file:
            link = [int(i) for i in line.split(' ')]
            links.append(link)

        topo_file.close()

        sList = []
        hList = []
        for i in range(num_switch):
            sList.append(self.addSwitch('s' + str(i + 1)))

        for i in range(num_host):
            hList.append(self.addHost('h' + str(i + 1)))
            self.addLink(hList[i], sList[i])

        for i in range(num_link):
            self.addLink(sList[links[i][0]], sList[links[i][1]])

def simpleTest():
    topo = MyTopo()
    linkopt = dict(delay = '5ms', use_htb = True)
    net = Mininet(topo = topo, controller = partial(RemoteController, ip="202.117.15.122",port = 6653, **linkopt), autoSetMacs = True, link=TCLink)
    net.start()
    h1 = Host('h17')
#   flow,pingall, flow rule, mutil threads,5s
    for hostX in net.hosts:
        for hostY in net.hosts:
            if(hostX!=hostY):
                hostX.cmd("./sends" + ' ' + hostY.IP() + ' ' + 1 + ' ' + 0) # send 1 packet
#   firewall
    


#   send rule
    h1.cmd("python3 pushflow4.py")
#
#   api

    CLI( net )
    net.stop()

# topos = { 'mytopo': ( lambda: MyTopo() ) }
if __name__ == '__main__':
    setLogLevel('info')
    simpleTest()
