from typing import Optional

from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


# PASO 1 - Conectar con la base de datos

engine = create_engine("sqlite:///biblioteca.db")


# PASO 2 - Crear la clase Base

class Base(DeclarativeBase):
    pass


# PASO 3 - Definir la clase Libro con sus anotaciones

class Libro(Base):
    __tablename__ = "libros"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str]
    autor: Mapped[str]
    paginas: Mapped[Optional[int]]


# PASO 4 - Crear la tabla

Base.metadata.create_all(engine)


with Session(engine) as session:

    # PASO 5 - Guardar los tres libros

    session.add(Libro(titulo="Don Quijote de la Mancha", autor="Miguel de Cervantes", paginas=1250))
    session.add(Libro(titulo="La casa de los espíritus", autor="Isabel Allende", paginas=480))
    session.add(Libro(titulo="Platero y yo", autor="Juan Ramón Jiménez"))
    session.commit()


    # PASO 6 - Consultar los libros

    libro = session.get(Libro, 1)
    print(libro.titulo, "-", libro.autor)

    consulta = select(Libro).where(Libro.paginas > 400)

    for libro in session.scalars(consulta):
        print(libro.titulo, libro.paginas)


    # PASO 7 - Actualizar un libro

    platero = session.get(Libro, 3)
    platero.paginas = 150
    session.commit()


    # PASO 8 - Eliminar un libro

    casa = session.get(Libro, 2)
    session.delete(casa)
    session.commit()


    # PASO 9 - Mostrar el estado final

    for libro in session.scalars(select(Libro)):
        print(libro.id, libro.titulo, libro.paginas)
