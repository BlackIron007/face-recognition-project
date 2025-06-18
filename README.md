# AI-Based Face Recognition for Group Attendance Management System

This project is a smart, AI-powered attendance system that uses facial recognition to automatically mark attendance of users in real-time via webcam. Designed for classrooms, workplaces, or group gatherings, it streamlines the manual attendance process into a fast, contactless, and accurate system.

---

##  Features

-  Real-time webcam video capture
-  Face recognition using machine learning models
-  Attendance data auto-stored in a database
-  Cloud-ready architecture for scalability
-  Web-based user interface (HTML + CSS)
-  Dashboard and login/logout flow
-  Secure backend with API endpoint for recognition

---

##  Tech Stack

| Layer         | Tools Used                        |
|--------------|------------------------------------|
| Frontend     | HTML, CSS, JavaScript              |
| Backend      | Python, Flask                      |
| ML Model     | Face recognition (Dlib / OpenCV)   |
| Database     | PostgreSQL                         |
| Deployment   | Localhost (Cloud-ready architecture) |

---

##  System Architecture

> This diagram shows how each component of the system interacts with the others.

![System Architecture](docs/week2/diagrams/system_architecture.png)

---

##  UX Flow

> This diagram represents the user journey through the application, from login to logout.

![UX Flow](docs/week2/diagrams/ux_flow.png)

---

##  Sequence Diagram

> This diagram shows the sequence of operations between different components when a user interacts with the system.

![Sequence Diagram](docs/week2/diagrams/sequence_diagram.png)

---

## ER Diagram (Database Design)

> The Entity-Relationship diagram below shows the relational structure between users, their facial images, and attendance records.

![ER Diagram](docs/week2/diagrams/ER-diagram.png)

---

## Database Schema

> The following SQL schema defines the structure of the database tables used for storing users, facial encodings, and attendance logs.

- **User Profiles Table**  
  Stores employee information and face encodings.

- **Attendance Records Table**  
  Logs attendance check-in/out with confidence score and location.

- **Face Images Table**  
  Supports storage of multiple face images per user with encoding metadata.

➡ [Click here to view schema SQL file](docs/database_schema.sql)

➡ [Click here to view detailed design document](docs/database_design.md)

---

##  Setup Instructions

> To run this project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/BlackIron007/face-recognition-project.git
   cd face-recognition-project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt   
3. Run the application:
   ```bash
   python run.py
4. Visit http://localhost:5000 in your browser.   

