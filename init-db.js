db = db.getSiblingDB("oep_db");
db.products_tb.drop();

db.products_tb.insertMany([
    {
        "id": 1,
        "name": "Product 1"
    },
    {
        "id": 2,
        "name": "Product 2"
    },
    {
        "id": 3,
        "name": "Product 3"
    },
]);