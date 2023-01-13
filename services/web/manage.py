"""
Start development server by running `python3 manage.py run`

To regenerate database run `python3 manage.py create_db`
Create Quest user by running `python3 manage.py seed_db`

Environment variables:

Path to flask app:
FLASK_APP=project/__init__.py

Enable debugging:
FLASK_DEBUG=1
"""

from os import environ

from flask.cli import FlaskGroup

# app is required for running the (uvicorn) server
from project import db, app

cli = FlaskGroup()


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    from project.models import User
    new_user = User()
    new_user.id = 0
    new_user.username = "Quest"
    new_user.set_password(environ.get('QUEST_PASSWD', 'thinking_mooning_ions_geek_pop'))
    db.session.add(new_user)
    db.session.commit()

    from project.models import Quiz
    example_quiz = Quiz(title="Default Quiz", author=0)

    from project.models import Cards
    example_card_1 = Cards(1, "Did the quiz load up?", "Yes", "No", "", "")
    example_card_2 = Cards(1, "Everything seems to work. Select lowest integer.", "42", "53", "a", ":)")
    example_quiz.cards.append(example_card_1)
    example_quiz.cards.append(example_card_2)
    db.session.add(example_quiz)

    db.session.commit()


if __name__ == "__main__":
    cli()
