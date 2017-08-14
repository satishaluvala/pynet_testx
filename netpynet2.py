from netmiko import ConnectHandler
pynet_rtr2 = {'device_type':'cisco_ios','ip':'184.105.247.71','username':'pyclass','password':'88newclass'}
net_connect = ConnectHandler(**pynet_rtr2)
output = net_connect.config_mode()
output = net_connect.find_prompt()
print output

output = net_connect.send_command('do sh run | include logging')
print output

commands = ['logging buffered 12333']
output = net_connect.send_config_set(commands)
print output
 
output = net_connect.send_command('sh run | include logging')
print output



