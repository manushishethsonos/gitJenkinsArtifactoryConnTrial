from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="demo", # Replace with your own username
    version="0.0.1",
    author="Sonos Inc",
    author_email="manushi.sheth@sonos.com",
    description="Trial package for git-jenkins connection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
