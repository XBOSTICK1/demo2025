import os

os.system('mkdir /etc/net/ifaces/ens34')
os.system('mkdir /etc/net/ifaces/ens35')

os.system('echo "172.16.1.1/28" /etc/net/ifaces/ens34/ipv4address')
os.system('echo "172.16.2.1/28" /etc/net/ifaces/ens35/ipv4address')

os.system('cp /etc/net/ifaces/ens33/options /etc/net/ifaces/ens34')
os.system('cp /etc/net/ifaces/ens33/options /etc/net/ifaces/ens35')

os.system('apt-get update && apt-get -y install firewalld && systemctl enable --now firewalld')
os.system('firewall-cmd --permanent --zone=public --add-interface=ens33')
os.system('firewall-cmd --permanent --zone=trusted --add-interface=ens34')
os.system('firewall-cmd --permanent --zone=trusted --add-interface=ens35')
os.system('firewall-cmd --permanent --zone=public --add-masquerade')
os.system('firewall-cmd --complete-reload')
