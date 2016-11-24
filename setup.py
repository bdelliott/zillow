from setuptools import find_packages, setup

setup(name='zillow',
      version='0.0.1',
      description='Zillow API scripts',
      author='Brian Elliott',
      author_email='bdelliott@gmail.com',
      license='MIT',
      install_requires=['requests'],
      namespace_packages=[],
      packages=find_packages('.'),
      include_package_data=True,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 2.7',
      ],
      entry_points={
        'console_scripts': ['zillow=zillow.cli:main']  
      }
)
