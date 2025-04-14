# Image Splitter

This project is an image splitter application built using PyQt5 and Pillow. It allows users to select an image file and split it into smaller tiles.

## Features

- Select an image file to split.
- Specify an optional output folder name for the tiles.
- Split the image into tiles of a specified size.

## Requirements

- Python 3.x
- PyQt5
- Pillow

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd image-splitter
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/sliceConverter.py
```

## Testing

Unit tests for the application can be found in the `tests` directory. To run the tests, use:
```
pytest tests/test_sliceConverter.py
```

## License

This project is licensed under the MIT License.