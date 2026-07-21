"""
Stores all menu items available at Pizza Corner, including pizzas,
sides, beverages, and the customer cart.

Each category is stored as a dictionary where the key represents
the menu option number, and the value contains the item's name,
description, and price.
"""

cart = []  # Currently, the cart is empty

pizza_options = {
   
    1: {
        "name": "Classic Margherita",
        "description": "Classic pizza topped with mozzarella cheese, tomato sauce, and fresh basil",
        "price": 150,
    },

    2: {
        "name": "Cheese & Corn Pizza",
        "description": "Cheesy delight loaded with sweet corn kernels and melted mozzarella",
        "price": 170,
    },

    3: {
        "name": "Farmhouse Pizza",
        "description": "Hearty pizza topped with onions, capsicum, tomatoes, mushrooms, and mozzarella",
        "price": 200,
    },

    4: {
        "name": "Paneer & Capsicum Pizza with Special Hot Sauce",
        "description": "Spicy paneer cubes and crunchy capsicum topped with a flavorful hot sauce",
        "price": 260,
    },

    5: {
        "name": "Mexican Green Wave Pizza",
        "description": "Zesty mix of capsicum, onions, tomatoes, jalapeños, and Mexican herbs",
        "price": 300,
    }
}


sides_options = {

    1: {
        "name": "Garlic Bread",
        "description": "Freshly baked bread topped with garlic butter and herbs",
        "price": 180
    },

    2: {
        "name": "Cheesy Garlic Bread",
        "description": "Garlic bread loaded with melted mozzarella cheese",
        "price": 220
    },

    3: {
        "name": "French Fries",
        "description": "Crispy golden potato fries seasoned with salt and herbs",
        "price": 90
    },

    4: {
        "name": "Veggie Nuggets",
        "description": "Crunchy vegetable nuggets served with a tangy dip",
        "price": 140
    },

    5: {
        "name": "Stuffed Cheese Rolls",
        "description": "Soft bread rolls filled with gooey melted cheese",
        "price": 160
    }

}


beverage_options = {

    1: {
        "name": "Coca-Cola",
        "description": "Chilled sparkling cola beverage",
        "price": 60
    },

    2: {
        "name": "Sprite",
        "description": "Refreshing lemon-lime fizzy drink",
        "price": 60
    },

    3: {
        "name": "Cold Coffee",
        "description": "Creamy chilled coffee blended with milk and ice",
        "price": 120
    },

    4: {
        "name": "Fresh Lime Soda",
        "description": "Tangy lime juice mixed with sparkling soda",
        "price": 90
    },

    5: {
        "name": "Lemon Iced Tea",
        "description": "Refreshing chilled tea infused with lemon juice and served over ice",
        "price": 140
    }

}
