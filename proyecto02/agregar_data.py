from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import enlace

engine = create_engine(enlace)

from app import Docente

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objetos de tipo Docente
docente1 = Docente(nombre="Tony", placa="SGH-0306", \
        anio="2005", costo="300")

docente2 = Docente(nombre="Luis", placa="SLP-0201", \
        anio="2003", costo="200")

docente3 = Docente(nombre="Ana", placa="SIO-0214", \
        anio="2000", costo="100")

docente4 = Docente(nombre="Monica", placa="LJK-0201", \
        anio="2001", costo="100")

# se agrega los objetos
# a la sesión
# a la espera de un commit
# para agregar un registro a la base de
# datos
session.add(docente1)
session.add(docente2)
session.add(docente3)
session.add(docente4)

# se confirma las transacciones
session.commit()
