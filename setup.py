from setuptools import setup, find_packages
setup(
    name="image_preprocess",
    version="0.1.0",
    packages=find_packages(),
    scripts=['src/preprocessing.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['opencv_python>=3.2.0',
                    'numpy>=1.12.0'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
    },

    # metadata for upload to PyPI
    author="Hsu",
    author_email="Hsuxu820@gmail.com",
    description="This is a image processing library",
    license="PSF",
    keywords="hello world example examples",
    url="https://github.com/Hsuxu/Image-preprocessing",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)
