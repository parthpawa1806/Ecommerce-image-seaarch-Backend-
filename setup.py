from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='your_project_name',
    version='1.0',
    packages=['your_project_name'],
    include_package_data=True,
    install_requires=requirements,
    license_files=('LICENSE.txt',),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        # Add any other relevant classifiers
    ],
)


