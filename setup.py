"""
Simple Date Calculator
"""


import os
from setuptools import setup


def read(frame):
    return open(os.path.join(os.path.dirname(__file__), frame)).read()


setup(
    name="date-calculator",
    version='0.0.1',
    url='https://github.com/engine-treasure/date-calculator',
    license='MIT',
    author='Engine Treasure',
    author_email='enginechen07@gmail.com',
    description=read("README"),
    # packages=[],
    scripts=['bin/date-cal'],
    # include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['click'],
    # classifiers=[
    #     # As from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    #     #'Development Status :: 1 - Planning',
    #     #'Development Status :: 2 - Pre-Alpha',
    #     #'Development Status :: 3 - Alpha',
    #     'Development Status :: 4 - Beta',
    #     #'Development Status :: 5 - Production/Stable',
    #     #'Development Status :: 6 - Mature',
    #     #'Development Status :: 7 - Inactive',
    #     'Programming Language :: Python',
    #     'Programming Language :: Python :: 2',
    #     #'Programming Language :: Python :: 2.3',
    #     #'Programming Language :: Python :: 2.4',
    #     #'Programming Language :: Python :: 2.5',
    #     'Programming Language :: Python :: 2.6',
    #     'Programming Language :: Python :: 2.7',
    #     #'Programming Language :: Python :: 3',
    #     #'Programming Language :: Python :: 3.0',
    #     #'Programming Language :: Python :: 3.1',
    #     #'Programming Language :: Python :: 3.2',
    #     #'Programming Language :: Python :: 3.3',
    #     'Intended Audience :: Developers',
    #     'Intended Audience :: System Administrators',
    #     'License :: OSI Approved :: BSD License',
    #     'Operating System :: OS Independent',
    #     'Topic :: System :: Systems Administration',
    # ]
)
