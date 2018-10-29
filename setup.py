import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ediblepwn',
    version='1.0',
    author='Chris Doucette',
    author_email='chrisdoucette15@gmail.com',
    description='API Wrapper for haveibeenpwned.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/ediblesushi/ediblepwn',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
