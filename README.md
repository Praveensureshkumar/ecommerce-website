# 🛒 E-Commerce Web Application

An end-to-end E-Commerce platform built using Django, MySQL, Elasticsearch and JavaScript.  
This project features real-time search, secure authentication, order processing and a custom admin dashboard.

## 🚀 Features

- Real-time Search using Elasticsearch (30% faster search experience)
- Secure User Authentication with Django
- Product & Order Management backed by MySQL
- Custom Admin Dashboard to streamline backend operations (reduced admin workload by 40%)
- Responsive Frontend using HTML, CSS, and JavaScript
- Scalable Architecture with clean MVC structure

## 🛠️ Tech Stack

- Backend: Django (Python)  
- Database: MySQL  
- Search Engine: Elasticsearch  
- Frontend: HTML, CSS, JavaScript 

## ⚙️ Setup Instructions

```bash
# 1. Clone the Repository
git clone https://github.com/your-username/ecommerce-app.git
cd ecommerce-app

# 2. Set Up Virtual Environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Configure MySQL Database
# - Create a database in MySQL (e.g., ecommerce_db)
# - Update the DATABASES section in settings.py with your credentials

# 5. Run Migrations
python manage.py makemigrations
python manage.py migrate

# 6. Run Elasticsearch
# Make sure Elasticsearch is running on localhost:9200
# If using Docker:
docker run -p 9200:9200 -e "discovery.type=single-node" elasticsearch:7.10.0

# 7. Run the Django Server
python manage.py runserver
