import hashlib

from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import or_, and_, not_

from models import User
from exts import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        if password == repassword:

            user = User()
            user.username = username
            user.password = password
            user.phone = phone

            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.user_center'))

    return render_template('user/register.html')


# user center
@user_bp.route('/')
def user_center():
    # 查询数据库中的数据
    users = User.query.filter(User.isdelete == False).all()  # select * from user;
    print(users)  # [user_objA,user_objB,....]
    return render_template('user/center.html', users=users)



@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # select * from user where username='xxxx';

        # 查询
        user_list = User.query.filter_by(username=username)

        for u in user_list:
            if u.password == password:
                return 'login success！'
        else:
            return render_template('user/login.html', msg='username or password are wrong！')

    return render_template('user/login.html')


@user_bp.route('/search')
def search():
    keyword = request.args.get('search')  # name or phone are both ok
    user_list = User.query.filter(or_(User.username.contains(keyword), User.phone.contains(keyword))).all()
    return render_template('user/center.html', users=user_list)

@user_bp.route('/delete', endpoint='delete')
def user_delete():
    id = request.args.get('id')
    #
    # # get id for this user
    # user = User.query.get(id)
    # user.isdelete = True
    # db.session.commit()
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('user.user_center'))

@user_bp.route('/update', endpoint='update', methods=['GET', 'POST'])
def user_update():
    if request.method == 'POST':
        username = request.form.get('username')
        phone = request.form.get('phone')
        id = request.form.get('id')

        user = User.query.get(id)
        user.phone = phone
        user.username = username
        db.session.commit()
        return redirect(url_for('user.user_center'))
    else:
        id = request.args.get('id')
        user = User.query.get(id)
        return render_template('user/update.html', user=user)


@user_bp.route('/test')
def test():
    username = request.args.get('username')
    user = User.query.filter_by(username=username).first()
    print(user.username, user.rdatetime)

    user = User.query.filter_by(username=username).last()
    print(user.username, user.rdatetime)
    return 'test'


@user_bp.route('/select')
def user_select():
    user = User.query.get(2)
    # user1 = User.query.filter(User.username == 'chw').all()  # all(), first()
    # user_list = User.query.filter(User.username.like('z%')).all()  # select * from user where username like 'z%';

    # user_list = User.query.filter(not_(User.username.contains('i'))).all()
    # user_list = User.query.filter(User.phone.in_(['15810106788','13801011299'])).all()
    # # user_list = User.query.order_by(-User.id).all()


    # user_list = User.query.limit(2).all()
    user_list = User.query.offset(4).limit(2).all()
    return render_template('user/select.html', user=user, users=user_list)

