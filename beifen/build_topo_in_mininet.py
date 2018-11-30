# -*- coding: utf-8 -*-
"""
Created on Tue May 31 09:51:09 2016

@author: mike
"""

def getport(s,port):
    if s not in port.keys():
        port[s]=1
    else:
        port[s] = port[s]+1
    return port





class TRF_Topo(Topo):

    def build(self, file_name = 'dcell_4_1.trf'):
        port={}
        topo_file = open(file_name)
        
        first_line = topo_file.readline()
        
        [num_switch, num_link, undefined_arg, num_host] = [ int(i) for i in first_line.split(' ')]

        
        #linkopt = dict(max_queue_size=1000, use_htb = True)#dict(bw =10, delay = '5ms', loss = 10, max_queue_size=1000,use_htb=True) 
        
        links = []
        for line in topo_file:
            link = [ int(i) for i in line.split(' ')]
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

        
if __name__ == '__main__':
    setLogLevel('info')
    simpleTest()
