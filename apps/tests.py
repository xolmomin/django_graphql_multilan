from django.test import TestCase

# Create your tests here.


'''

mutation nimadir {
  deleteProduct(id: 10) {
    product {
      id
    }
  }
}


mutation UpdateProduct {
  updateProduct(productData: {id:5, name:"body", description: "gfdd", price: 37400, categoryId: 2}){
    product{
      id,
      name,
      description,
      price,
      category{
        name
      }
    }
  }
}


query {
  category(id:1){
    id, name, productSet{
      name, description
    }
  }
}



mutation UpdateProduct {
  updateProduct(productData: {id:12, name:"Product 12", description: "zor tovar", price: 37400, categoryId: 2}){
    product{
      id,
      name,
      description,
      price,
      category{
        id,
        name
      }
    }
  }
}


mutation CreateProduct {
  createProduct(productData: {name:"Product 5", description: "Description 1", price: 18000.00, categoryId: 15}){
    product{
      id,
      name,
      description,
      price,
      category{
        id
      }
    }
  }
}


mutation CreateProduct {
  createProduct(productData: {name:"Product 1", description: "Description 1", price: 18000.00}){
    product{
      name,
      description,
      price
    }
  }
}



query {
  categories{
    id,
    name,
    createdAt,
    productSet {
      id,
      name
    }
  }
}

'''