# Coffee Shop Management System ☕

This is an Object-Oriented Programming (OOP) system written in Python to manage the basic workflow of a coffee shop. The project handles customer registration, product cataloging, and order creation with robust input validation via the terminal.

## 🚀 Features

*   **Coffee Shop Management:** Centralizes establishment information (Name, Address, CNPJ) and manages lists of registered customers, products, and active orders.
*   **Customer Registration:** Captures first name, last name, address, email, and password.
    *   *Email Validation:* Uses Regular Expressions (`re`) to ensure correct email formatting.
    *   *Text Validation:* Ensures names and last names contain only letters and cannot be empty.
*   **Product Registration:** Adds items to the shop's catalog with details such as name, type, size, and price.
    *   *Numeric Validation:* Directs inputs to prevent empty prices and ensures product sizes are greater than zero.
*   **Order Management:** Allows adding products to a customer's order, verifying beforehand whether the item is available in the coffee shop's current catalog.

## 🛠️ Technologies Used

*   **Python 3.x**
*   **`re` Library:** Used for pattern matching and email format validation.
*   **`unidecode` Library:** Imported for handling accents and special character formatting.

## 🏗️ Architecture & Classes

The system relies on four main classes that interact with one another:

1.  **`Cafeteira` (Coffee Shop):** The core class of the application, responsible for running the registration workflows (`cadastrar_cliente`, `cadastrar_produto`, `cadastrar_pedido`) and storing the data.
2.  **`Cliente` (Customer):** Models identification, contact details, and credentials for users.
3.  **`Produto` (Product):** Stores attributes regarding the beverages or food items available.
4.  **`Pedido` (Order):** Handles the instantiation and data display of completed orders.

## 🔧 How to Run

### Prerequisites
Make sure you have Python installed on your machine and the `unidecode` dependency set up. You can install it using pip:

```bash
pip install unidecode
