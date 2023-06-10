from datetime import datetime
from pytz import timezone
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import Session
from yadisk import YaDisk
from db_models import optmobex_xiaomi_table, \
    optmobex_samsung_table, \
    optmobex_apple_table, \
    r_apple_table, \
    terra_apple_table

from config import hidden_vars

tables = {
    'optmobex_xiaomi': optmobex_xiaomi_table,
    'optmobex_samsung': optmobex_samsung_table,
    'optmobex_apple': optmobex_apple_table,
    'r_apple': r_apple_table,
    'terra_apple': terra_apple_table
}

y = YaDisk(token=hidden_vars.yadisk)
engine = create_engine(f'postgresql://'
                       f'{hidden_vars.postgresql_login}:{hidden_vars.postgresql_password}'
                       f'@{hidden_vars.postgresql_host}:{hidden_vars.postgresql_port}/'
                       f'{hidden_vars.postgres_db_name}', echo=False)


def check_data_in_db(date_: str, distributor_price_list: str):
    table = tables.get(distributor_price_list)
    with Session(bind=engine) as session:
        response = session.query(table).where(table.c.date == date_).first()
    return response


def write_into_db(distributor_price_list: str, price_list: list) -> None:
    table = tables.get(distributor_price_list)
    conn = engine.connect()
    conn.execute(insert(table), price_list)
    conn.commit()


def date_out(date: str) -> str:
    m_date = datetime.strptime(str(date), "%Y-%m-%d %H:%M:%S%z")
    tz = timezone("Etc/GMT-3")
    m_date_utc3 = tz.normalize(m_date.astimezone(tz))
    out_date = m_date_utc3.strftime("%Y-%m-%dT%H:%M")
    return out_date


def _profit(entry_price: int) -> int:
    price_range = [(0, 2000),  # 500
                   (2000, 7000),  # 1400
                   (7000, 10000),  # 1900
                   (10000, 15000),  # 2400
                   (15000, 20000),  # 2900
                   (20000, 30000),  # 3400
                   (30000, 50000),  # 3900
                   (50000, 100000),  # 5900
                   (100000, 3000000)]  # 8900
    profit = [500, 1400, 1900, 2400, 2900, 3400, 3900, 5900, 8900]
    for i in range(len(profit)):
        if entry_price in range(*price_range[i]):
            return entry_price + profit[i]

