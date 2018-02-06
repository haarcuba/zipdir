from setuptools import setup, find_packages

README = 'zip entire directories recursively'

requires = []
tests_require = []

setup(name='zipdir',
      version='0.1.2',
      description=README,
      long_description=README,
      url='https://github.com/haarcuba/zipdir',
      classifiers=[
          "Programming Language :: Python",
      ],
      author='Yoav Kleinberger',
      author_email='haarcuba@gmail.com',
      keywords='zip',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      )
