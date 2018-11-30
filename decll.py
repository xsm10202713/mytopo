from mininet.topo import Topo

def servers(n, k):
    s=n
    if(k==0):
        return n
    else:
        for i in range(k):
            s=s*(s+1)
        return(s)



def cells( n,  k):

    if(k==0):
        return 1
    else:
        return (servers(n, k-1)+1)


def dcell( n,  k):


    edge = 0
    for i in range(k):

        number_of_cells = int(servers(n, k)/servers(n, i))
        for j in range(cells(n, i)):
            cell = j
            for v1 in range(j*servers(n, i-1)+j,(j+1)*servers(n, i-1)-1):
                v2 = (cell+1)*servers(n, i-1) + j
                for times in range(number_of_cells-1):
                    edge=edge+1
                cell=cell+1
    for ver in range( servers(n, k)):
        ord_of_swi = int(ver/n)
        rank_of_swi = ord_of_swi + servers(n, k)
        edge=edge+1
class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        k=4
        L1 = k * k / (2 * 2)
        L2 = L1 * 2
        L3 = L2
        c = []
        a = []
        e = []
        h = []
        # add core ovs
        print "add core switch"
        for i in range(L1):
            sw = self.addSwitch('s%s' % (i + 1))
            c.append(sw)

        # add aggregation ovs
        print "add aggregation switch"
        for i in range(L2):
            sw = self.addSwitch('s%s' % (L1 + i + 1))
            a.append(sw)

        print "add edge switch"
        # add edge ovs
        for i in range(L3 ):
            sw = self.addSwitch('s%s' % (L1 + L2 + i + 1))
            e.append(sw)

        print "add links between core and agg"
        # add links between core and aggregation ovs
        for i in range(L1):
            sw1 = c[i]
            print sw1,
            print "core to agg"
            for sw2 in a[i / (k / 2)::k / 2]:
                # linkopts = dict(bw=15, delay='2ms', loss=5, use_htb=True)
                # net.addLink(sw2, sw1, **linkopts)
                # net.addLink(sw2, sw1, bw=10, delay='5ms', loss=10, max_queue_size=1000, use_htb=True)
                self.addLink(sw2, sw1)

        print "add links between aggregation and edge ovs"
        # add links between aggregation and edge ovs
        for i in range(0, L2, k / 2):
            for sw1 in a[i:i + k / 2]:
                print sw1,
                print "agg to edge"
                for sw2 in e[i:i + k / 2]:
                    # linkopts = dict(bw=15, delay='2ms', loss=5, use_htb=True)
                    # net.addLink(sw2, sw1, **linkopts)
                    # net.addLink(sw2, sw1, bw=10, delay='5ms', loss=10, max_queue_size=1000, use_htb=True)
                    self.addLink(sw2, sw1)

        print "add hosts and its links with edge ovs"
        # add hosts and its links with edge ovs
        count = 1
        for sw1 in e:
            print sw1,
            print "'s host"
            for i in range(k / 2):
                host = self.addHost('h%s' % (count))
                h.append(host)
                # linkopts = dict(bw=15, delay='2ms', loss=5, use_htb=True)
                # net.addLink(sw1, host, **linkopts)
                # net.addLink(sw1, host, bw=10, delay='5ms', loss=10, max_queue_size=1000, use_htb=True)
                self.addLink(sw1, host)
                count += 1


topos = { 'mytopo': ( lambda: MyTopo() ) }


