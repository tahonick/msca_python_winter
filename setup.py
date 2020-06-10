import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ravescovi", # Replace with your own username
    version="0.0.1",
    author="Rafael Vescovi, MSCA Students",
    author_email="ravescovi@gmail.com",
    description="A baseline package for MSCA class",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ravescovi/msca_python_winter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)