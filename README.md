# EcoQuest

- Follow the instructions below to run the web application
- VS Code is the recommended text editor to locally run the web app, however, any IDE will work with a few adjustments in the instructions.

## Set-up Instructions

### 1. Clone the repo 

```bash
git clone https://github.com/github_username/repo_name.git
```

### 2. Set up and activate local environment 

```bash
python -m venv .venv
```

- Activate venv on macOS

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

### 2. Run the django server

```bash
python manage.py
```

## Debugging

If you encounter a problem during running the server run the following code

```bash
python manage.py makemigrations
python manage.py migrate
```



- Enter python manage.py runserver into terminal and check it successfully runs and gives a local URL to see the website.
- Either CTRL + Click the URL or type the URL into a browser.

# Dependencies 

Python
Pip (Should come with the virtual environment being set up correctly)
Git (To clone the repository from GitHub)
VS Code or another IDE

To check Python
```bash
python --version
```

To check Git in terminal
```bash
git --version
```

To check pip in terminal
```bash
pip --version
```

# Testing

## Testing whole project

### Enter into the terminal within groupproject folder

```bash
python manage.py test
```

## Testing specific project package's tests module

Enter into the terminal within the groupproject folder the following where ```<package-name>``` is the name of the package intended to be tested:

```bash
python manage.py test <package-name>
```

or the following could be entered where it is specified that the ```tests``` module within the package is being used to test the package:

```bash
python manage.py test <package-name>.tests
```

For example if you wanted to run all the tests in the package ```registration``` you could enter the following into the terminal:

```bash
python manage.py test registration
```

or alternatively the following could be entered:

```bash
python manage.py test registration.tests
```


## Testing specific test class

Enter into the terminal within the groupproject folder where ```<package-name>``` is the name of the package containing the ```tests``` module that has the class intended to be used for testing followed by ```tests``` which is then followed by a ```<class-name>``` where this is the name of the class intended to be tested, all separated by a ```.``` symbol:

```bash
python manage.py test <package-name>.tests.<class-name>
```

For example if you wanted to run all the tests in the class ```RegistrationViewTest``` you could enter the following into the terminal:

```bash
python manage.py test registration.tests.RegistrationViewTest
```

## Testing specific test method

Enter into the terminal within the groupproject folder where ```<package-name>``` is the name of the package containing the ```tests``` module that has the class that contains the method intended to be used for testing followed by ```tests``` which is then followed by a ```<class-name>``` where this is the name of the class with the method intended to be used for testing which is finally followed by a ```<method-name>``` which is the method intended to be used for testing, all separated by a ```.``` symbol:

```bash
python manage.py test <package-name>.tests.<class-name>.<method-name>
```

For example if you wanted to run all the tests in the method ```test_registration_page_loads``` you could enter the following into the terminal:

```bash
python manage.py test registration.tests.RegistrationViewTest.test_registration_page_loads
```
