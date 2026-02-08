## 🚀 Final Project (Basic Version) - URL Shortner Application

**Innomatics Research Labs – Data Science Internship**

This repository contains a Flask-based **URL Shortener web application (Basic version)**. The application allows users to shorten long URLs and store them for future reference. Users can view previously shortened URLs along with their original URLs through a dedicated history page.

The objective of this task is to understand **Flask-based backend development, database integration using ORM, multi-page frontend handling, and basic URL validation**, without implementing authentication or advanced user management features.

---

## 🧩 Problem Statement

Develop a basic URL Shortener web application that:
- Shortens long URLs
- Allows users to save URLs
- Displays previously shortened URLs
- Provides a simple and clean user interface

The application should use Flask for backend development, HTML/CSS for frontend rendering, and an ORM with a database to store URL mappings.

---

## 📁 Project Structure

**All submission files are organized as shown below:**

```
📁 Sourav_419_Data-Science-with-Advanced-GENAI-Internship_Assignment_10
│
├── app.py
├── flask_task4.png
├── URL Shortener Web Application (Basic).pdf
├── instance
│   └── urls.db
└── templates
    ├── index.html
    └── history.html
```

Each file contributes directly to fulfilling the project requirements.

---

## 🛠 Technologies Used

- Python  
- Flask  
- HTML  
- CSS  
- SQLAlchemy (ORM)  
- SQLite (Database)  

---

## ▶️ Application Workflow

1. The user enters a long URL on the Home page.
2. Upon clicking the **Shorten** button, the application generates a shortened version of the URL.
3. The original URL and its shortened version are stored in the database.
4. The shortened URL is displayed on the same page and can be copied using the copy button.
5. The History page displays all previously stored original URLs along with their shortened URLs.

---

## ▶️ How the Application Works

The Flask application runs on a local development server and uses SQLAlchemy as an ORM to interact with an SQLite database. When a user submits a URL, a unique short code is generated and mapped to the original URL. This mapping is stored in the database and reused for displaying history and redirecting shortened URLs.

Basic URL validation is performed to ensure the entered input resembles a valid URL before processing.

---

## ▶️ How to Run the Application

Ensure Python is installed on your system. Install the required dependencies using:

pip install -r requirements.txt

After installing dependencies, navigate to the project directory and start the application using:

python app.py

Once the server starts, open a web browser and access the application at:

http://127.0.0.1:5000/

---

## 📌 Features Implemented

- URL shortening functionality  
- Database storage of original and shortened URLs  
- URL history tracking  
- Copy-to-clipboard support for shortened URLs  
- Multi-page frontend (Home & History)  

---

## 🧑‍🎓 Intern Details

| Field | Information |
|------|-------------|
| **Name** | Sourav Varma Gottumukkala |
| **Assignment** | Final Project (Basic Version) - URL Shortner Application |
| **Internship** | Data Science Internship |
| **Organization** | Innomatics Research Labs |

---

## 🏁 Final Summary

This project demonstrates the ability to design and implement a basic URL Shortener web application using Flask and database integration. It reflects understanding of backend logic, ORM usage, frontend rendering, and structured project organization while meeting all the requirements specified for the Basic version of the task.

---

**This completes Internship Assignment => Final Project (Basic Version) - URL Shortner Application successfully.**

---

**If you found this URL Shortener project helpful, feel free to give it a ⭐**
