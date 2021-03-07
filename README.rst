kenya-ambulances-master-list
============================

Kenya Ambulances master list

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT


#Running Locally With Docker

1. Clone the project:

    $ git clone https://github.com/Labohkip81/Kenya-Ambulances-Master-list---Unes-Practical-Test-.git

2. cd into the folder:
      $cd Kenya-Ambulances-Master-list---Unes-Practical-Test/

3. Build the docker image and run:

    $docker compose -f local.yml build 

4. Running the container:

    $docker compose -f local.yml run 


5. Running Commands interactively 
    $ docker-compose -f local.yml run --rm django python manage.py <command>


Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy kenya_ambulances_master_list

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest




Deployment
----------

The following details how to deploy this application.

```
docker compose -f production.yml up
```

