from setuptools import setup, find_packages

setup(
    name='jupyter-repo2docker',
    version='0.4.1',
    install_requires=[
        'docker',
        'traitlets',
        'python-json-logger',
        'escapism',
        'jinja2'
    ],
    python_requires='>=3.4',
    author='Yuvi Panda',
    author_email='yuvipanda@gmail.com',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'jupyter-repo2docker = repo2docker.__main__:main',
        ]
    },
)
