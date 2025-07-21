# 🛒 Ecommerce Backend API — HROne Hiring Task

This is a sample **FastAPI** backend application for an e-commerce platform built as part of the **HROne Backend Intern Hiring Task**.

---

## 🚀 Tech Stack

- **Python 3.13**
- **FastAPI** – for building APIs
- **MongoDB Atlas** – cloud NoSQL database
- **Motor** – async MongoDB driver
- **Uvicorn** – ASGI server
- **Render** – hosting (Free Plan)

---

## 📂 Project Structure

├── main.py # Entry point
├── db.py # MongoDB connection
├── routes/
│ ├── product.py # /products endpoints
│ └── orders.py # /orders endpoints
├── models/
│ ├── product.py # Product schema
│ └── orders.py # Order schema
├── .env # MongoDB URI (locally)
├── requirements.txt # Dependencies
└── README.md # You're here!

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/samchirayilsaji/Ecommerce-backend
cd Ecommerce-backend

# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority

{
  "name": "T-shirt",
  "description": "Cotton round neck",
  "price": 499.99,
  "size": "medium"
}
🔸 List Products
GET /products

Query params (all optional):

name: partial name match (regex)
size: e.g., large
limit: number of records
offset: for pagination
🧾 Swagger Docs

Available at:
👉 https://ecommerce-backend-he59.onrender.com/docs
Hosted on Render (Free Plan):
🔗 https://ecommerce-backend-he59.onrender.com


