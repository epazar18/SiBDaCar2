from operator import index
from tkinter import E
from django.forms import ValidationError
from flask import Flask, render_template,request,session,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer
from utils.db import db
from model import  Usuarios,Medicos,Expedientes,Cadaveres,Autopsias,expediente_cadaver
from flask_login import LoginManager
app = Flask(__name__)

app.secret_key='root'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/forenses'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
SQLAlchemy(app)



# Routes to Render Something
@app.route('/')
def index():    
    return render_template("index.html")

@app.route('/estimar')
def estimar(): 
    #profiles=Cadaveres.query.all()
    result=Expedientes.query.filter(Expedientes.nro_expediente==123).first()
    id_expediente=result.getid()
    profiles = db.session.query(Cadaveres).filter(expediente_cadaver.id_e==id_expediente, Cadaveres.id_c==expediente_cadaver.id_c).all()
    print ("consults ",profiles)
    for dat in profiles:
        print("nomrbes ",dat.getnbre())
    return render_template("estimar.html",profiles=profiles)     
   

@app.route('/home', strict_slashes=False)
def home():
    return render_template("home.html")

@app.route('/expedientes', strict_slashes=False)
def expedientes():
    return render_template("expedientes.html")

@app.route('/NuevaAutopsia', strict_slashes=False)
def NuevaAutopsia():
    result=Expedientes.query.filter(Expedientes.nro_expediente==123).first()
    id_expediente=result.getid()
    profiles = db.session.query(Cadaveres).filter(expediente_cadaver.id_e==id_expediente, Cadaveres.id_c==expediente_cadaver.id_c).all()
   
    return render_template("newAutopsia.html",profiles=profiles) 

@app.route('/IngresoCadaver', methods=['POST'])
def IngresoCadaver():
   
   if request.method=='POST':
       # apellido=request.form.get('apellido')   
        nbre= request.form.get('nbre')
        print(nbre)  
        fechaIng=request.form.get('fechaIng')
        hora=request.form.get('hora')
        fechaNac=request.form.get('fechaNac')
        sexo=request.form.get('sexo')
        temp_a=request.form.get('tempAmLH')
        hora_temp_lh=request.form.get('horaTempLH')
        posicion=request.form.get('posicion')
        pupilas_reaccion=request.form.get('pupilas')
        peso=request.form.get('peso')
        talla=request.form.get('talla')
        domicilio_lh="pp"
        raza=request.form.get('raza')
        color_piel=request.form.get('colorPiel')
        desarrollo_muscular=request.form.get('desMuscular')
        nuevo_cadaver=Cadaveres(nbre,"2020-12-12",	"00:12:12",	"1998-05-12",	"Femenino",	"15",	"12",	"acostada",	"pp_",	"20",	"25",	"pp",
        "kk","ll","dd")       
        db.session.add(nuevo_cadaver)
        db.session.commit()  
        return redirect(url_for('NuevoCadaver'))


@app.route('/IngresoExpediente', methods=['POST'])
def IngresoExpediente():
   if request.method=='POST':
        nro_e=request.form.get('nro_e')   
        nbre_e=request.form.get('nbre_e')
        fecha=request.form.get('fecha_e')
        direccion=request.form.get('dire')
        localidad=request.form.get('ciudad')
        ubicacion=request.form.get('ubicacion')
        nuevo_expediente=Expedientes(nro_e,fecha,nbre_e,direccion,ubicacion,localidad)       
        db.session.add(nuevo_expediente)
        db.session.commit()  
        return redirect(url_for('NuevoExpediente'))

@app.route('/NuevoExpediente', strict_slashes=False)
def NuevoExpediente():   
    return render_template("newExpediente.html")
    

@app.route('/NuevoCadaver', strict_slashes=False)
def NuevoCadaver():
    return render_template("newCadaver.html")
    
@app.route('/login',methods=['POST'])
def login():    
    if request.method=='POST':
        session.pop('user_id',None)
        usuario_nbre=request.form['usuario']
        passw=request.form['password']   
        user = Usuarios.query.filter_by(nbre_usuario=usuario_nbre).first()
       # user =[x for x in usuarios if x.nbre_usuario==usuario_nbre][0]
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not user.passw==passw:
       
        return redirect(url_for('index'))
    
    return redirect(url_for('home'))
  

@app.route('/registro',methods=['POST'])
def registro():
    nbre=request.form.get('new_nbre')   
    usuario=request.form.get('usuario')
    dni=request.form.get('new_dni')
    apellido=request.form.get('new_apelllido')
    email=request.form.get('new_email')
    clave=request.form.get('new_clave')
    nro_m=(request.form.get('nroM'))
  
    nuevo_usuario=Usuarios(nbre,apellido,dni,usuario,email,clave,)
    nuevo_medico=Medicos(nro_m)
    db.session.add(nuevo_usuario)
    db.session.add(nuevo_medico)
    db.session.commit()
    return redirect(url_for('index'))

with app.app_context():
    db.create_all()

# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)