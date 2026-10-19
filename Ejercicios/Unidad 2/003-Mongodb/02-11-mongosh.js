// PARTE A · Ejercicios 2 a 11
// Ejecutar dentro de mongosh, en este orden.

// EJERCICIO 2
use biblioteca

db.libros.insertOne({
    titulo: "El Quijote",
    autor: "Miguel de Cervantes",
    anio: 1605,
    genero: "novela",
    paginas: 1250,
    disponible: true
})

db.libros.find()

// EJERCICIO 3
db.libros.insertMany([
    {
        titulo: "Cien años de soledad",
        autor: "Gabriel García Márquez",
        anio: 1967,
        genero: "novela",
        paginas: 471,
        disponible: true
    },
    {
        titulo: "La sombra del viento",
        autor: "Carlos Ruiz Zafón",
        anio: 2001,
        genero: "misterio",
        paginas: 576,
        disponible: true
    },
    {
        titulo: "El principito",
        autor: "Antoine de Saint-Exupéry",
        anio: 1943,
        genero: "infantil",
        paginas: 96,
        disponible: true
    },
    {
        titulo: "Patria",
        autor: "Fernando Aramburu",
        anio: 2016,
        genero: "novela",
        paginas: 648,
        disponible: true
    },
    {
        titulo: "Harry Potter y la piedra filosofal",
        autor: "J. K. Rowling",
        anio: 1997,
        genero: "fantasía",
        paginas: 256,
        disponible: true
    }
])

db.libros.find()

// EJERCICIO 4
db.libros.countDocuments()

// EJERCICIO 5
db.libros.find({ genero: "novela" })

// EJERCICIO 6
db.libros.find({ anio: { $gt: 2000 } })

// EJERCICIO 7
db.libros.find(
    {},
    {
        titulo: 1,
        autor: 1,
        _id: 0
    }
).sort({ anio: 1 })

// EJERCICIO 8
db.libros.find(
    {
        paginas: { $lt: 300 }
    },
    {
        titulo: 1,
        paginas: 1,
        _id: 0
    }
)

// EJERCICIO 9
db.libros.updateOne(
    {
        titulo: "El principito"
    },
    {
        $set: {
            disponible: false
        }
    }
)

db.libros.find({ disponible: false })

// EJERCICIO 10
db.libros.updateMany(
    {},
    {
        $set: {
            ejemplares: 1
        }
    }
)

db.libros.updateOne(
    {
        titulo: "El Quijote"
    },
    {
        $inc: {
            ejemplares: 2
        }
    }
)

db.libros.find({ titulo: "El Quijote" })

// EJERCICIO 11
db.libros.deleteOne({
    titulo: "Harry Potter y la piedra filosofal"
})

db.libros.countDocuments()
