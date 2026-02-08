## 🚀 Backend Project 2 (Debugging)

*Innomatics Research Labs – Data Science Internship*

This repository contains a refactored Flask-based note taking application. The original application provided for this task was broken and did not function correctly. As part of this assignment, the application was carefully analyzed, all bugs were identified, and the code was refactored to ensure the application works properly.

The application contains a single Home route where users can add notes using a text field and a button. All added notes are displayed as an unordered list on the same page.

---

## 🧩 Task Description

The task is to refactor a broken Flask application and make sure the application works properly. While fixing the application, all bugs must be identified and documented along with the approach used to resolve them.

The Home route should:
- Contain a text field and a button
- Allow users to add notes
- Display all notes as an unordered list on the same page

---

## 📁 Project Structure

All submission files are organized as shown below:

```
📁 Sourav_419_Data-Science-with-Advanced-GENAI-Internship_Assignment_9
│
├── app.py
├── Bug_Fix_Document.pdf
├── flask_task3.png
└── templates
    └── home.html
```

Each file contributes directly to fulfilling the task requirements.

---

## 🛠 Technologies Used

Python, Flask, and HTML are used to build and refactor this application.

---

## ▶️ How the Application Works

The application runs on a local Flask development server using a single Home route. When the page loads, an input field and a button are displayed. The user enters a note and submits the form.

Upon submission, the request is sent to the backend using a POST request. The backend validates the input and stores the note in memory. All stored notes are then rendered on the same page as an unordered list.

---

## ▶️ How to Run the Application

Ensure Python is installed on your system. Install Flask by running the following command:

pip install flask

After installing Flask, navigate to the project directory and start the application using:

python app.py

Once the server starts, open a web browser and access the application at:

http://127.0.0.1:5000/

---

## 📌 Output

Users can add multiple notes using the input field. Each submitted note is displayed immediately below the input field as part of an unordered list on the same page.

---

## 🧑‍🎓 Intern Details

| Field | Information |
|------|-------------|
| **Name** | Sourav Varma Gottumukkala |
| **Assignment** | Backend Project 2 (Debugging) |
| **Internship** | Data Science Internship |
| **Organization** | Innomatics Research Labs |

---

## 🏁 Final Summary

This project demonstrates the ability to analyze a broken Flask application, identify functional and logical bugs, refactor the code, and ensure correct application behavior. It also highlights proper documentation of bugs and a clear approach to resolving them.

**This completes Internship Assignment => Backend Project 2 (Debugging) successfully.**

---

**If you found this Flask refactoring project helpful, feel free to give it a ⭐**
