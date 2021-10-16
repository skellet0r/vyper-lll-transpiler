import os
import pathlib

import setuptools

# install eth-brownie as a library
os.environ["BROWNIE_LIB"] = "1"

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text()
requires = (here / "requirements.txt").read_text().split()
dev_requires = (here / "requirements-dev.txt").read_text().split()

setuptools.setup(
    name="vyper-transpiler",
    version="0.1.0",
    description="Experimental Vyper LLL Transpiler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skellet0r/vyper-lll-transpiler",
    author="Edward Amor",
    author_email="edward.amor3@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="ethereum evm lll vyper yul",
    packages=["transpiler"],
    python_requires=">=3.9, <4",
    install_requires=[requirement for requirement in requires if "==" in requirement],
    extras_require={"dev": [requirement for requirement in dev_requires if "==" in requirement]},
    project_urls={
        "Bug Reports": "https://github.com/skellet0r/vyper-lll-transpiler/issues",
        "Source": "https://github.com/skellet0r/vyper-lll-transpiler",
    },
)
