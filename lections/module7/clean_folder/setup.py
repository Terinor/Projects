from setuptools import setup

setup(
    name='clean_folder',
    version='0.1',
    py_modules=['clean_folder.clean'],
    entry_points={
        'console_scripts': ['clean-folder = clean_folder.clean:main'],
    },
)
