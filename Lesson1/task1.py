'''
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться
доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен
именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего
сообщения («Узел доступен», «Узел недоступен»).
При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
'''

import ipaddress
import socket
import os
import platform
import subprocess


def get_adresses(hosts: list) -> list:
    hostname = ([ipaddress.ip_address(socket.gethostbyname(host)) for host in hosts])
    return hostname


def host_ping(hostname: list) -> None:
    """
    Функция проверяте доступность узлов и выводит результат
    """
    option = '-n' if platform.system().lower() == 'windows' else '-c'

    for address in hostname:
        responds = subprocess.call(('ping', option, str(address)), stdout=subprocess.DEVNULL)
        if responds == 0:
            print([{'host': str(address), 'answer': 'The node is available', 'reachability': responds}])

        else:
            print([{'host': str(address), 'answer': 'The node is not available', 'reachability': responds}])


if __name__ == '__main__':
    HOSTS = ['192.168.1.1', '192.168.1.66', 'google.com', 'yandex.ru']

    ip_addresses = get_adresses(HOSTS)
    host_ping(ip_addresses)
