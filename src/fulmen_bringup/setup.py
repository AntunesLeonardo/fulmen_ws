import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'fulmen_bringup'

setup(
    name=package_name,
    version='0.2.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='AntunesLeonardo',
    author_email='leonardo.antunes.segment155@passinbox.com',
    maintainer='AntunesLeonardo',
    maintainer_email='leonardo.antunes.segment155@passinbox.com',
    description='Package containing main launchers and configuration files for general definitions for Fulmen mobile robot.',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
