print('Exc 4.1')
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
nat=nat.replace('Fast','Gigabit')
print('Измененная настройка:', nat)
print('-----------------------------------------')

print('Exc 4.2')
mac = "AAAA:BBBB:CCCC"
mac=mac.replace(':','.')
print(mac)
print('-----------------------------------------')

print('Exc 4.3')
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
config=config.split()
print('Промежуточный контроль:', config)
vlans=config[-1].split(',')
print('Итог:', vlans)
print('-----------------------------------------')

print('Exc 4.4')
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
temp=list(set(vlans))
result=sorted(temp)
print(result)
print('-----------------------------------------')

print('Exc 4.5')
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
vlans1=command1.split()
vlans2=command2.split()
vlans1=set(vlans1[-1].split(','))
vlans2=set(vlans2[-1].split(','))
result=sorted(vlans1 & vlans2)
print(result)
print('-----------------------------------------')

print('Exc 4.6')
ospf_route = " 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_route=ospf_route.replace(',','')
ospf_route=ospf_route.split()
print(ospf_route)
prefix=ospf_route[0]
metric=ospf_route[1]
nexthop=ospf_route[3]
time=ospf_route[4]
interface=ospf_route[5]

ip_template='''
Prefix:             {}
AD/Metric:          {}
Next-Hop:           {}
Last update:        {}
Outbound Interface: {}
'''
print(ip_template.format(prefix,metric,nexthop,time,interface))
print('-----------------------------------------')

print('Exc 4.7')
mac = "AAAA:BBBB:CCCC"
mac=mac.split(':')
print(mac)
result=bin(int(mac[0],16))+bin(int(mac[1],16))+bin(int(mac[2],16))
result=result.replace('0b','')
print(result)

print('-----------------------------------------')

print('Exc 4.8')
ip = "192.168.3.1"
ip=ip.split('.')
oct1=int(ip[0])
oct2=int(ip[1])
oct3=int(ip[2])
oct4=int(ip[3])
ip_template2 = '''
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:<08b}  {1:<08b}  {2:<08b}  {3:<08b}
'''
print(ip_template2.format(oct1,oct2,oct3,oct4))
print('-----------------------------------------')