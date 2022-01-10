from datetime import datetime

from exts import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(11), unique=True)
    isdelete = db.Column(db.Boolean, default=False)
    rdatetime = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.username

# class Company(Base):
#     __tablename__ = 'company'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(32), index=True, unique=True, nullable=True)
#     encoded = str(id).encode()
#     result = hashlib.sha256(encoded)
#     company_data = Column(String(64), default=result.hexdigest())
#
# #many to many
# class UsertoCompany(Base):
#
#     __tablename__ = 'usertocompany'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id=Column(Integer, ForeignKey('users.id'))
#     company_id=Column(Integer, ForeignKey('company.id'))



