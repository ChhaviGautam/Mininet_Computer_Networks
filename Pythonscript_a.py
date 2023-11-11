#!/usr/bin/env python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class LinuxRouter(Node):
    "A Node with IP forwarding enabled."

    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()

class NetworkTopo(Topo):
    "A LinuxRouter connecting three IP subnets"

    def build(self, **_opts):
        defaultIP = '192.168.1.1/24'
        router1 = self.addNode('r1', cls=LinuxRouter, ip=defaultIP)
        router2 = self.addNode('r2', cls=LinuxRouter, ip='172.16.0.1/12')
        router3 = self.addNode('r3', cls=LinuxRouter, ip='10.0.0.1/8')

        s1, s2, s3 = [self.addSwitch(s) for s in ('s1', 's2', 's3')]

        self.addLink(s1, router1, intfName2='r1-eth1', params2={'ip': defaultIP})
        self.addLink(s2, router2, intfName2='r2-eth1', params2={'ip': '172.16.0.1/12'})
        self.addLink(s3, router3, intfName2='r3-eth1', params2={'ip': '10.0.0.1/8'})

        h1 = self.addHost('h1', ip='192.168.1.100/24', defaultRoute='via 192.168.1.1')
        h2 = self.addHost('h2', ip='192.168.1.101/24', defaultRoute='via 192.168.1.1')
        h3 = self.addHost('h3', ip='172.16.0.100/12', defaultRoute='via 172.16.0.1')
        h4 = self.addHost('h4', ip='172.16.0.101/12', defaultRoute='via 172.16.0.1')
        h5 = self.addHost('h5', ip='10.0.0.100/8', defaultRoute='via 10.0.0.1')
        h6 = self.addHost('h6', ip='10.0.0.101/8', defaultRoute='via 10.0.0.1')

        for h, s in [(h1, s1), (h2, s1), (h3, s2), (h4, s2), (h5, s3), (h6, s3)]:
            self.addLink(h, s)

        # Add router-router link in a new subnet for the router-router connection
        self.addLink(router1, router2, intfName1='r1-eth2', intfName2='r2-eth2', params1={'ip': '10.100.0.1/24'}, params2={'ip': '10.100.0.2/24'})
        self.addLink(router2, router3, intfName1='r2-eth3', intfName2='r3-eth2', params1={'ip': '10.101.0.1/24'}, params2={'ip': '10.101.0.2/24'})
        self.addLink(router3, router1, intfName1='r3-eth3', intfName2='r1-eth3', params1={'ip': '10.102.0.1/24'}, params2={'ip': '10.102.0.2/24'})

def run():
    "Test linux router"
    topo = NetworkTopo()
    net = Mininet(topo=topo, waitConnected=True)
    net.start()
    

    # Add static routes for subnets not directly connected
    net['r1'].cmd('ip route add 172.16.0.0/12 via 10.100.0.2')
    net['r1'].cmd('ip route add 10.0.0.0/8 via 10.102.0.1')

    net['r2'].cmd('ip route add 192.168.1.0/24 via 10.100.0.1')
    net['r2'].cmd('ip route add 10.0.0.0/8 via 10.101.0.2')

    net['r3'].cmd('ip route add 192.168.1.0/24 via 10.102.0.2')
    net['r3'].cmd('ip route add 172.16.0.0/12 via 10.101.0.1')

    info('*** Routing Table on Router:\n')
    info(net['r1'].cmd('route'))
    info(net['r2'].cmd('route'))
    info(net['r3'].cmd('route'))


    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
