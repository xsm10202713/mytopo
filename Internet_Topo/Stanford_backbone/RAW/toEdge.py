# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 17:02:35 2016

@author: Mike
"""

link_file = open('link.csv')
switch_file = open('switch.csv')
edge_file = open('stanford_32_37', 'w')



switch_num = 0
switch_name_count = {}
switch_port_count = {}
switch_list = []

for line in switch_file:
    line = line.strip()
    info = line.split(',')
    
    if (info[0] in switch_name_count) == False:
        print 'in'
        switch_name_count[info[0]] = switch_num
        switch_num += 1
    print info[0]
    switch_port_count[info[1]] = switch_name_count[info[0]]




links = list()
    
for line in link_file:
    line = line.strip()
    info = line.split(',')
    s0 = switch_port_count[info[0]]
    s1 = switch_port_count[info[1]]
    
    if (s0,s1) not in links and (s1,s0) not in links:
        links.append(s0,s1)
    
edge_file.write(str(switch_num) + ' ' + str(len(links)) + ' 2 0\n')

for (s0,s1) in links:
    edge_file.write(s0 + ' ' + s1 + '\n')
    
link_file.close()
switch_file.close()
edge_file.close()