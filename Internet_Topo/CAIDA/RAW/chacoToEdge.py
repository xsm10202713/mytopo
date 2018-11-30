# -*- coding: utf-8 -*-
"""
Created on Mon Jul 04 20:40:50 2016

@author: Mike
"""

topo_file_name = 'caida_bcc.graph'
topo_file = open(topo_file_name)

first_line = topo_file.readline()
[num_switch, num_link] = [ int(i) for i in first_line.split(' ')]

links = []
num_line = 0
for line in topo_file:
    line = line.strip()
    for i in line.split(' '):
        if not ([int(i) - 1, num_line] in links):
            links.append([num_line, int(i) - 1])
    num_line += 1
    
edge_file = open('caida_bcc_edge', 'w')

edge_file.write(str(num_switch) + ' ' + str(len(links)) + ' 2 0\n')

for l in links:
    edge_file.write(str(l[0]) + ' ' + str(l[1]) + '\n')
    

edge_file.close()
topo_file.close()