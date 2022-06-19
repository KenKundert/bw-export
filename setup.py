from setuptools import setup

with open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name = 'bw-export',
    version = '0.0.0',
    description = 'export Avendesora accounts to BitWarden',
    long_description = readme,
    long_description_content_type = 'text/x-rst',
    author = "Ken Kundert",
    author_email = 'bw-export@nurdletech.com',
    url = 'http://nurdletech.com/linux-utilities/bw-export',
    download_url = 'https://github.com/kenkundert/bw-export/tarball/master',
    license = 'GPLv3+',
    zip_safe = True,
    scripts = 'bw-csv-export bw-json-export'.split(),
    install_requires = 'inform>=1.25'.split(),
    python_requires = '>=3.6',
    keywords = 'personal finance'.splitlines(),
    classifiers = [
        'Development Status :: 4 - Beta',
        #'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Utilities',
    ],
)
