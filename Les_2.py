london_co = {
"r1": {
    "location": "21 New Globe Walk",
    "vendor": "Cisco",
    "model": "4451",
    "ios": "15.4",
    "ip": "10.255.0.1"
},
"r2": {
    "location": "21 New Globe Walk",
    "vendor": "Cisco",
    "model": "4451",
    "ios": "15.4",
    "ip": "10.255.0.2"
},
"sw1": {
    "location": "21 New Globe Walk",
    "vendor": "Cisco",
    "model": "3850",
    "ios": "3.6.XE",
    "ip": "10.255.0.101",
    "vlans": "10,20,30",
    "routing": True
}
}
'''
#Excersice 5.1
device_number = input('Введите номер устройства: ')
print('\n' + '-' * 30)
print(london_co[device_number])
print('='*150)

#Excersice 5.1a
device_number = input('Введите наименование устройства: ')
parametr = input('Какой параметр Вас интересует? ')
print('\n' + '-' * 30)
print(london_co[device_number][parametr])
print('='*150)

#Excersice 5.1b
dev_names=list(london_co.keys())
dev_names=','.join(dev_names)
str1 = 'Введите наименование устройства ('+dev_names+'): '
device_number = input(str1)
dev_keys=london_co[device_number].keys()
dev_keys=','.join(dev_keys)
str2 = 'Какой параметр Вас интересует ('+dev_keys+'): '
parametr = input(str2)
print('\n' + '-' * 30)
print(london_co[device_number][parametr])

#Excersice 5.1c
dev_names=list(london_co.keys())
dev_names=','.join(dev_names)
str1 = 'Введите наименование устройства ('+dev_names+'): '
device_number = input(str1)
dev_keys=london_co[device_number].keys()
dev_keys=','.join(dev_keys)
str2 = 'Какой параметр Вас интересует ('+dev_keys+'): '
parametr = input(str2)
print('\n' + '-' * 30)
result=london_co[device_number].get(parametr,'Такого параметра не существует!')
print(result)

#Excersice 5.1d
dev_names=list(london_co.keys())
dev_names=','.join(dev_names)
str1 = 'Введите наименование устройства ('+dev_names+'): '
device_number = input(str1)
device_number=device_number.lower()
dev_keys=london_co[device_number].keys()
dev_keys=','.join(dev_keys)
str2 = 'Какой параметр Вас интересует ('+dev_keys+'): '
parametr = input(str2)
parametr=parametr.lower()
print('\n' + '-' * 30)
result=london_co[device_number].get(parametr,'Такого параметра не существует!')
print(result)
'''

#Excersice 5.2
print('Программа поможет Вам преобразовать IP-адрес и маску подсети в двоичный формат'+'\n')
ip_mask =input('Введите адрес в формате: 10.1.1.0/24 \n')
print()
ip_mask=ip_mask.split('.')
oct1=int(ip_mask[0])
oct2=int(ip_mask[1])
oct3=int(ip_mask[2])
mask=ip_mask[3].split('/')
oct4=int(mask[0])
mask0='/'+mask[1]
mask=int(mask[1])
mask_bin='1'*mask+'0'*(32-mask)
mask_oct1=int(mask_bin[0:8],2)
mask_oct2=int(mask_bin[8:16],2)
mask_oct3=int(mask_bin[16:24],2)
mask_oct4=int(mask_bin[24:32],2)
ip_template = '''
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:<08b}  {1:<08b}  {2:<08b}  {3:<08b}
'''
mask_template = '''
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:<08b}  {1:<08b}  {2:<08b}  {3:<08b}
'''
print('Результат преобразования IP-адреса в двоичный формат:','\n',ip_template.format(oct1,oct2,oct3,oct4))
print('Результат преобразования маски подсети в десятичный и двоичный форматы:'+'\n'*2+mask0,mask_template.format(mask_oct1,mask_oct2,mask_oct3,mask_oct4))