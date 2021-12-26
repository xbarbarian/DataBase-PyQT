# 3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2.
# Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате
# (использовать модуль tabulate). Таблица должна состоять из двух колонок и выглядеть примерно так:
#
# Reachable
# 10.0.0.1
# 10.0.0.2
#
# Unreachable
# 10.0.0.3
# 10.0.0.4
import ipaddress
import os
import platform
import subprocess


from tabulate import tabulate


def host_range_ping_tab(host):

    net = ipaddress.ip_network(host)

    option = '-n' if platform.system().lower() == 'windows' else '-c'

    responds = subprocess.call(('ping', option, str(host)), stdout=subprocess.DEVNULL)
    result = {'Reachable': [not responds]}
    result.update({'Unreachable': [hosting for hosting in net.hosts() if host not in result['Reachable']]})

    print(tabulate(result, headers='keys', tablefmt='simple'))



if __name__ == '__main__':
    host_range = '192.4.2.0/28'
    host_range_ping_tab(host_range)