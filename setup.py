from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='image_reccomender',
    version='1.0',
    packages=['image_reccomender'],
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        # Add any other relevant classifiers
    ],
)
