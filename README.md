# ZipDir

Zip dir is a small library for zipping directories recursively into zip files.

## Installation

    $ pip install zipdir

## Usage

Either obtain the binary data

```python
    zipBits = zipDirectory( '/path/to/directory' )
```


or else, specify an output file

```python
    zipDirectory( '/path/to/directory', outputFile = '/my/file.zip' )
```


Enjoy!
