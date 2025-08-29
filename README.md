Diviso – Smart Bill Splitter

A simple Django REST API that lets you upload café/restaurant bills, extracts text using OCR (Tesseract), and lays the foundation for fair cost-splitting.

Features

Upload bill images (JPG/PNG)

OCR-based text extraction (Tesseract)

RESTful API (Django REST Framework)

Future-ready for itemized splitting & payments

Quick Start
git clone https://github.com/yourusername/diviso-backend.git
cd diviso-backend
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Upload a bill:

curl -X POST -F "image=@/path/to/bill.jpg" http://127.0.0.1:8000/api/bills/upload/

Roadmap

 Bill upload & OCR

 Preprocessing (rotation, noise cleanup)

 Authentication & user profiles

 Itemized splitting logic

 Payment integration

Tech Stack

Django • DRF • Tesseract OCR • SQLite (dev) • PostgreSQL (planned)