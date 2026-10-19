const { MongoClient } = require("mongodb");

const cliente = new MongoClient("mongodb://127.0.0.1:27017");


async function main() {

    try {

        await cliente.connect();

        const libros = cliente
            .db("biblioteca")
            .collection("libros");


        const total = await libros.countDocuments();


        const disponibles = await libros.countDocuments({
            disponible: true
        });


        const prestados = await libros.countDocuments({
            disponible: false
        });


        const libroMasLargo = await libros.findOne(
            {},
            {
                sort: {
                    paginas: -1
                }
            }
        );


        console.log(
            "Número total de libros: " +
            total
        );

        console.log(
            "Libros disponibles: " +
            disponibles
        );

        console.log(
            "Libros prestados: " +
            prestados
        );

        console.log(
            "Libro con más páginas: " +
            libroMasLargo.titulo
        );


    } catch (error) {

        console.log("Error: " + error.message);

    } finally {

        await cliente.close();

    }

}


main();
