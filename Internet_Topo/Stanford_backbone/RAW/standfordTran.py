class StanfordTopo( ):
    "Topology for Stanford backbone"

    PORT_ID_MULTIPLIER = 1
    INTERMEDIATE_PORT_TYPE_CONST = 1
    OUTPUT_PORT_TYPE_CONST = 2
    PORT_TYPE_MULTIPLIER = 10000
    SWITCH_ID_MULTIPLIER = 100000
    
    DUMMY_SWITCH_BASE = 1000
    
    PORT_MAP_FILENAME = "switch.txt"
    TOPO_FILENAME = "link.txt"
    
    
    dummy_switches = set()
    
    switchL = [] 
    switch_num = {}
    linkL = list()
    
    def add_switch(self, s):
        self.switchL.append(s)
        self.switch_num[s] = len(self.switchL) - 1

    def add_link(self, node1, node2):
        self.linkL.append((node1,node2))

    def __init__( self ):
        # Read topology info
        ports = self.load_ports(self.PORT_MAP_FILENAME)        
        links = self.load_topology(self.TOPO_FILENAME)
        switches = ports.keys()
        # Add default members to class.
        #super( StanfordTopo, self ).__init__()
        # Create switch nodes
        for s in switches:
            self.add_switch( "s%s" % s )
        # Wire up switches       
        self.create_links(links, ports)
        
        print self.switchL
        print self.linkL        
        
        num_list = list()

        for (i,j) in self.linkL:
            a = self.switch_num[i]
            b = self.switch_num[j]
            
            if ((a,b) not in num_list) and ( (b,a) not in num_list ):
                num_list.append((a,b))
        
        
        edge_file = open('stanford_26_46', 'w')
        for (i,j) in num_list:
            edge_file.write(str(i) + ' ' + str(j) + '\n')
        edge_file.close()

        # Wire up hosts
        #host_id = len(switches) + 1
        #for s in switches:
            # Edge ports
            #for port in ports[s]:
               # self.add_host( "h%s" % host_id )
               # self.add_link( "h%s" % host_id, "s%s" % s, 0, port )
               # host_id += 1
        # Consider all switches and hosts 'on'
        # self.enable_all()
            
    def load_ports(self, filename):
        ports = {}
        f = open(filename, 'r')
        for line in f:
            if not line.startswith("$") and line != "":
                tokens = line.strip().split(":")
                port_flat = int(tokens[1])
                
                dpid = port_flat / self.SWITCH_ID_MULTIPLIER
                port = port_flat % self.PORT_TYPE_MULTIPLIER
                
                if dpid not in ports.keys():
                    ports[dpid] = set()
                if port not in ports[dpid]:
                    ports[dpid].add(port)             
        f.close()
        return ports
        
    def load_topology(self, filename):
        links = set()
        f = open(filename, 'r')
        for line in f:
            if line.startswith("link"):
                tokens = line.split('$')
                src_port_flat = int(tokens[1].strip('[]').split(', ')[0])
                dst_port_flat = int(tokens[7].strip('[]').split(', ')[0])
                links.add((src_port_flat, dst_port_flat))
        f.close()
        return links
        
    def create_links(self, links, ports):  
        '''Generate dummy switches
           For example, interface A1 connects to B1 and C1 at the same time. Since
           Mininet uses veth, which supports point to point communication only,
           we need to manually create dummy switches

        @param links link info from the file
        @param ports port info from the file
        ''' 
        # First pass, find special ports with more than 1 peer port
        first_pass = {}
        for (src_port_flat, dst_port_flat) in links:
            src_dpid = src_port_flat / self.SWITCH_ID_MULTIPLIER
            dst_dpid = dst_port_flat / self.SWITCH_ID_MULTIPLIER
            src_port = src_port_flat % self.PORT_TYPE_MULTIPLIER
            dst_port = dst_port_flat % self.PORT_TYPE_MULTIPLIER
            
            if (src_dpid, src_port) not in first_pass.keys():
                first_pass[(src_dpid, src_port)] = set()
            first_pass[(src_dpid, src_port)].add((dst_dpid, dst_port))
            if (dst_dpid, dst_port) not in first_pass.keys():
                first_pass[(dst_dpid, dst_port)] = set()
            first_pass[(dst_dpid, dst_port)].add((src_dpid, src_port))
            
        # Second pass, create new links for those special ports
        dummy_switch_id = self.DUMMY_SWITCH_BASE
        for (dpid, port) in first_pass.keys():
            # Special ports!
            if(len(first_pass[(dpid,port)])>1):
                self.add_switch( "s%s" % dummy_switch_id )
                self.dummy_switches.add(dummy_switch_id)
            
                self.add_link( node1="s%s" % dpid, node2="s%s" % dummy_switch_id)
                dummy_switch_port = 2
                for (dst_dpid, dst_port) in first_pass[(dpid,port)]:
                    first_pass[(dst_dpid, dst_port)].discard((dpid,port))
                    self.add_link( node1="s%s" % dummy_switch_id, node2="s%s" % dst_dpid)
                    ports[dst_dpid].discard(dst_port)
                    dummy_switch_port += 1
                dummy_switch_id += 1  
                first_pass[(dpid,port)] = set()    
            ports[dpid].discard(port)
        
        # Third pass, create the remaining links
        for (dpid, port) in first_pass.keys():
            for (dst_dpid, dst_port) in first_pass[(dpid,port)]:
                self.add_link( node1="s%s" % dpid, node2="s%s" % dst_dpid)
                ports[dst_dpid].discard(dst_port)     
            ports[dpid].discard(port)      
            
            
            
s = StanfordTopo()