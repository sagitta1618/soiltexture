# to build run : python3 setup.py sdist bdist_wheel
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="soiltexture",
    version="1.0.4", # CHANGE HERE
    author="sagitta1618",
    description="Soil texture classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sagitta1618/soiltexture",
    packages=setuptools.find_packages(),
    install_requires=['matplotlib'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
