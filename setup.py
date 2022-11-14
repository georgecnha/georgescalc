from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="georgescalc",
    version="0.0.1",
    author="George Pontes da Cunha",
    author_email="george.pontes02@gmail.com",
    description="Mix of functions",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/georgecnha/georges_calc",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)