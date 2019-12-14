from setuptools import find_packages, setup


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='django-allauth-d120',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='AGPL',
    description='Allauth provider for the D120 SSO',
    long_description='README.md',
    url='https://github.com/d120/django-allauth-d120',
    author='ckleemann',
    author_email='ckleemann@d120.de',
    install_requires=requirements,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)