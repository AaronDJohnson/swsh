import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="swsh",
    version="0.0.1",
    author="Aaron Johnson",
    author_email="johnsoad@uwm.edu",
    description="A spectral decomposition spin-weighted spheroidal harmonic calculator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AaronDJohnson/swsh",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy>=1.19.0',
        'scipy>=1.6.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)