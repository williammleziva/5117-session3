## Session 3 - Flask environment setup
ensure not in any virtual environment 

    exit

check python verison

    python --version

create pipfiles, in new dir

    pipenv --python 3.8.10

Install new dependancies: 

    pipenv install []

Optional- Create requirements.txt file with

    pipenv requirements


## Enter environment and run 

enter virtual environment 

    pipenv shell

install from pipfiles

    pipenv install

To Run

    flask --app server.py run

Optionly, Run in debug mode 

    flask --app server.py --debug run

## dotenv instruction

    pipenv install dotenv
    touch .env 

Within python/flask include 

    from dotenv import load_dotenv
    import os

    load_dotenv()
    my_id = os.getenv("ID")
