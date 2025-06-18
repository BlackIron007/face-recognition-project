#  Database Design – Face Recognition Attendance System

This document outlines the database design for the **AI-Based Face Recognition Group Attendance Management System**, covering all core tables, relationships, and rationales to ensure data integrity, scalability, and performance.

---

##  Overview

The database consists of **three primary relational tables**:

1. `user_profiles` – Stores employee information and face encoding.
2. `attendance_records` – Stores check-in/check-out logs linked to users.
3. `face_images` – Stores face images and metadata for recognition.

All tables are normalized and follow relational database best practices with appropriate constraints and data types.

---

##  Table: `user_profiles`

| Column         | Data Type    | Description                          |
|----------------|--------------|--------------------------------------|
| `user_id`      | VARCHAR(255) | Unique system ID for user (Primary Key) |
| `employee_id`  | VARCHAR(255) | Official company employee ID (Unique) |
| `first_name`   | VARCHAR(255) | User's first name                    |
| `last_name`    | VARCHAR(255) | User's last name                     |
| `email`        | VARCHAR(255) | User email address (Unique)          |
| `phone_number` | VARCHAR(20)  | Contact number                       |
| `department`   | VARCHAR(100) | Department name                      |
| `position`     | VARCHAR(100) | Job title/position                   |
| `face_encoding`| TEXT         | Facial feature encoding vector       |
| `is_active`    | BOOLEAN      | Is the user active in the system     |
| `created_at`   | TIMESTAMP    | Record creation timestamp            |
| `updated_at`   | TIMESTAMP    | Last update timestamp                |

** Relationships:**
- One-to-many with `attendance_records`
- One-to-many with `face_images`

---

##  Table: `attendance_records`

| Column            | Data Type    | Description                             |
|-------------------|--------------|-----------------------------------------|
| `attendance_id`   | VARCHAR(255) | Unique ID for each attendance record    |
| `user_id`         | VARCHAR(255) | Foreign key to `user_profiles.user_id`  |
| `check_in_time`   | TIMESTAMP    | Time of check-in                        |
| `check_out_time`  | TIMESTAMP    | Time of check-out                       |
| `date`            | DATE         | Attendance date                         |
| `status`          | BOOLEAN      | Present (true) or Absent (false)        |
| `confidence_score`| FLOAT        | Confidence level of face match          |
| `location`        | GEOMETRY     | Geo-location data for attendance        |
| `created_at`      | TIMESTAMP    | Record creation timestamp               |

** Relationships:**
- Many-to-one with `user_profiles`

---

## 🖼 Table: `face_images`

| Column            | Data Type    | Description                             |
|-------------------|--------------|-----------------------------------------|
| `image_id`        | VARCHAR(255) | Unique image ID                         |
| `user_id`         | VARCHAR(255) | Foreign key to `user_profiles.user_id`  |
| `image_path`      | VARCHAR(255) | Path to stored image                    |
| `encoding_vector` | TEXT         | Encoded vector from image               |
| `is_primary`      | BOOLEAN      | Whether this is the primary image       |
| `created_at`      | TIMESTAMP    | Timestamp of image record               |

** Relationships:**
- Many-to-one with `user_profiles`

---

##  ER Diagram

![ER Diagram](../../week2/diagrams/er_diagram.png)

_This diagram shows the relationships between all entities and how they are linked via primary and foreign keys._

---

##  Design Highlights

- ✅ **Normalization:** No redundant data across tables.
- ✅ **Foreign Keys:** Ensures referential integrity.
- ✅ **Timestamps:** Useful for auditing and logs.
- ✅ **Face Encoding:** Stored as `TEXT` to support long vector arrays.
- ✅ **Scalability:** Designed for multi-user, real-time attendance tracking.

---

##  File Reference

SQL schema: [`database_schema.sql`](../../../../database/database_schema.sql)  
ER Diagram: [`er_diagram.png`](../../week2/diagrams/er_diagram.png)

