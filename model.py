from enum import unique
from re import U
from tokenize import PseudoExtras
from xml.dom.pulldom import PROCESSING_INSTRUCTION
from xmlrpc.client import Boolean, boolean
from utils.db import db
from sqlalchemy.types import Enum
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey,UniqueConstraint

class EnumRigidez(Enum):  
    one = 'Completo'
    two = 'Incompleto en progresión'
    three = 'en regresión'

class EnumEnf(Enum):  
    one = 'Completo'
    two = 'Incompleto'
   


class Usuarios(db.Model):
    id_u=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(100))
    apellido=db.Column(db.String(100))
    dni=db.Column(db.Integer)
    nbre_usuario=db.Column(db.String(50))    
    email=db.Column(db.String(60))
    passw=db.Column(db.String(50))
    UniqueConstraint(nombre)
    def __init__(self,nombre,apellido,dni,nbre_usuario,email,passw):
        self.nombre=nombre
        self.apellido=apellido
        self.passw=passw
        self.dni=dni
        self.email=email
        self.nbre_usuario=nbre_usuario
    def __repr__(self):
        return f'<user:{self.nbre_usuario}>'

class Expedientes(db.Model):
    id_e=db.Column(db.Integer, primary_key=True)
    nro_expediente=db.Column(db.Integer)
    fecha_e=db.Column(db.DateTime)
    nbre_e=db.Column(db.String(50))
    domicilio_lh=db.Column(db.String(100))    
    ubicacion=db.Column(db.String(600))
    localidad=db.Column(db.String(50))
    
    def __init__(self,nro_expediente,fecha_e,nbre_e,domicilio_lh,ubicacion,localidad):
        self.nro_expediente=nro_expediente
        self.fecha_e=fecha_e
        self.nbre_e=nbre_e
        self.domicilio_lh=domicilio_lh
        self.ubicacion=ubicacion
        self.localidad=localidad

    def getid(self):
        return self.id_e
class Medicos(db.Model):
    id_m=db.Column(db.Integer, primary_key=True)
    nro_matricula=db.Column(db.Integer)
        
    def __init__(self,nro_matricula):
        self.nro_matricula=nro_matricula

class Cadaveres(db.Model):
    id_c=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(100))
    fecha_ing=db.Column(db.Date)
    hora_ingr=db.Column(db.Time)
    fecha_nac=db.Column(db.Date)
    sexo=db.Column(db.String(50))
    temp_a=db.Column(db.Float)
    hora_temp_lh=db.Column(db.Time)
    posicion=db.Column(db.String(100))
    pupilas_reaccion=db.Column(db.String(50))
    peso=db.Column(db.Float)
    talla=db.Column(db.Float)
    domicilio_lh=db.Column(db.String(100))
    raza=db.Column(db.String(100))
    color_piel=db.Column(db.String(100))
    desarrollo_muscular=db.Column(db.String(100))
    
    def __init__(self,nombre,fecha_ing,hora_ingr,fecha_nac,sexo,temp_a,hora_temp_lh,posicion,pupilas_reaccion,
    peso,talla, domicilio_lh,raza,color_piel,desarrollo_muscular):
        self.nombre=nombre
        self.fecha_ing=fecha_ing
        self.fecha_nac=fecha_nac
        self.hora_ingr=hora_ingr
        self.sexo=sexo
        self.temp_a=temp_a
        self.hora_temp_lh=hora_temp_lh
        self.talla=talla
        self.posicion=posicion
        self.pupilas_reaccion=pupilas_reaccion
        self.peso=peso
        self.color_piel=color_piel
        self.desarrollo_muscular=desarrollo_muscular
        self.domicilio_lh=domicilio_lh
        self.raza=raza

    def getnbre(self):
        return self.nombre


class Autopsias(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nro_legajo=db.Column(db.Integer)
    anio=db.Column(db.Integer)
    fecha_inic=db.Column(db.Date)
    hora_inic=db.Column(db.Time)    
    temp_a=db.Column(db.Float)
    temp_r=db.Column(db.Float)
    enfriamiento = db.Column(Enum('Completo','Incompleto'))
    espasmos=db.Column(db.Boolean)
    rigidez=db.Column(Enum( 'Completo','Incompleto en progresión','en regresión'))
    rigidez_hasta=db.Column(db.String(100))
    rigidez_vencida=db.Column(db.String(100))
    livideces=db.Column(db.Boolean)
    color_iris=db.Column(db.String(100))
    conjuntivas=db.Column(db.String(100))
    cornea=db.Column(db.String(100))
    pupilas=db.Column(db.String(100))
    id_expediente =db.Column(db.Integer, db.ForeignKey(Expedientes.id_e))    
    id_cadaver=db.Column(db.Integer, db.ForeignKey(Cadaveres.id_c)) 
    id_medico=db.Column(db.Integer, db.ForeignKey(Medicos.id_m)) 
    
    def __init__(self,nro_legajo,anio,fecha_inic,temp_a,temp_r,enfriamiento,espasmos,rigidez,rigidez_hasta,rigidez_vencida,livideces,
    color_iris,conjuntivas,cornea,pupilas):
        self.nro_legajo=nro_legajo
        self.anio=anio
        self.fecha_inic=fecha_inic
        self.temp_a=temp_a
        self.temp_r=temp_r
        self.enfriamiento=enfriamiento
        self.espasmos=espasmos
        self.rigidez=rigidez
        self.rigidez_hasta=rigidez_hasta
        self.rigidez_vencida=rigidez_vencida
        self.color_iris=color_iris
        self.conjuntivas=conjuntivas
        self.cornea=cornea
        self.pupilas=pupilas




