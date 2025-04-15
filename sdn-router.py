#!/usr/bin/python
from mininet.node import RemoteController
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI


class LinuxRouter(Node):
    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()

class NetworkTopo(Topo):
    def build(self, **_opts):
        # ROUTERS
        r1 = self.addHost('r1', cls=LinuxRouter, ip='10.0.0.1/24')
        r2 = self.addHost('r2', cls=LinuxRouter, ip='10.0.0.2/24')
        self.addLink(r1, r2, 
                    intfName1='r1-eth2', 
                    intfName2='r2-eth2',
                    params1={'ip': '10.100.0.1/24'}, 
                    params2={'ip': '10.100.0.2/24'})

        # SWITCHES
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        self.addLink(s1, r1, intfName2='r1-eth1', params2={'ip': '10.0.1.1/24'})
        self.addLink(s2, r2, intfName2='r2-eth1', params2={'ip': '10.0.2.1/24'})

        # HOSTS
        h1 = self.addHost('h1', ip='10.0.1.251/24', defaultRoute='via 10.0.1.1')  # Host d1 in 10.0.1.0/24
        h2 = self.addHost('h2', ip='10.0.2.251/24', defaultRoute='via 10.0.2.1')  # Host d2 in 10.0.2.0/24S
        self.addLink(h1, s1)
        self.addLink(h2, s2)


def run():
    print("START")
    topo = NetworkTopo()
    net = Mininet(topo=topo, controller=lambda name: RemoteController(name, ip='127.0.0.1', port=6633))

    # ADD ROUTING
    info(net['r1'].cmd("ip route add 10.0.2.0/24 via 10.0.0.2 dev r1-eth2"))  # r1 knows how to reach subnet 2
    info(net['r2'].cmd("ip route add 10.0.1.0/24 via 10.0.0.1 dev r2-eth2"))  # r2 knows how to reach subnet 1

    net.start()
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()