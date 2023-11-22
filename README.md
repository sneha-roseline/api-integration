# GitHub API Integration

# Project Overview:
Pull data from the GitHub API to retrieve information about repositories and users. 
Process the data using Python and store it in a simple SQLite database. 
Set up a basic Flask web application to display the stored data.

## Technologies Used:

Python
Flask
SQLite
Requests library for making API requests
Git for version control

## Step-by-Step Implementation:

### Step 1: **Set Up Your Development Environment:**
   - Install Python from the [official website](https://www.python.org/).
   - Install Flask: `pip install flask`.
   - SQLite is included with Python, so no additional installation is needed.
   - Install Git by following the instructions on the [Git website](https://git-scm.com/).

### Step 2: **Initialize a Git Repository:**
   ```bash
   mkdir github-api-integration
   cd github-api-integration
   git init
   git add .
   git commit -m "Initial commit" 
```
### Step 3: **Create a Flask Application:**
Create a file named app.py for your Flask application

### Step 4: **Create HTML Template:**
Create a folder named templates in your project directory and create an HTML file named index.html inside it.

### Step 5: **Pull Data from GitHub API and Store in SQLite:**
Modify the app.py file to include code for pulling data from the GitHub API and storing it in the SQLite database.

### Step 6: **Run the Flask Application:**
Run the Flask application, Visit http://127.0.0.1:5000/ in your web browser to see the GitHub data displayed.

## Usage
The Flask application displays information about GitHub repositories, including repository name, owner login, and stargazers count.

## Output

<p align="center">
  <img width="715" alt="Screen Shot 2023-11-22 at 2 34 33 PM" src="https://github.com/sneha-roseline/github-api-integration/assets/146040464/095255e5-c9dc-4286-a0be-c4fa06b1d186">
</p>

