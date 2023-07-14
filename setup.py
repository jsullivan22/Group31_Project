import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]
setuptools.setup(
    name="DummySignalGen", 
    version="0.0.1",
    author="James Sullivan, Xiyuan Li",
    author_email1="jms2561@columbia.edu",
    author_email2="xli2522@uwo.ca",
    description="Package for generating dummy signals.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='GNU',
    url="",
    install_reqs = REQUIREMENTS,
    packages=setuptools.find_packages(),
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
