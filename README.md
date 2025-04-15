# Hyprid Traffic Engineering Using SDNs

> By Aditya Girisha `012145901`

## Install Requirements

### Install Python and Pip

```
curl https://pyenv.run | bash
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc
pyenv install 3.9.7
pyenv global 3.9.7
```

### Create and Activate Virtual Env
```
$ python3 -m venv venv
$ source venv/bin/activate
$ deactivate
```

### Install Python Requirements
```
apt install gcc python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev zlib1g-dev
$ pip3 install -r requirements.txt
```

### Install Ryu
```
git clone https://github.com/faucetsdn/ryu.git
cd ryu; pip install .
```

### Install Mininet
```
$ sudo apt-get install mininet
$ mn --version
```

### Install OVS
```
$ sudo apt-get install openvswitch-switch
$ ovs-vsctl --version
```

### Install Wireshark
```
$ sudo apt-get install wireshark
$ wireshark --version
```

