# ByteBack

ByteBack is an educational tool designed to decompile executable files, identify their source programming language, and outline the prerequisites needed for further development and analysis in Visual Studio Code. This project is open-source and intended strictly for educational purposes.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To install and run ByteBack, you'll need the following:

- Python 3.8 or higher
- pip (Python package installer)
- Visual Studio Code (or any IDE that supports Python development)
- setuptools (Required for installing dependencies, usually included with pip)

### Installing

Follow these steps to get your development environment set up:

1. Clone the repository:
```
git clone https://github.com/Suffix30/ByteBack.git
```

2. Navigate to the cloned directory:
```
cd ByteBack
```

3. Create a virtual environment:
```
python -m venv env
```

4. Activate the virtual environment:

On Windows:
```
env\Scripts\activate
```

On Unix or MacOS:
```
source env/bin/activate
```

5. Install the required dependencies:
```
pip install -r requirements.txt
```

Make sure that your `requirements.txt` file includes all necessary packages.

## Running Tests

To run automated tests for ByteBack, navigate to the project directory and execute:

```
pytest
```

Make sure you have `pytest` installed, which can be included in your `requirements.txt` file.

## Contributing

Contributions are what make the open-source community such a fantastic place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Authors

* **Your Name** - *Initial work* - [Suffix30](https://github.com/Suffix30)

See also the list of [contributors](https://github.com/Suffix30/ByteBack/contributors) who have participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

## Disclaimer

This project is for educational purposes only. Please ensure you have the right to decompile the software you are testing with ByteBack.
