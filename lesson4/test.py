
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


    def __call__(self, *args, **kwargs):
        obj = type.__call__(self,*args)
        for name in kwargs:
            setattr(obj,name,kwargs[name])
        return obj



class Test():

    def teds(self):
        pass


class Ond:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Не может быть отрицательной')
        instance.__dict__[self.name] = value


    def __delete__(self, instance):
        pass

class Work():

    hours = Ond()

    def __init__(self, hours):
        self.hours = hours




ans = Work(10)
print(ans)

# ans1= Test(a=1,b=2)
# print(ans1)









