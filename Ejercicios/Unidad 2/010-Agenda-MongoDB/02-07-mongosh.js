// PARTE A · Ejercicios 2 a 7
// Ejecutar dentro de mongosh, en este orden.

// EJERCICIO 2
use agenda

db.contactos.insertOne({
    nombre: "Ana López",
    telefono: "600111222",
    ciudad: "Valencia"
})

db.contactos.find()

// EJERCICIO 3
db.contactos.insertMany([
    {
        nombre: "Luis Martín",
        telefono: "600333444",
        ciudad: "Madrid"
    },
    {
        nombre: "Marta Ruiz",
        telefono: "600555666",
        ciudad: "Valencia"
    },
    {
        nombre: "Pedro Gómez",
        telefono: "600777888",
        ciudad: "Sevilla"
    },
    {
        nombre: "Lucía Sanz",
        telefono: "600999000",
        ciudad: "Barcelona"
    }
])

// EJERCICIO 4
db.contactos.find()

db.contactos.countDocuments()

// EJERCICIO 5
db.contactos.find({ ciudad: "Valencia" })

db.contactos.find(
    {
        ciudad: "Valencia"
    },
    {
        nombre: 1,
        telefono: 1,
        _id: 0
    }
)

// EJERCICIO 6
db.contactos.updateOne(
    {
        nombre: "Luis Martín"
    },
    {
        $set: {
            telefono: "611222333"
        }
    }
)

db.contactos.findOne({ nombre: "Luis Martín" })

// EJERCICIO 7
db.contactos.deleteOne({
    nombre: "Pedro Gómez"
})

db.contactos.countDocuments()

db.contactos.find(
    {},
    {
        nombre: 1,
        _id: 0
    }
)

exit
