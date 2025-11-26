from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="brainpy",
    version="0.1.0",
    author="Dmitry Seksov",
    author_email="dmitrypidaras89@gmail.com",
    description="A library that converts Brainfuck code to Python and executes it",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/silentbyte69/brainpy",
    project_urls={
        "Homepage": "https://github.com/silentbyte69/brainpy",
        "Documentation": "https://github.com/silentbyte69/brainpy#readme",
        "Repository": "https://github.com/silentbyte69/brainpy",
        "Bug Tracker": "https://github.com/silentbyte69/brainpy/issues",
        "Changelog": "https://github.com/silentbyte69/brainpy/releases",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Education",
        "Topic :: Utilities",
    ],
    packages=find_packages(include=["brainpy", "brainpy.*"]),
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=3.0",
            "black>=22.0",
            "flake8>=5.0",
            "mypy>=1.0",
            "twine>=4.0",
            "build>=0.10.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "brainpy=brainpy.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords=[
        "brainfuck",
        "interpreter",
        "compiler",
        "esolang",
        "programming-language",
        "code-conversion",
    ],
)
