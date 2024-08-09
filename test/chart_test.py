# This is the "app/chart_test.py" file

from pandas import DataFrame

from app.chart import email_table

def test_data_fecthing():
    assert isinstance(email_table, DataFrame)
    assert len(email_table) == 20
    assert email_table.columns.tolist() == ["keyword","impression","like","share","comment"]




