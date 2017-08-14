from netmiko import ConnectHandler
pynet_rtr1 = {'device_type':'cisco_ios','ip':'184.105.247.70','username':'pyclass','password':'88newclass'}
pynet_rtr2 = {'device_type':'cisco_ios','ip':'184.105.247.71','username':'pyclass','password':'88newclass'}
pynet_jnpr_srx1 = {'device_type':'juniper','ip':'184.105.247.76','username':'pyclass','password':'88newclass'}
all_devices = [pynet_rtr1,pynet_rtr2,pynet_jnpr_srx1]
for a_device in all_devices:
    net_connect = ConnectHandler(**a_device)
    output = net_connect.send_command('sh arp')
    print "/n/n"
    print a_device
    print output



