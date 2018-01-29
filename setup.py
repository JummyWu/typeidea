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
    ],
    scripts=[
        'typeidea/manage.py',
    ],
)
