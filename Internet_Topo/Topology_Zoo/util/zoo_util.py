# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 21:05:00 2016

@author: Mike
"""



class Mininet_topology_zoo():
    '''
    construct the topology in mininet from topology zoo
    http://www.topology-zoo.org/
    every switch has only one host.
    '''
    all_switches = []
    all_links = []

    def __init__(self):
        # Read topology info
        file_name = "Kdl"            
        
        file = open(file_name +  ".gml","r")
        self.all_switches, self.all_links = self.handler(file)
        # Add default members to class

        #print self.all_links        
        
        
        edge_file = open(file_name + '_' + str(len(self.all_switches)) + '_' + str(len(self.all_links)), 'w')

        edge_file.write(str(len(self.all_switches)) + ' ' + str(len(self.all_links)) + ' 2 0\n')

        for l in self.all_links:
                edge_file.write(str(l[0]) + ' ' + str(l[1]) + '\n')
    

        file.close()
        edge_file.close()        
        
        #self._addSwitches(self.all_switches)
        #self._addLinks(self.all_switches, self.all_links)

    def handler(self,file):
        switches = []
        links = []
        for line in file:
            if line.startswith("    id "):
                token = line.split("\n")
                token = token[0].split(" ")
                line = line[7:]
                if not line.startswith("\""):
                    token = line.split("\n")
                    switches.append(int(token[0]))
            if line.startswith("    source"):
                token = line.split("\n")
                token = token[0].split(" ")
                sw1 = int(token[-1])
            if line.startswith("    target"):
                token = line.split("\n")
                token = token[0].split(" ")
                sw2 = int(token[-1])
                links.append((sw1,sw2))
        return switches, links

    #def _addSwitches(self,switches):
        #for s in switches:
            #self.addSwitch('s%d' %s)
            #self.addHost('h%d'  %s)


    def _addLinks(self,switches,links):
        #for s in switches:
        #    self.addLink("h%s" %s, "s%s" %s, 0)
    
        for dpid1, dpid2 in links:
            self.addLink(node1="s%s" %dpid1, node2="s%s" %dpid2)
            
            
topos = Mininet_topology_zoo()