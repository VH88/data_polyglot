import setuptools

with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name='data_polyglot',
    python_requires=">=3.7",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(include=['data_polyglot*']),
    include_package_data=True,
    version='1.0.0',
    description='Convenient way to model JSON payload and response with least lines of code to test API',
    author='Vadim Harenco',
    author_email='vharenco@gmail.com',
    url='https://github.com/VH88/data-polyglot',
    keywords=['testing', 'test automation', 'API', 'payload', 'serializer', 'serialize', 'deserialize', 'json'],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: '
        'Libraries :: Python Modules',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
    ]
)