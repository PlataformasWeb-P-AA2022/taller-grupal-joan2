from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import enlace

engine = create_engine(enlace)

from app import Matriculas

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objetos de tipo Docente
cliente1 = Matriculas(nombre="Tony", placa="123-ASD", \
        anoMatricula= 2012, costo = 2000)

cliente2 = Matriculas(nombre="Andres", placa="1453-ASJ", \
        anoMatricula= 2017, costo = 42000)

cliente3 = Matriculas(nombre="Carlos", placa="1223-TSD", \
        anoMatricula= 2022, costo = 3400)

cliente4 = Matriculas(nombre="Jhoselin", placa="0123-ESD", \
        anoMatricula= 2021, costo = 2300)

# se agrega los objetos
# a la sesión
# a la espera de un commit
# para agregar un registro a la base de
# datos
session.add(cliente1)
session.add(cliente2)
session.add(cliente3)
session.add(cliente4)

# se confirma las transacciones
session.commit()
