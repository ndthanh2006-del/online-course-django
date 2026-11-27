# Online Course - Django Final Project

## Windows setup (no Visual Studio required)
1. Install Python 3.11+ from https://www.python.org/downloads/ and enable **Add Python to PATH**.
2. Extract this ZIP.
3. Open the extracted `online_course_submission` folder in File Explorer.
4. Click the address bar, type `cmd`, and press Enter.
5. Run:

```bat
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
py manage.py migrate
py manage.py seed_demo
py manage.py createsuperuser
py manage.py runserver
```

6. Open http://127.0.0.1:8000/ for the course app.
7. Open http://127.0.0.1:8000/admin/ for Django admin.

Visual Studio is not needed. You can use Command Prompt and any text editor.

## GitHub submission
Create a new **public** GitHub repository, then upload the contents of this folder.
The six required source files are:
- `onlinecourse/models.py`
- `onlinecourse/admin.py`
- `onlinecourse/templates/onlinecourse/course_details_bootstrap.html`
- `onlinecourse/views.py`
- `onlinecourse/urls.py`
- `course_project/urls.py` (project-level routes include the app routes)

For Task 6, submit the URL to `onlinecourse/urls.py`.

## Screenshots
- Task 3: Open `/admin/`, sign in, and capture the page showing both **Authentication and Authorization** and **OnlineCourse**. Save as `03-admin-site.png`.
- Task 7: Open the seeded course page, complete the sample exam correctly, submit, and capture the result page showing **Congratulations**, score, and exam results. Save as `07-final.png`.

Do not submit the screenshots until you have captured them from your own running application. The project includes sample content to make this straightforward.
