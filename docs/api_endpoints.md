# API Endpoints

## 1. POST /api/add_user
- Input: { name, employee_id, photo (Base64) }
- Output: { success, user_id, message }

## 2. POST /api/recognize
- Input: { frame (Base64 image) }
- Output: [{ user_id, name, confidence }, ...] or []

## 3. POST /api/mark_attendance
- Input: { user_id }
- Output: { success, attendance_id, timestamp }

## 4. GET /api/attendance
- Input: (optional filters: start_date, end_date)
- Output: [{ user_id, name, timestamp, status, confidence }, ...]

## 5. (Future) POST /api/login
- For admin access control

