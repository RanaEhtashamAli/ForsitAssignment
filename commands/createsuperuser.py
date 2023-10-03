import os.path as path
import re
import sys
from inspect import getsourcefile
from contextlib import contextmanager

import click

current_dir = path.dirname(path.abspath(getsourcefile(lambda: 0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])

from database.session import get_db
from app.user.models import User


@click.command()
@click.option("--email", prompt="Your email", help="Super user's email.")
@click.option("--password", prompt="Your password", help="Provide password for the admin user.")
@click.option("--confirm_password", prompt="Confirm password", help="Provide password again for the admin user.")
def createsuperuser(email, password, confirm_password):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        click.echo('Please provide a valid email address.')
        exit()
    if password != confirm_password:
        click.echo('Password and Confirm Password does not match.')
        exit()
    new_user = User(email=email, is_admin=True)
    new_user.set_password(password)
    with contextmanager(get_db)() as session:
        session.add(new_user)
        session.commit()
    click.echo('Super user created.')


if __name__ == '__main__':
    createsuperuser()
