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

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'maps',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '3306',
        }
    }

    try:
        import amani
        amani.patch(__file__, globals(), prefix='test')
    except:
        pass

    print A.a
    print A.b
    print DATABASES['default']


test_constants.json

    [
        ["A", "a", 2],
        ["A", "b", ["test"]],
        ["DATABASES", "default",
            {
                "ENGINE": "django.db.backends.mysql",
                "NAME": "maps",
                "USER": "user",
                "PASSWORD": "password",
                "HOST": "",
                "PORT": "3306"
            }
        ]
    ]
