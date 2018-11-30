from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class SingleSwitchTopo( Topo ):
    "Single switch connected to n hosts."
    def build( self,k=4):
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
			sw = self.addSwitch('s{}'.format(i + 1))
			c.append(sw)

		# add aggregation ovs
		print "add aggregation switch"
		for i in range(L2 / 2):
			sw = self.addSwitch('s{}'.format(L1 + i + 1))
			a.append(sw)

		print "add edge switch"
		# add edge ovs
		for i in range(L3 / 2):
			sw = self.addSwitch('s{}'.format(L1 + L2 / 2 + i + 1))
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
				host = self.addHost('h{}'.format(count))
				h.append(host)
				# linkopts = dict(bw=15, delay='2ms', loss=5, use_htb=True)
				# net.addLink(sw1, host, **linkopts)
				# net.addLink(sw1, host, bw=10, delay='5ms', loss=10, max_queue_size=1000, use_htb=True)
				self.addLink(sw1, host)
				count += 1


if __name__ == '__main__':
    setLogLevel( 'info' )

