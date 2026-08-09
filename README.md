# CompareX

CompareX is a Flask-based product price comparison web application that helps users compare products and prices across different stores.

## 🚀 Features

* 🔎 Search for products
* 📊 Compare product prices
* 🛍️ View products from multiple stores
* 💰 Track and manage product prices
* ➕ Add new products
* 🏪 Add store-specific prices
* ✏️ Update product prices
* 🗑️ Delete products
* 👨‍💼 Admin interface for managing products and prices
* 📱 Responsive web interface

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite
* **Version Control:** Git & GitHub

## 📁 Project Structure

```text
comparex/
├── app.py
├── database.py
├── predictor.py
├── insert_data.py
├── requirements.txt
├── templates/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── scraper/
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd comparex
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

On macOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Flask application with:

```bash
flask --app app run --port 5001
```

Then open:

```text
http://127.0.0.1:5001
```

## 🔗 Main Routes

| Route                           | Purpose               |
| ------------------------------- | --------------------- |
| `/`                             | Home page             |
| `/search`                       | Search products       |
| `/compare/<product_name>`       | Compare a product     |
| `/admin`                        | Admin interface       |
| `/add_product`                  | Add a product         |
| `/prices/<product_id>`          | View product prices   |
| `/add_price/<product_id>`       | Add a product price   |
| `/update_prices/<product_name>` | Update product prices |
| `/delete_product/<product_id>`  | Delete a product      |

## 🧪 Local Testing

The application can be tested locally using Flask's development server:

```bash
flask --app app run --port 5001
```

Successful requests should return HTTP `200` responses for the main application pages and static resources.

> **Note:** Flask's built-in development server is intended for local development and testing. A production WSGI server should be used when deploying CompareX online.

## 📌 Future Improvements

* Deploy CompareX online
* Add user authentication
* Improve price-history visualization
* Add automated price scraping
* Add more shopping platforms
* Add price-drop notifications
* Improve search and filtering
* Add automated testing
* Improve production security and configuration

## 👩‍💻 Author

**Bhavana Pothuri**

## 📄 License

This project is currently intended for educational and personal development purposes.
