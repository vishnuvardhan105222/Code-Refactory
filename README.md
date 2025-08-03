🛠️ User Management API – Messy Migration Refactor
This project is a refactored version of an existing poorly structured Python web service. The goal was to clean up and organize the codebase for maintainability, without adding new features or UI. It follows best practices for separation of concerns and project structure.

🚀 Features
✅ Create Users – POST /users

✅ Update Users – PUT /user/<id>

✅ Delete Users – DELETE /user/<id>

✅ Get All Users – GET /users

✅ Get Single User – GET /user/<id>

✅ Search by Name – GET /search?name=<name>

✅ Login Endpoint – POST /login

✅ Health Check – GET /

📂 Project Structure
graphql
Copy
Edit
messy-migration/
├── app.py              # Main app entrypoint
├── init_db.py          # Initializes the SQLite DB schema
├── requirements.txt    # Project dependencies
├── README.md           # This file
├── Change.md           # Summary of code changes and rationale
├── users.db            # SQLite database (auto-generated)
├── .gitignore          # Ignores venv, __pycache__, *.db
├── venv/               # Python virtual environment
└── __pycache__/        # Python bytecode cache (ignored)
💻 Setup Instructions
1. Create Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Initialize the Database
bash
Copy
Edit
python init_db.py
4. Run the Application
bash
Copy
Edit
python app.py
Server runs on: http://localhost:5009

📬 Example API Calls (PowerShell)
powershell
Copy
Edit
# Create a user
Invoke-RestMethod -Uri http://localhost:5009/users -Method POST -ContentType "application/json" -Body '{"name":"Alice","email":"alice@example.com","password":"securepass"}'

# Search by name
Invoke-RestMethod -Uri http://localhost:5009/search?name=Alice -Method GET

# Update a user
Invoke-RestMethod -Uri http://localhost:5009/user/1 -Method PUT -ContentType "application/json" -Body '{"name":"Alice Updated"}'

# Delete a user
Invoke-RestMethod -Uri http://localhost:5009/user/1 -Method DELETE
🧾 Notes
Database: SQLite (lightweight, self-contained)

No additional features added – strictly adhered to the original functionality

Manual testing confirmed for all endpoints

