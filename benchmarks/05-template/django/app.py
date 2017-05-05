
"""
"""

import sys


def main(name):
    # unload django modules, if any, so we can reconfigure settings
    modules = [m for m in sys.modules.keys() if m.startswith('dj')]
    for m in modules:
        del sys.modules[m]

    from django.conf import settings
    from django.template import Context
    from django.template import loader
    from django import setup

    settings.configure(
        TEMPLATES=[{'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    'APP_DIRS': True,
                    'DIRS': [name,]}, ]
    )
    setup()
    template = loader.get_template('welcome.html')
    # return lambda ctx: template.render(Context(ctx))
    return template.render
