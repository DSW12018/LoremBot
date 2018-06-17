import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

 install_requires = [
    'requests==2.19.1',
    'SQLAlchemy==1.2.8'
]

setuptools.setup(
    name="lorem-bot",
    version="0.0.1",
    author="DSW12018",
    author_email="thiagoflames@gmail.com",
    license='MIT',
    description="A bot framework for devolopers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DSW12018/LoremBot",
    packages=setuptools.find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=install_requires,
    classifiers=(
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        "Operating System :: OS Independent",
    ),
)
