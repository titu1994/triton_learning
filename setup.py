from setuptools import setup, find_packages
from importlib import util

# Load the module
spec = util.spec_from_file_location("version", "triton_learn/version.py")
version_module = util.module_from_spec(spec)
spec.loader.exec_module(version_module)

# Extract the version string
version = version_module.version

setup(
    name='triton_learn',
    version=version,
    description='A Python library for...',
    long_description='...',
    author='Somshubra Majumdar',
    author_email='titu1994@gmail.com',
    url='https://github.com/your-username/my-python-library',
    packages=find_packages(),
    install_requires=[
        # List of dependencies required by your library
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)