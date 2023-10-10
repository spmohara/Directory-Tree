# File Directory Tree in Python

# Overview
This application was created for a work project, which involved a device driver communicating 
with an [Extron](https://www.extron.com/) streaming media player device. The request was to build a file directory tree 
based on a list of file paths returned upon sending a query command to the Extron device. These
paths specified the location of each file stored on the unit. The user requested to view, navigate, 
search, sort, and eventually select files to play using an Extron UI within an AV control system.

# Description
A [class](directory.py) in Python used to build a file directory tree from a list of provided [file paths](file_paths.txt). 
The tree can be traversed through and items can be searched for within a directory. 
The items can also be sorted either alphanumerically or by the date they were modified.

# Usage
## Instantiation
```python
from directory import Directory

directory = Directory(read_file_name='file_paths.txt', path='/shares/win7/Artbeats', sort_by='Alphanumeric')
```

## Attributes
### Get current directory path
```python
directory.path
```

### Set current directory path
```python
directory.path = '/shares/win7/Audio'
```

### Get current sorting method of items
```python
directory.sort_by
```

### Sort items alphanumerically
```python
directory.sort_by = 'Alphanumeric'
```

### Sort items by date modified
```python
directory.sort_by = 'Date Modified'
```

## Methods
### Get files in current directory
```python
directory.get_items(type_='Files')
```

### Get folders in current directory
```python
directory.get_items(type_='Folders')
```

### Get files and folders in current directory
```python
directory.get_items()
```

### Search for files in current directory
```python
directory.get_items(type_='Files', search_term='Mbps')
```

### Search for folders in current directory
```python
directory.get_items(type_='Folders', search_term='short')
```

### Search for files and folders in current directory
```python
directory.get_items(search_term='test')
```

### Step into subdirectory
```python
directory.step(direction='In', subdirectory='withMusic')
```

### Step out of current directory
```python
directory.step(direction='Out')
```

## Workflow
Please reference the provided [test file](test_directory.py) for a workflow example.

# Dependencies
Python 3.x

# License
Licensed under the [MIT License](LICENSE)
