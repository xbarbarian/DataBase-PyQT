import dis


# Метакласс для проверки соответствия сервера:
class ServerMaker(type):

    def __init__(self, clsname, bases, clsdict):
        #к моменту начала работы метода __ini__ метакласса словарь
        #атрибутов контролируемого класса уже сформирован

        for key ,value in clsdict.items():
            #Пропустим специальные и частные методы
            if key.startswith("__"):
                continue

            #Пропустим любые невызываемые объекты
            if not hasattr(value,"__call__"):
                continue
            #Проверить наличие строки документирования
            if not getattr(value,"__doc__"):
                raise TypeError(f'Метод {key} должен иметь строку документации из class {clsdict.get("__qualname__")}')

        # Список методов,которые используются в функции класс:
        methods = []
        # Атрибуты, используемые в функции классов
        attrs = []
        # перебираем ключи
        for func in clsdict:
            try:
                # Возвращает итератор по инстуркциям в предоставленной функции
                # методе строке исходного кода или объекта
                ret = dis.get_instructions(clsdict[func])
                # Если не функция то ловим исключение
                # (если порт)
            except TypeError:
                pass
            else:
                # Раз функция разбираем код, получая используемые методы и атрибуты.
                for i in ret:
                    # i - Instruction(opname='LOAD_GLOBAL', opcode=116, arg=9, argval='send_message',
                    # argrepr='send_message', offset=308, starts_line=201, is_jump_target=False)
                    # opname - имя для операции
                    if i.opname == 'LOAD_GLOBAL':
                        if i.argval not in methods:
                            # заполняем списко методами, использующимися в функциях класса
                            methods.append(i.argval)
                    elif i.opname == 'LOAD_ATTR':
                        if i.argval not in attrs:
                            # заполняем список атрибутами и спользующимися в функциях класса
                            attrs.append(i.argval)

        # Если обнаружено использование недопустимого метода connect делаем исключение
        if 'connect' in methods:
            raise TypeError('Использование метода connect недопустимо в серверном классе')
            # Если сокет не инициализировался константами SOCK_STREAM(TCP) AF_INET(IPv4), тоже исключение.
        if not ('SOCK_STREAM' in attrs and 'AF_INET' in attrs):
                raise TypeError('Некорректная инициализация сокета.')
            # Обязательно вызываем конструктор предка:
        super().__init__(clsname, bases, clsdict)


# Метакласс для проверки корректности клиентов:
class ClientMaker(type):
    def __init__(self, clsname, bases, clsdict):
        # Список методов, которые используются в функциях класса:
        methods = []
        for func in clsdict:
            # Пробуем
            try:
                ret = dis.get_instructions(clsdict[func])
                # Если не функция то ловим исключение
            except TypeError:
                pass
            else:
                # Раз функция разбираем код, получая используемые методы.
                for i in ret:
                    if i.opname == 'LOAD_GLOBAL':
                        if i.argval not in methods:
                            methods.append(i.argval)
        # Если обнаружено использование недопустимого метода accept, listen, socket бросаем исключение:
        for command in ('accept', 'listen', 'socket'):
            if command in methods:
                raise TypeError('В классе обнаружено использование запрещённого метода')
        # Вызов get_message или send_message из utils считаем корректным использованием сокетов
        if 'get_message' in methods or 'send_message' in methods:
            pass
        else:
            raise TypeError('Отсутствуют вызовы функций, работающих с сокетами.')
        super().__init__(clsname, bases, clsdict)


class DocMeta(type):
    """Метакласс, проверяющий наличие строк в документации в подконтрольном классе"""
    def __init__(self,clsname,bases,clsdict):
        #к моменту начала работы метода __ini__ метакласса словарь
        #атрибутов контролируемого класса уже сформирован

        for key ,value in clsdict.items():
            #Пропустим специальные и частные методы
            if key.startswith("__"):
                continue

            #Пропустим любые невызываемые объекты
            if not hasattr(value,"__call__"):
                continue
            #Проверить наличие строки документирования
            if not getattr(value,"__doc__"):
                raise TypeError(f'Метод {key} должен иметь строку документации из class {clsdict.get("__qualname__")}')

        type.__init__(self,clsname,bases,clsdict)

