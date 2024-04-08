class InvalidDataException(Exception):
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f'Ошибка: сумма {self.amount} не соответствует'
class GetMoney(InvalidDataException):
    def get(self, money, amount):
       self.send_money(money, amount)
       print(f'{str(money)} в количестве {amount} получены')

    def send_money(self, money, amount):
        if not self.send_to_me(money, amount):
            raise InvalidDataException(100)

    def send_to_me(self, money, amount):
        return False

p = GetMoney(100)
#p.get('деньги', 100)
try:
   p.get('деньги',100)
except InvalidDataException:
    print(p)
