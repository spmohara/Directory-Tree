# Directory Tree

# Overview
This application was created for a work project, which involved a device driver communicating 
with an [Extron](https://www.extron.com/) streaming media player device. The request was to build a directory tree 
based on a list of file paths returned upon sending a query command to the Extron device. These
paths specified the location of each file stored on the unit. The user requested to view, navigate, 
search, sort, and eventually select files to play using an Extron UI within an AV control system.

# Description
A [class](directory.py) in Python used to build a directory tree from a list of provided [file paths](file_paths.txt). 
The tree can be traversed through and items can be searched for within a directory. 
The items can also be sorted either alphanumerically or by the date they were modified.

# Usage
## Instantiation
```python
from directory import Directory

my_directory = Directory(file_name='file_paths.txt', path='/shares/win7/Artbeats', sort='Alphanumeric')
```

## Attributes
### Get current directory path
```python
my_directory.path
```

### Set current directory path
```python
my_directory.path = '/shares/win7/Audio'
```

### Get current sorting method of items
```python
my_directory.sort
```

### Sort items alphanumerically
```python
my_directory.sort = 'Alphanumeric'
```

### Sort items by date modified
```python
my_directory.sort = 'Date Modified'
```

## Methods
### Get files in current directory
```python
my_directory.get_items(type_='Files')
```

### Get folders in current directory
```python
my_directory.get_items(type_='Folders')
```

### Get files and folders in current directory
```python
my_directory.get_items()
```

### Search for files in current directory
```python
my_directory.get_items(type_='Files', search_term='Mbps')
```

### Search for folders in current directory
```python
my_directory.get_items(type_='Folders', search_term='short')
```

### Search for files and folders in current directory
```python
my_directory.get_items(search_term='test')
```

### Step into subdirectory
```python
my_directory.step(direction='In', subdirectory='withMusic')
```

### Step out of current directory
```python
my_directory.step(direction='Out')
```

## Workflow
Please reference the provided [test file](test_directory.py) for a workflow example.

# Dependencies
Python 3.x

# License
Licensed under the [MIT License](LICENSE)
