from mininet.topo import Topo

class MyTopo(Topo):
    def build( self ):


        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        # h1 = self.addHost('h1', ip='172.16.20.10/24', defaultRoute='via 172.16.20.1')
        # h2 = self.addHost('h2', ip='172.16.10.10/24', defaultRoute='via 172.16.10.1')
        # h3 = self.addHost('h3', ip='192.168.30.10/24', defaultRoute='via 192.168.30.1')
        h1 = self.addHost('h1', ip='10.0.1.1/24', defaultRoute='via 10.0.1.2')
        h2 = self.addHost('h2', ip='10.0.2.1/24', defaultRoute='via 10.0.2.2')
        h3 = self.addHost('h3', ip='10.0.3.1/24', defaultRoute='via 10.0.3.2')
        # Add links
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s1, h1)
        self.addLink(s2, h2)
        self.addLink(s3, h3)

# Create an instance of custom topology class
topos = { 'mytopo': ( lambda: MyTopo() ) }