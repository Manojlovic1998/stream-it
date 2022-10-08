# stream-it

Python CLI tool for downloading videos.

## MVP 1.0.0

- Features:
  - [ ] Use json file data format to download, name, and save videos into specific directory.
  - [ ] Download the videos from multiple platforms.
  - [ ] Change network MAC address before running the downloads.
  - [ ] Revert to original MAC address once downloads have completed.

## Tool Usage

### Exceptions

This CLI tool is built with the help of _click_ lib. The _click_ library has built in exception handlers which are used to show error messages or/and abort command execution.

# Technologies

- [Pipenv](https://pipenv.pypa.io/en/latest/)
  - Used for handling the python shell development environment.
- [JSON Crack](https://jsoncrack.com/)
  - Used to preview the [stdin-example.json]("./stdin-example.json") abstract input example for the minimum viable product.
- [Click](https://click.palletsprojects.com/en/8.1.x/#documentation)
  - Used to speed up the development of cli tool interface. It comes with really nice pre-baked solutions.
- [JSON Schema](https://json-schema.org/implementations.html)
  - Used to validate the json input file schema.
