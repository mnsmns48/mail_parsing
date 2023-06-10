from sqlalchemy import MetaData, Table, Column, VARCHAR, Integer

metadata = MetaData()
optmobex_xiaomi_table = Table('optmobex_xiaomi', metadata,
                              Column('date', VARCHAR),
                              Column('product', VARCHAR),
                              Column('enter_cost', Integer),
                              Column('out_cost', Integer),
                              )
optmobex_samsung_table = Table('optmobex_samsung', metadata,
                               Column('date', VARCHAR),
                               Column('product', VARCHAR),
                               Column('enter_cost', Integer),
                               Column('out_cost', Integer),
                               )
optmobex_apple_table = Table('optmobex_apple', metadata,
                             Column('date', VARCHAR),
                             Column('product', VARCHAR),
                             Column('enter_cost', Integer),
                             Column('out_cost', Integer),
                             )
r_apple_table = Table('r_apple', metadata,
                      Column('date', VARCHAR),
                      Column('product', VARCHAR),
                      Column('enter_cost', Integer),
                      Column('out_cost', Integer),
                      )
terra_apple_table = Table('terra_apple', metadata,
                          Column('date', VARCHAR),
                          Column('product', VARCHAR),
                          Column('enter_cost', Integer),
                          Column('out_cost', Integer),
                          )
