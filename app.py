from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail
from write_excel import write_excel

app = Flask(__name__)

ENV = "dev"

if ENV =='dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:Fastlife33@localhost/python-web-app'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI']= ''

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Pesa(db.Model):
    __tablename__ = 'pesa'
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime)
    region = db.Column(db.String(30))
    site_name = db.Column(db.String(30))
    site_number = db.Column(db.Integer)
    type = db.Column(db.String(30))
    address = db.Column(db.String(30))
    city = db.Column(db.String(30))
    county = db.Column(db.String(30))
    state = db.Column(db.String(30))
    zip_code = db.Column(db.Integer)

    s_power_system_b = db.Column(db.String(30))
    s_rects_conv_b = db.Column(db.String(30))
    s_load_cap_b = db.Column(db.String(30))
    s_load_current_b = db.Column(db.String(30))
    s_dist_b = db.Column(db.String(30))
    b_power_system_b = db.Column(db.String(30))
    b_rects_conv_b = db.Column(db.String(30))
    b_load_cap_b = db.Column(db.String(30))
    b_load_current_b = db.Column(db.String(30))
    b_dist_b = db.Column(db.String(30))
  
    s_power_system_a = db.Column(db.String(30))
    s_rects_conv_a = db.Column(db.String(30))
    s_load_cap_a = db.Column(db.String(30))
    s_load_current_a = db.Column(db.String(30))
    s_dist_a = db.Column(db.String(30))
    b_power_system_a = db.Column(db.String(30))
    b_rects_conv_a = db.Column(db.String(30))
    b_load_cap_a = db.Column(db.String(30))
    b_load_current_a = db.Column(db.String(30))
    b_dist_a = db.Column(db.String(30))
    s_load_current_a = db.Column(db.String(30))

    manufacturer_b = db.Column(db.String(30))
    type_model_b = db.Column(db.String(30))
    Sulf_gel_b = db.Column(db.String(30))
    batteries_b = db.Column(db.String(30))
    cells_b = db.Column(db.String(30))
    runtime_b = db.Column(db.DateTime)

    manufacturer_a = db.Column(db.String(30))
    type_model_a = db.Column(db.String(30))
    Sulf_gel_a = db.Column(db.String(30))
    batteries_a = db.Column(db.String(30))
    cells_a = db.Column(db.String(30))
    runtime_a = db.Column(db.DateTime)


    def __init__(self, installer, date, region, site_name, site_number, type, address, city, county, state, zip_code, s_power_system_b, s_rects_conv_b, s_load_cap_b, s_load_current_b, s_dist_b, b_power_system_b, b_rects_conv_b, b_load_cap_b, b_load_current_b, b_dist_b, s_power_system_a, s_rects_conv_a, s_load_cap_a, s_load_current_a, s_dist_a, b_power_system_a, b_rects_conv_a, b_load_cap_a, b_load_current_a, b_dist_a, manufacturer_b, type_model_b, Sulf_gel_b, batteries_b, cells_b, runtime_b, manufacturer_a, type_model_a, Sulf_gel_a, batteries_a, cells_a, runtime_a):
        self.intaller = installer
        self.date = date
        self.region = region
        self.site_name = site_name
        self.site_number = site_number
        self.type = type
        self.address = address
        self.city = city
        self.county = county
        self.state = state
        self.zip_code = zip_code

        self.s_power_system_b = s_power_system_b
        self.s_rects_conv_b = s_rects_conv_b
        self.s_load_cap_b = s_load_cap_b
        self.s_load_current_b = s_load_current_b
        self.s_dist_b = s_dist_b
        self.b_power_system_b = b_power_system_b
        self.b_rects_conv_b = b_rects_conv_b
        self.b_load_cap_b = b_load_cap_b
        self.b_load_current_b = b_load_current_b
        self.b_dist_b = b_dist_b

        self.s_power_system_a = s_power_system_a
        self.s_rects_conv_a = s_rects_conv_a
        self.s_load_cap_a = s_load_cap_a
        self.s_load_current_a = s_load_current_a
        self.s_dist_a = s_dist_a
        self.b_power_system_a = b_power_system_a
        self.b_rects_conv_a = b_rects_conv_a
        self.b_load_cap_a = b_load_cap_a
        self.b_load_current_a = b_load_current_a
        self.b_dist_a = b_dist_a

        self.manufacturer_b = manufacturer_b
        self.type_model_b = type_model_b
        self.Sulf_gel_b = Sulf_gel_b
        self.batteries_b = batteries_b
        self.cells_b = cells_b
        self.runtime = runtime_b

        self.manufacturer_a = manufacturer_a
        self.type_model_a = type_model_a
        self.Sulf_gel_a = Sulf_gel_a
        self.batteries_a = batteries_a
        self.cells_a = cells_a
        self.runtime_a = runtime_a

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    if request.method =='POST':
        installer = request.form['installer']
        date = request.form['date']
        region = request.form['region']
        site_name = request.form['site name']
        site_number = request.form['site number']
        type = request.form['type']
        address = request.form['address']
        city = request.form['city']
        county = request.form['county']
        state = request.form['state']
        zip_code = request.form['zip code']

        s_power_system_b = request.form['24v power system b']
        s_rects_conv_b = request.form['q&s of rects/conv 24 b']
        s_load_cap_b = request.form['t 24v load cap b']
        s_load_current_b = request.form['e 24v load current b']
        s_dist_b = request.form['avail 24v dist b']
        b_power_system_b = request.form['48v power system model b']
        b_rects_conv_b = request.form['q&s of rects/conv 48 b']
        b_load_cap_b = request.form['t 48v load cap b']
        b_load_current_b = request.form['e 48v load current b']
        b_dist_b = request.form['avail 48v dist b']

        s_power_system_a = request.form['24v power system b']
        s_rects_conv_a = request.form['q&s of rects/conv 24 b']
        s_load_cap_a = request.form['t 24v load cap b']
        s_load_current_a = request.form['e 24v load current b']
        s_dist_a = request.form['avail 24v dist b']
        b_power_system_a = request.form['48v power system model b']
        b_rects_conv_a = request.form['q&s of rects/conv 48 b']
        b_load_cap_a = request.form['t 48v load cap b']
        b_load_current_a = request.form['e 48v load current b']
        b_dist_a = request.form['avail 48v dist b']

        manufacturer_b = request.form['manufacturer b']
        type_model_b = request.form['type/model b']
        Sulf_gel_b = request.form['sulfuric or gel type b']
        batteries_b = request.form['# of batteries b']
        cells_b = request.form['# of cells b']
        runtime_b = request.form['Run time b']

        manufacturer_a = request.form['manufacturer a']
        type_model_a = request.form['type/model a']
        Sulf_gel_a = request.form['sulfuric or gel type a']
        batteries_a = request.form['# of batteries a']
        cells_a = request.form['# of cells a']
        runtime_a = request.form['Run time a']

        data = Pesa(installer, date, region, site_name, site_number, type, address, city, county, state, zip_code, s_power_system_b, s_rects_conv_b, s_load_cap_b, s_load_current_b, s_dist_b, b_power_system_b, b_rects_conv_b, b_load_cap_b, b_load_current_b, b_dist_b, s_power_system_a, s_rects_conv_a, s_load_cap_a, s_load_current_a, s_dist_a, b_power_system_a, b_rects_conv_a, b_load_cap_a, b_load_current_a, b_dist_a, manufacturer_b, type_model_b, Sulf_gel_b, batteries_b, cells_b, runtime_b, manufacturer_a, type_model_a, Sulf_gel_a, batteries_a, cells_a, runtime_a)

        db.session.add(data)
        send_mail(installer, date, region, site_name, site_number, type,address,city, county, state, zip_code, s_power_system_b, s_rects_conv_b, s_load_cap_b, s_load_current_b, s_dist_b, b_power_system_b, b_rects_conv_b, b_load_cap_b, b_load_current_b, b_dist_b, s_power_system_a, s_rects_conv_a, s_load_cap_a, s_load_current_a, s_dist_a, b_power_system_a, b_rects_conv_a, b_load_cap_a, b_load_current_a, b_dist_a, manufacturer_b, type_model_b, Sulf_gel_b, batteries_b, cells_b, runtime_b, manufacturer_a, type_model_a, Sulf_gel_a, batteries_a, cells_a, runtime_a)
        write_excel(date, region, site_name, site_number, type,address,city, county, state, zip_code, s_power_system_b, s_rects_conv_b, s_load_cap_b, s_load_current_b, s_dist_b, b_power_system_b, b_rects_conv_b, b_load_cap_b, b_load_current_b, b_dist_b, s_power_system_a, s_rects_conv_a, s_load_cap_a, s_load_current_a, s_dist_a, b_power_system_a, b_rects_conv_a, b_load_cap_a, b_load_current_a, b_dist_a, manufacturer_b, type_model_b, Sulf_gel_b, batteries_b, cells_b, runtime_b, manufacturer_a, type_model_a, Sulf_gel_a, batteries_a, cells_a, runtime_a)
        db.session.commit()

        return render_template('success.html')

if __name__ == '__main__':
   
    app.run()