import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="demoGJASonos", # Replace with your own username
    version="0.0.1",
    author="Sonos Inc",
    author_email="manushi.sheth@sonos.com",
    description="Trial package for git-jenkins connection",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
