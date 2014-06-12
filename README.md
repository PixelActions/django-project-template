Django project template
=======================

This is the base template for the django projects at PixelActions.

Feel free to improve/comment if you feel like it!

Usage:

```bash
$ django-admin.py startproject --template=https://github.com/pixelactions/django-project-template/zipball/master <project_name>
```

Notes and Explanations:
-----------------------

We use gunicorn for deployment and currently use Webfaction as our host. So outside the main project folder can be found the relevant fab files for deployment on webfaction servers. If you are also a webfaction user feel free to use them.

Concerning the settings files, we also use generic local/stage files and every developer abides to the same settings pretty much. local settings use SQLite3 while stage settings use MySQL.


