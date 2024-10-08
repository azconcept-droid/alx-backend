const express = require('express');

const app = express()

const listProducts = [
    {
        id: 1,
        name: 'Suitcase 250',
        price: 50,
        stock: 4
    },
    {
        id: 2,
        name: 'Suitcase 450',
        price: 100,
        stock: 10
    },
    {
        id: 3,
        name: 'Suitcase 650',
        price: 350,
        stock: 2
    },
    {
        id: 4,
        name: 'Suitcase 1050',
        price: 550,
        stock: 5
    },
]

function getItemById(id) {
    listProducts.forEach((product) => {
        if (product.id === id){
            return product;
        }
    }) 
}

app.get('/list_products', (req, res)=>{
    const list_products = [];
    let i = 0;

    listProducts.forEach((product) => {

        list_products[i]['itemId'] = product.id
        list_products[i]['itemName'] = product.name
        list_products[i]['price'] = product.price
        list_products[i]['initialAvailableQuantity'] = 10

        i = i + 1
    })

    res.json(list_products);
})

app.listen(1245, () => {
    console.log('app running on port 1245')
})