# coding:utf-8
from setuptools import setup, find_packages

packages = find_packages('typeidea')
print(packages)

setup(
    name='typeidea',
    version='0.1',
    decription='Blog System base on Django',
    author='jummy',
    author_email='929440925@qq.com',
    url='https://www.jummy.top',
    packages=packages,
    package_dir={'':'typeidea'},
    #package_data={'typeidea'[
    #    'themes/default/statis/js/*.js',
    #]},
    include_package_data=True,
    install_requires=[
        'django==1.11.8',
        'django-autocomplete-light==3.2.10',
        'hiredis==0.2.0',
        'redis==2.10.6',
        'django-ckeditor==5.3.1',
        'django-debug-toolbar==1.9.1',
        'django-markdownx==2.0.22',
        'mysqlclient==1.3.12',
        'Pillow==5.0.0',
        'xadmin==0.6.1',
        'djangorestframework==3.7.7',
        'django-reversion==2.0.12',
        'Markdown==2.6.11',
        'django-redis==4.8.0',
        'coreapi==2.3.3',
        'gunicorn==19.7.1',
    ],
    scripts=[
        'typeidea/manage.py',
    ],
)
