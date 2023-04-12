db = db.getSiblingDB("oep_db");
db.products_tb.drop();

db.products_tb.insertMany([
    {
        "name": "Product 1"
    },
    {
        "name": "Product 2"
    },
    {
        "name": "Product 3"
    },
]);