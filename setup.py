from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable'
    'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 7',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: '
]

setup(
  name='Helloprinterpackage',
  version='0.0.1',
  description='A basic hello printer package',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Asher Thomas Abraham',
  author_email='achutomonline@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Hello', 
  packages=find_packages(),
  install_requires=[''] 
)