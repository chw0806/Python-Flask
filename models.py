import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
import hashlib


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), index=True, unique=True, nullable=False)
    password = Column(String(32), nullable=False)


class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), index=True, unique=True, nullable=True)
    encoded = str(id).encode()
    result = hashlib.sha256(encoded)
    company_data = Column(String(64), default=result.hexdigest())

#many to many
class UsertoCompany(Base):

    __tablename__ = 'usertocompany'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id=Column(Integer, ForeignKey('users.id'))
    company_id=Column(Integer, ForeignKey('company.id'))



def create_table():
    # 创建engine对象
    engine = create_engine(
        "mysql+pymysql://root:137629122@127.0.0.1:3306/flask?charset=utf8",
        max_overflow=0,
        pool_size=5,
        pool_timeout=30,
        pool_recycle=-1
    )

    Base.metadata.create_all(engine)

def drop_table():

    engine = create_engine(
        "mysql+pymysql://root:137629122@127.0.0.1:3306/flask?charset=utf8",
        max_overflow=0,
        pool_size=5,
        pool_timeout=30,
        pool_recycle=-1
    )

    Base.metadata.drop_all(engine)

if __name__ == '__main__':
    create_table()  # 原来已经存在user表，再执行一次不会有问题
    #drop_table()

