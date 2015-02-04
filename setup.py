"""
    Flask-Keen
    ----------

    Thin wrapper around KeenClient

    Links
    `````
    * `development version
    <https://github.com/pmarti/flask-keen>`_
"""
from setuptools import setup


setup(name='Flask-Keen',
      version='0.1.0',
      url='https://github.com/pmarti/flask-keen',
      license='MIT',
      author='Pablo Marti',
      author_email='pmargam@gmail.com',
      description='Keen API for Flask',
      long_description=__doc__,
      py_modules=['flask_keen'],
      zip_safe=False,
      platforms='any',
      install_requires=['Flask'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ])