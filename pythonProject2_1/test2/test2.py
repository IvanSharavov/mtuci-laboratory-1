from main import  CaloriesCalculator,Record

def test_week_calc():
    cal_calculator = CaloriesCalculator(1000)
    cal_calculator.add_record(Record(amount= 150, comment="123"))
    cal_calculator.add_record(Record(amount= 160, comment="123"))
    cal_calculator.add_record(Record(amount= 150, date="2022-02-18"))
    cal_calculator.add_record(Record(amount=1999, date="2022-01-16"))
    assert cal_calculator.get_week_stats()==560;
