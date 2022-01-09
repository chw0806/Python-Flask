from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User, Company, UsertoCompany
from sqlalchemy.orm import scoped_session
from sqlalchemy.sql import text
engine = create_engine("mysql+pymysql://root:137629122@127.0.0.1:3306/flask?charset=utf8", max_overflow=0, pool_size=5)

Session = sessionmaker(bind=engine)

session=Session()

# add
# objs = [User(name='chwgg', password='12343'),
#         Company(name='apple'),
# User(name='gg', password='12343')
#         ]
# session.add_all(objs)

# delete
# res = session.query(User).filter_by(name='ccc').delete()

# update
# res = session.query(User).filter(User.id > 0).update({User.name:'ccc'})

# read
res = session.query(Company).filter(Company.id > 0).all()
for item in res:
    print(item.id, item.name, item.company_data)


session.commit()
# 并没有真正关闭连接，而是放回池中
session.close()