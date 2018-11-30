# -*- coding: utf-8 -*-
"""
Created on Tue May 31 09:51:09 2016

@author: mike
"""
port = 32
topo_file_name = 'fattree_' + str(port)


        
class FattreeTopo():
    "Topology for fat tree topology"
    
    def __init__( self, n=4,):
        
        
        self.host_ids = list()
        self.switch_ids = list()
        self.edges = list()
        self.switch_id_pair = list()

        self.fattree(n)
        
        topo_file = open(topo_file_name + '_'+str(len(self.switch_ids)) + '_' + str(len(self.switch_id_pair)),'w')        
        
        
        topo_file.write(str(len(self.switch_ids)) + ' ' + str(len(self.switch_id_pair) ) + ' 2 0\n')

        for (s1, s2) in self.switch_id_pair:
            topo_file.write(str(s1 - 1) + ' ' + str(s2 - 1) + '\n')
            
        topo_file.close()

        
    def fattree( self, k ):
        pod_size = k / 2
        host_size = k*k*k/4
    
        for i in range(host_size):
            self.host_ids.append(i+1)
    
        for i in range(host_size, host_size + k * k + k * k / 4):
            self.switch_ids.append(i+1 - host_size)
    
        for i in range(host_size):
            j = i / pod_size + host_size;
            hi =  (i+1)
            sj =  (j+1 - host_size)
            self.edges.append((sj, hi))
    
        for i in range(host_size, host_size + k*pod_size):
            si = (i + 1 - host_size)
            for p in range(pod_size):
                j = (int((i-host_size) / pod_size) * pod_size
                    + host_size + k * pod_size + p)
                sj = (j + 1 - host_size)
                self.switch_id_pair.append((sj, si))
    
        for i in range(host_size + k*pod_size, host_size + k*pod_size*2):
            si = (i+1 - host_size)
            for p in range(pod_size):
                j = ((i - host_size - k*pod_size) % pod_size * k / 2
                    + host_size + k*k + p)
                sj = (j+1 - host_size)
                self.switch_id_pair.append((sj, si))
        
FattreeTopo(n = port)



