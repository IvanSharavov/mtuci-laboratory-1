from main import  CashCalculator,Record

def test_day_calc():
 cash_calculator=CashCalculator(2000)
 cash_calculator.add_record(Record(amount=160, comment="123"))
 result = cash_calculator.get_today_cash_remined('RUB')
 assert result == 820.0



