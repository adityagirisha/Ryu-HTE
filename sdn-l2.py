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

class SparseMeshTopo(Topo):
    def build(self, **_opts):
        # ROUTERS
        routers = {}
        for i in range(1, 18):
            routers[f'r{i}'] = self.addHost(f'r{i}', cls=LinuxRouter, ip=f'10.0.0.{i}/24')

        # LINKS
        links = [
            (1, 2, ), 
            (1, 5),
            (2, 3), 
            (2, 6),
            (3, 6), 
            (3, 7),
            (4, 5), 
            (4, 8),
            (5, 6), 
            (5, 8),
            (6, 9),
            (7, 10),
            (8, 12), 
            (8, 9),
            (9, 10),
            (11, 13),
            (12, 13),
            (13, 14), 
            (13, 15),
            (14, 16), 
            (14, 17),
            (15, 17)
        ]

        for r1, r2 in links:
            self.addLink(routers[f'r{r1}'], routers[f'r{r2}'])

        # HOSTS
        for i in range(1, 18):
            host = self.addHost(f'h{i}', ip=f'10.0.{i}.100/24', defaultRoute=f'via 10.0.0.{i}')
            self.addLink(host, routers[f'r{i}'])

def run():
    topo = SparseMeshTopo()
    net = Mininet(topo=topo, controller=lambda name: RemoteController(name, ip='127.0.0.1', port=6633))
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
