# ForsitAssignment

* Take pull of main branch from this repository.
* Create a virtual environment using following command:
  * For windows:
    ``python -m venv env``
  * For Mac or Linux:
    ``python3 -m venv env``
* Activate the virtual environment using following command:
  * For windows:
    ``env/Scripts/activate``
  * For Mac or Linux:
    ``source env/bin/activate``
* Install the requirements using following commands:
    ``pip install -r requirement.txt``
* Create a ``.env`` file in the root folder. You can take example from the .env.example file.
* File all the environment variables.
* Run following command to run Database migrations:
  ``alembic upgrade head``
* In the root directory you can run following command to create admin user:
  ``python commands/createsuperuser.py``
* It will ask for email and password and will create a user for you.
* Run following command to insert dummy data in database:
  ``python commands/populate_data.py``
* Once done with above steps you can run following command to run the app:
  ``python main.py``