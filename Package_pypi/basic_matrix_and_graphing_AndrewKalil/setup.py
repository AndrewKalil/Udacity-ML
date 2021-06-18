from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Indented Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Aproved :: MIT License',
    'Programming Language :: Python :: 3'
]

with open("README.md") as fh:
    long_description = fh.read()

setup(name='basicLinalgAKal',
      author='Andrew Kalil',
      author_email='andrew_kalil@hotmail.com',
      version='0.1',
      description='Basic matrix operations and graphing functions',
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='MIT',
    #   classifiers=classifiers,
      keywords='Matrix Linear Algebra',
      packages=find_packages(),
      zip_safe=False)
