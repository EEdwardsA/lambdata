import setuptools

REQUIRED = ["numpy", "pandas"]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata_eedwardsa", # Replace with your own username
    version="0.0.2",
    author="EEdwardsA",
    description="A collection of data science functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EEdwardsA/lambdata",
    packages=setuptools.find_packages(),
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)