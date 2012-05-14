from distutils.core import setup

setup(
    name='chef_install',
    version='0.3.0',
    url='https://github.com/exslim/chef-install',
    license='BSD',
    author='Igor Gumenyuk',
    author_email='me@exslim.net',
    description='Tool for installing Chef cookbooks on local machine',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=['chef_install'],
    platforms='Linux',
    entry_points={
              'console_scripts': [
                  'chef-install = chef_install.app:main',
              ]
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
