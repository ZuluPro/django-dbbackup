================================
Django project for test Dbbackup
================================

This module is a fake Django project for test Django Dbbackup. It contains
project settings in ``runtests.py`` and an application named :mod:`testapp`.

Tests are stored in :mod:`dbbackup.tests` and for run them you must launch:

::

    python runtests.py

In fact, ``runtests.py`` acts as a ``manage.py`` file and all Django command
are available. So you could launch:

::

    python runtests.py shell

For get a Python shell configured with the test project. Also all test
command options are available and usable for run only some chosen tests.
See `Django test command documentation`_ for more informations about it.

.. _`Django test command documentation`: https://docs.djangoproject.com/en/stable/topics/testing/overview/#running-tests
