import datetime
import logging


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        total = 0
        for item in self.records:
            if str(datetime.date.today()) == item.date:
                total += item.amount
            else:
                break

        return total

    def get_week_stats(self):
        total = 0
        for wd in range(7):
            for item in self.records:
                if str((datetime.date.today() - datetime.timedelta(days=wd)).date()) == item.date:
                    total += item.amount
                else:
                    break
        return total


class CaloriesCalculator(Calculator):

    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        received = self.get_today_stats()
        if received < self.limit:
            logging.warning(f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit - received} кКал")
        else:
            logging.info("Хватит есть!")


class CashCalculator(Calculator):

    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        b={
         'EUR': 152,
         "USD":180,
        'RUB':160
        }
        for i in b:
            b[i] = round(b[i]/b["RUB"], 2)
        logging.debug(b)
        remaining = self.limit - self.get_today_stats()
        if remaining < 0:
            return 0
        return round(remaining/b[currency],2)


class Record:

    def __init__(self, amount=0, date=datetime.date.today(), comment=""):
        self.amount = amount
        self.date = date
        self.comment = comment


if __name__ == "__main__":
    cash_calculator = CashCalculator(2000)
    cash_calculator.add_record(Record(amount=150, comment="123"))
    cash_calculator.add_record(Record(amount=150, comment="123"))
    cash_calculator.add_record(Record(amount=150, comment="2022-01-18"))
    print(cash_calculator.get_today_cash_remained('RUB'))

    calorie_calculator = CaloriesCalculator(2000)
    calorie_calculator.add_record(Record(amount=150, comment="123"))
    calorie_calculator.add_record(Record(amount=1999, comment="123"))
    calorie_calculator.add_record(Record(amount=150, comment="2022-01-18"))
    logging.info(calorie_calculator.get_calories_remained())
