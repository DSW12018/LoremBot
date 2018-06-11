import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lorem-bot",
    version="0.0.1",
    author="Thiago Pereira",
    author_email="thiagoflames@gmail.com",
    license='MIT',
    description="A bot framework for devolopers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DSW12018/LoremBot",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),

)
