from setuptools import setup
from setuptools import find_packages

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name="TaxiFareStreamlit", version="1.0",
      description="taxifare streamlit",
      packages=find_packages(),
      include_package_data=True,  install_requires=requirements)
