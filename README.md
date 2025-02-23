
# Running Django Webapp

VS Code is the recommended text editor to locally run the web app, however, any IDE will work with a few adjustments in the instructions.

1) Clone the repository into your laptop or computer
2) Check that all the files have been downloaded successfully
3) Create a terminal if one is not open already and navigate into the [Group-Software-Engineering-Project/] folder using cd (to navigate directories). To check if you're in the correct folder, do [ls] (works regardless of operating system and lists files and folders in your current directory/folder)
4) In the terminal, do the following:
   4.1) python -m venv .venv (this creates a separate environment for any packages that need to be installed to get the web          app working)
   4.2) Check if there is a .venv folder within Group-Software-Engineering-Project folder and if there is do the following

    For Windows:
       Use either / or \
       .venv\Scripts\activate
   For Linux and MacOS
     source .venv/bin/activate

5) Once a ./venv folder has been made and in terminal there is a (.venv) appearing with your path when you type commands, do python install -r requirements.txt
6) Enter into terminal [cd groupproject]
7) Type into terminal [python manage.py runserver] and if that doesn't work follow the instructions given

    It will either say that there are migrations that need to be done, to fix this do:
       python manage.py migrate
   If that doesn't work do:
     python manage.py makemigrations

   Continue until db.sqlite3 has been made and no new migrations show in python manage.py migrate

8) Enter python manage.py runserver into terminal and check it successfully runs and gives a local URL to see the website.
9) Either CTRL + Click the URL or type the URL into a browser

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
   
