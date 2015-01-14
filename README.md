# amani

#About

Amani is a way to patch configuration files.

#Install

    pip install amani

#Usage

constants.py

    class A:

        a = 1
        b = []
        c = [1, 3, 5]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'maps',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '3306',
        }
    }

    try:
        import amani
        g = globals()
        amani.patch(__file__, g)
    except:
        pass


patch_constants.py

    PATCHES = [
        ["A", "a", 2],
        ["A", "b", ["test"]],
        ["A", "c", 1, 2**32],
        ["DATABASES", "default", "USER", "username"],
        ["DATABASES", "default", "PASSWORD", "pass-WORD"]
    ]
