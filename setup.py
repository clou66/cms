import codecs
import os

from setuptools import find_packages
from setuptools import setup

version = '1.0.0.dev0'
description = "A web application framework based on Pyramid and SQLAlchemy." \
              "Content Management System called Huracán."
author = 'Toko'
author_email = 'info@surpri.de'
url = 'https://www.surpri.de'
keywords = 'web cms pyramid sqlalchemy bootstrap Huracán'


install_requires = [
    'Chameleon>=2.7.4',
    'alembic>=0.8.0',
    'colander>=1.3.2',
    'deform>=2.0.5',
    'html2text',
    'iso8601==0.1.11',
    'js.angular',
    'js.bootstrap>=3.0.0',
    'js.deform>=2.0.3',
    'js.html5shiv',
    'js.jquery_timepicker_addon',
    'pyramid>=1.10.2',
    'pyramid_chameleon',
    'pyramid_deform>=0.2a3',
    'pyramid_mailer',
    'pyramid_tm',
    'pyramid_zcml>=1.1.0',
    'repoze.zcml>=1.0b1',
    'sqlalchemy>=1.0.0',
    'sqlalchemy-utils',
    'unidecode',
    'usersettings',
    'waitress',
    'zope.deprecation',
    'zope.interface',
    'zope.sqlalchemy',
    ]

tests_require = [
    'Pillow',
    'pytest-virtualenv',
    'zope.testbrowser>=5.0.0',
    ]

development_requires = [
    'pyramid_debugtoolbar',
]

docs_require = [
    'Sphinx',
    'docutils',
    'repoze.sphinx.autointerface',
    'sphinx_rtd_theme',
    'setuptools-git',
    'pytest',
    ]

setup_requires = [
    'setuptools_git>=0.3',
]


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), "rb", "utf-8") as f:
        return f.read()


setup(name='Huracán',
      version=version,
      description=description,
      long_description='\n\n'.join([read('README.rst'),
                                    read('AUTHORS.txt'),
                                    read('CHANGES.txt'), ]),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Huracán',
          'Framework :: Pyramid',
          'License :: MIT',
          'Natural Language :: English',
          'Natural Language :: German',
          'Operating System :: Unix',
          # 'Programming Language :: JavaScript',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation',
          'Programming Language :: Python :: Implementation :: CPython',
          # 'Programming Language :: Python :: Implementation :: PyPy',
          'Programming Language :: SQL',
          'Topic :: Internet',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',  # noqa
          'Topic :: Internet :: WWW/HTTP :: WSGI',
          'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries :: Application Frameworks',  # noqa
      ],
      author=author,
      author_email=author_email,
      url=url,
      keywords=keywords,
      license=license,
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      setup_requires=setup_requires,
      tests_require=tests_require,
      entry_points={
          'paste.app_factory': [
              'main = Huracán:main',
          ],
      },
      extras_require={
          'testing': tests_require,
          'development': development_requires,
          'docs': docs_require,
          },
)
