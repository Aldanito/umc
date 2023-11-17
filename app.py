from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from flask_mail import Mail
from flask_babel import Babel
from admin import init_admin
from config import config
import os
migrate = Migrate()
app = Flask(__name__)
app.config.from_object(config[os.getenv('FLASK_ENV', 'development')])
babel = Babel(app)
mail = Mail(app)  # instantiate the mail class
ckeditor = CKEditor(app)
db = SQLAlchemy(app)
migrate.init_app(app, db)
<<<<<<< HEAD
admin = Admin(app, template_mode='bootstrap4')



@app.route("/forward/<string:user>/<string:phone>", methods=['GET','POST'])
def move_forward(user,phone):
    conn = psycopg2.connect(
        host=,
        port='',
        database="",
        user='',
        password='')

    cursor = conn.cursor()
    sql = '''SELECT email from username'''
    cursor.execute(sql)
    rows = cursor.fetchall()
    emails = []
    for row in rows:
        emails.append("{0}".format(row[0]))
    print(emails)
    msg = Message(
                    'Заказ Звонка',
                    sender ='',
                    recipients = emails
                )
    msg.body = 'Поступил заказ от:\nКлиент:' +user +'\nНомер Телефона:' +phone +'\n'

    mail.send(msg)

    return redirect('/')

@app.route('/')
def index():
    session['logged_in'] = False
    session.clear()
    return render_template('index1.html')

    
class ImageView(ModelView):
    def is_accessible(self):
        if "logged_in" in session:  
            return True
        else:
            abort(403)
    form_overrides = dict(content=CKEditorField)
    create_template = 'edit.html'
    edit_template = 'edit.html'
    form_extra_fields = {
        'path': form.ImageUploadField('Image',
                                      base_path=file_path)
    }


class CertView(ModelView):
    def is_accessible(self):
        if "logged_in" in session:  
            return True
        else:
            abort(403)
    form_overrides = dict(content=CKEditorField)
    create_template = 'cert.html'
    edit_template = 'cert.html'
    form_extra_fields = {
        'path': form.ImageUploadField('Image',
                                      base_path=cert_path)
    }

class UserView(ModelView):
    def is_accessible(self):
        if "logged_in" in session:  
            return True
        else:
            abort(403)
    create_template = 'user_view.html'
    edit_template = 'user_view.html'


class User(db.Model):
    __tablename__ = 'username'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    email = db.Column(db.String)
    login = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(64))


class Post(db.Model):
    __tablename__ = "post1"
    id = db.Column(db.Integer, primary_key=True)
    title_en = db.Column(db.String(), unique=False, nullable=False)
    title_ru = db.Column(db.String(), unique=False, nullable=False)
    title_kz = db.Column(db.String(), unique=False, nullable=False)
    en = db.Column(db.Text(), nullable=False)
    ru = db.Column(db.Text(), nullable=False)
    kz = db.Column(db.Text(), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    path = db.Column(db.Unicode(128), nullable=False)


class Certificates(db.Model):
    __tablename__ = "cert"
    id = db.Column(db.Integer, primary_key=True)
    title_en = db.Column(db.String(), unique=False, nullable=False)
    title_ru = db.Column(db.String(), unique=False, nullable=False)
    title_kz = db.Column(db.String(), unique=False, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    path = db.Column(db.Unicode(128), nullable=False)


@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("username") == "admin" and  request.form.get("password") == "123456":
            session['logged_in'] = True
            return redirect("/admin")
        else:
            return render_template("login.html", failed = True)

    return render_template('login.html')


@app.route('/logout')
def logout():
    session['logged_in'] = False
    session.clear()
    return redirect('/login')


@app.route('/news/<string:lol>')
def newsstr():
    return redirect('/news/1')
    

@app.route('/news')
def news():
    return redirect('/news/1')


@app.route('/news/<int:page_num>')
def news_articles(page_num):
   
    news_articles = Post.query.order_by(Post.id.desc()).paginate(page=page_num, per_page=4, error_out = True)
    return render_template("news.html", news_articles=news_articles)

@app.route('/cert')
def cert():
    cert = Certificates.query.order_by(Certificates.id.desc())
    return render_template("cert_page.html", cert=cert)

@app.route('/news_page/<int:num>')
def news_page(num):
    if num:
        news_articles = Post.query.filter_by(id= num)
        return render_template('news_page.html',news_articles=news_articles)
    else:
        return abort(403)


@app.route('/files/<filename>')
def uploaded_files(filename,target):
    path = app.config['UPLOADED_PATH']  
    print(app.config['UPLOADED_PATH']+'/'+filename)  
    flash(f(app.config['UPLOADED_PATH']+'/'+filename), 'success')
    return send_from_directory(path, target.id)


@app.route('/upload', methods=['POST'])
def upload(target):
    f = request.files.get('upload')
    extension = f.filename.split('.')[-1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='Image only!')
    flash(f(app.config['UPLOADED_PATH']+'/'+f.filename), 'success')
    f.save(os.path.join(app.config['UPLOADED_PATH'], target.id))
    url = url_for('uploaded_files', filename=target.id)
    return upload_success(url=url)


@listens_for(Post, 'after_delete')
def del_image(target):
    if target.path:
        try:
            print(target.id)
            os.remove(op.join(file_path, target.path))
        except OSError:
            pass

@listens_for(Certificates, 'after_delete')
def del_image1(target):
    if target.path:
        try:
            print(target.id)
            print('Aldan'+" "+cert_path)
            os.remove(op.join(cert, target.path))
        except OSError:
            pass


admin.add_view(ImageView(Post, db.session, name='News'))
admin.add_view(CertView(Certificates, db.session, name='Certificates'))
admin.add_view(UserView(User, db.session, name='User'))
admin.add_link(MenuLink(name='Main page', endpoint='index'))
admin.add_link(MenuLink(name='Logout', endpoint='logout'))
=======
admin = init_admin(app, db)
>>>>>>> bab884bf6f34c0aa7aef5b44e696f405d95b1d7f

from routes import *

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
