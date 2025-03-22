# 🔗 Shortify - Flask URL Shortener

A simple and clean URL shortener built with **Flask** and **MongoDB**.  
Generate short links and get redirected instantly — no login required.

---

## 🚀 Features

- Shorten long URLs into 6-character short links
- Auto redirect to the original URL via short link
- Simple and clean web interface
- Copy-to-clipboard support
- Custom 404 page for broken links
- Fully API-backed for integration

---

## 🧱 Tech Stack

- Python 3.x
- Flask
- MongoDB (via PyMongo)
- Bootstrap (Frontend)
- JavaScript Fetch API

---

## 📁 Project Structure

```
shortify/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│   ├── utils.py
├── templates/
│   ├── index.html
│   └── 404.html
├── static/
├── run.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Nuraj250/shortify-flask.git
cd shortify-flask
```

### 2. Create and Activate Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root:

```env
MONGO_URI=mongodb://localhost:27017/
DB_NAME=shortify
BASE_URL=http://localhost:5000
```

Make sure MongoDB is running on your system.

### 5. Run the Application

```bash
python run.py
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## 🎯 API Endpoints

### POST `/shorten`

**Request Body:**

```json
{
  "url": "https://example.com"
}
```

**Response:**

```json
{
  "short_url": "http://localhost:5000/abc123"
}
```

---

## 📄 License

MIT License

---

## 🙌 Acknowledgements

Built with ❤️ using Flask and MongoDB.
```
