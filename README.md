# EcoQuest

- Follow the instructions below to run the web application
- VS Code is the recommended text editor to locally run the web app, however, any IDE will work with a few adjustments in the instructions.

## Set-up Instructions

### 1. Clone the repo 

```bash
git clone https://github.com/github_username/repo_name.git
```

### 2. Set up and activate local environmment 

```bash
python -m venv .venv
```

- Activate venv on MacOS

```bash
.venv/bin/activate
```

- Activate venv on Windows

```bash
.venv/Scripts/activate
```

### 3. Install dependencies

```bash
python install -r requirements.txt
```

## Run the program

### 1. Navigate into project folder

```bash 
cd groupproject
```

### 2. Run the dhango server

```bash
python manage.py
```

## Debugging

If you encounter a problem during running the server run the folloding code

```bash
python manage.py migrate
python manage.py makemigrations
```



- Enter python manage.py runserver into terminal and check it successfully runs and gives a local URL to see the website.
- Either CTRL + Click the URL or type the URL into a browser.

# Dependencies 

Python
Pip (Should come with the virtual environment being set up correctly)
Git (To clone the repository from GitHub)
VS Code or another IDE

To check Python (in VS Code or another terminal do python --version)
To check Git (git --version in terminal)
To check pip (pip --version in terminal)

# Testing

1) Enter into the terminal (python manage.py test) within groupproject folder
   
