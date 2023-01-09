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