# 2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
# Меняться должен только последний октет каждого адреса.
# По результатам проверки должно выводиться соответствующее сообщение.

import ipaddress
from task1 import host_ping


def host_range_ping():
    check_list = []
    net = ipaddress.ip_network("192.4.2.0/28")
    for addr in net:
        a = (str(addr))
        check_list.append(a)
        host_ping(check_list)


if __name__ == '__main__':
    host_range_ping()