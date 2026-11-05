CIRCLE WAVE CONNECT

Employee Engagement and Community Communication Platform

PROJECT OVERVIEW

Circle Wave Connect is an employee engagement and communication platform designed to help employees connect, communicate, and share their experiences within the workplace.

The platform provides a shared space where employees can ask questions, celebrate achievements, and share their weekly performance updates. It encourages collaboration, communication, knowledge sharing, and recognition among colleagues.

The application was developed using Python Flask, HTML, CSS, and SQLite.

PROJECT OBJECTIVES

The main objective of Circle Wave Connect is to improve communication and engagement among employees by providing a centralized platform where they can interact and share information. It aims to encourage employees to share questions and ideas, recognize and celebrate achievements, provide weekly performance updates, and strengthen collaboration within the workplace.

MAIN FEATURES

Create a Post

Employees can create posts by entering their names, selecting a category, and writing a message. This allows them to share information and communicate with other colleagues.

Post Categories

The application supports three post categories: Question, Achievement, and Weekly Performance.

The Question category allows employees to ask questions and seek assistance from their colleagues. The Achievement category allows employees to celebrate their accomplishments and recognize their successes. The Weekly Performance category allows employees to share their weekly progress, activities, and contributions.

Community Activity Feed

The community activity feed displays submitted posts, including employee names, employee initials, posting dates and times, messages, and post categories. This allows employees to view and engage with the information shared within the platform.

Database Storage

The application uses SQLite to store employee community posts. This ensures that submitted information remains available even after refreshing or reopening the application.

TECHNOLOGIES USED

Circle Wave Connect was developed using Python as the backend programming language and Flask as the web application framework. Flask-SQLAlchemy is used for database management, while SQLite provides database storage. HTML is used to structure the webpages, CSS is used for styling, and Jinja2 is used to display dynamic content in the HTML templates. Git and GitHub are used for version control and project hosting.

PROJECT STRUCTURE

The project is organized into different files and folders to make the application easier to manage and maintain.

The main project folder is named Circle_Wave_Attendance. It contains the main application file (app.py), database models (models.py), database initialization file (init_db.py), requirements file (requirements.txt), project documentation (README.md), and the SQLite database file (circle_wave.db).

The templates folder contains base.html and index.html, which define the structure and content of the application's webpages.

The static folder contains the CSS folder, which stores the application's styling in style.css, and the img folder, which contains the Circle Wave logo.

INSTALLATION AND SETUP

To run Circle Wave Connect locally, first clone the project repository from GitHub using the following command:

git clone YOUR_GITHUB_REPOSITORY_URL

Navigate into the project directory using:

cd Circle_Wave_Attendance

Create a virtual environment using:

python -m venv .venv

For Windows PowerShell, activate the virtual environment using:

.venv\Scripts\Activate.ps1

Install the required dependencies using:

pip install -r requirements.txt

After installing the dependencies, start the application by running:

python app.py

Once the application is running, open a web browser and visit the following address:

http://127.0.0.1:5000/

The Circle Wave Connect homepage should now be accessible locally.

DATABASE INFORMATION

Circle Wave Connect uses SQLite as its database management system. The database file is named circle_wave.db, and Flask-SQLAlchemy is used to manage database operations.

The current database model stores community posts using five main fields. The id field provides a unique identification number for each post. The name field stores the employee's name, while the message field stores the content of the post. The type field identifies the category of the post, and the created_at field records the date and time when the post was created.

APPLICATION REQUIREMENTS

The project dependencies are listed in the requirements.txt file. These include Flask version 2.3.2, Flask-SQLAlchemy version 3.0.3, and python-dotenv version 1.0.0.

FUTURE IMPROVEMENTS

Future improvements to Circle Wave Connect could include employee user authentication, allowing employees to securely access the platform. Other improvements could include editing and deleting posts, searching and filtering community posts, administrative post management, and additional features to improve employee interaction and engagement.

CONCLUSION

Circle Wave Connect provides a centralized platform for employee communication and engagement. By allowing employees to ask questions, recognize achievements, and share weekly performance updates, the application encourages a more connected and collaborative workplace.

The project demonstrates the use of web development technologies, database management, and software development practices to create a functional workplace communication application.

PROJECT INFORMATION

Project Name: Circle Wave Connect

Application Type: Employee Engagement and Communication Platform

Backend: Python Flask

Database: SQLite

Frontend: HTML and CSS