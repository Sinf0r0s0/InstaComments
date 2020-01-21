import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="instacomments",
    version="0.0.7",
    author="Sinf0r0s0",
    author_email="noteprof213@gmail.com",
    description="Small code to returns a list with  comments of an Instagram post.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/Sinf0r0s0/InstaComments",
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
