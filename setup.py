from setuptools import find_packages, setup

with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='apex-legends',
    version='0.1.7',
    description='Python wrapper for https://apex.tracker.gg/ api.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/xcodinas/apex-legends',
    author='Xavier Codinas',
    author_email='xavier19966@gmail.com',
    license='MIT',
    packages=find_packages(exclude=('tests*',)),
    install_requires=requirements,
    extras_require={
        ":python_version<='3.4'": ['enum34>=1.1.6'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
)
