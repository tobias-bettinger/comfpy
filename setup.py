import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="comfpy", # Replace with your own username
    version="0.0.1",
    author="Tobias Bettinger, Philipp Leibner",
    author_email="tob.bettinger@googlemail.com",
    description="comfort evaluation scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/comfpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)