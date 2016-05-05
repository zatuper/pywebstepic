# from http://www.tangowithdjango.com/book/chapters/models.html

import os

def populate():
    test_author=add_author('testauth')

    add_quest(author=test_author,
        title="Official Python Tutorial",
        text="http://docs.python.org/2/tutorial/")

    add_quest(author=test_author,
        title="How to Think like a Computer Scientist",
        text="http://www.greenteapress.com/thinkpython/")

    add_quest(author=test_author,
        title="Learn Python in 10 Minutes",
        text="http://www.korokithakis.net/tutorials/python/")

    django_author=add_author("Django")

    add_quest(author=django_author,
        title="Official Django Tutorial",
        text="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_quest(author=django_author,
        title="Django Rocks",
        text="http://www.djangorocks.com/")

    add_quest(author=django_author,
        title="How to Tango with Django",
        text="http://www.tangowithdjango.com/")

    frameauthor= add_author("Other aut")

    add_quest(Authorhor=frame_author,
        title="Bottle",
        text="http://bottlepy.org/docs/dev/")

    add_quest(author=frame_author,
        title="Flask",
        text="http://flask.pocoo.org")

    # Print out what we have added to the user.
    for auth in Author.objects.all():
        for q in Question.objects.filter(Author=auth):
            print "- {0} - {1}".format(str(auth), str(q))

def add_quest(author, title, text, rating=0):
    q = Question.objects.get_or_create(Author=author, title=title, text=text, rating=rating)[0]
    return q

def add_author(name):
    auth = Author.objects.get_or_create(name=name)[0]
    return auth

# Start execution here!
if __name__ == '__main__':
    print "Starting ask population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ask.settings')
    from ask.models import Author, Question
    populate()