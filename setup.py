from setuptools import setup, find_packages

setup(
    name='ByteBack',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # list your project's dependencies here
        # they will be installed alongside your package
    ],
    # other metadata
    author='Your Name',
    author_email='your.email@example.com',
    description='A tool for decompiling executables and analyzing their source.',
    license='MIT',
    keywords='decompile exe reverse-engineering',
    url='https://github.com/Suffix30/ByteBack',  # project home page
)
