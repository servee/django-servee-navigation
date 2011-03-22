Django-servee-navigation is a navigation plugin for django-servee

It requires django-treebeard but is installed during installation.

There are no views or URLS for this project, it uses the default views, urls, and forms of the Servee ModelInsert class.

To try it out:

1.   Download the project.
2.   run python setup.py develop [requires django-servee=>0.6 which is trunk, not in PyPI]
3.   cd example_project
4.   python manage.py syncdb
5.   python manage.py runserver
6.   http://localhost:8000/login/