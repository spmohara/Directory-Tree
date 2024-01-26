# Directory Tree

# Overview
This application was created for a work project, which involved a device driver communicating with an [Extron](https://www.extron.com/) streaming media player device. The request was to build a directory tree based on a list of file paths returned upon sending a query command to the Extron device. These paths specified the location of each file stored on the unit. The user requested to view, navigate, search, sort, and eventually select files to play using an Extron UI within an AV control system.

Example list of file paths:
```
shares/win7/Artbeats/test6.m3u Wed, 29 Jul 2015 18:43:07 GMT 183
shares/win7/Artbeats/Thumbs.db Wed, 13 Nov 2013 16:21:32 GMT 171520
shares/win7/Artbeats/withMusic/Artbeats_1_25M_music_fast.mp4 Wed, 17 Feb 2016 16:23:14 GMT 318342026
shares/win7/Artbeats/withMusic/Artbeats_1_25M_music_fast_1.MP4 Wed, 17 Feb 2016 16:23:14 GMT 318342026
shares/win7/Artbeats/withMusic/Artbeats_2_25M_music_fast.mp4 Wed, 17 Feb 2016 17:16:34 GMT 265777386
shares/win7/Artbeats/withMusic/Artbeats_3_25M_music_fast.mp4 Wed, 17 Feb 2016 20:32:34 GMT 253864857
shares/win7/Artbeats/withMusic/Artbeats_4_25M_music_fast.mp4 Wed, 17 Feb 2016 17:32:40 GMT 208844345
shares/win7/Artbeats/withMusic/Artbeats_5_25M_music_fast.mp4 Wed, 17 Feb 2016 20:39:10 GMT 214242172
shares/win7/Artbeats-frames/Artbeats_1.mp4 Wed, 17 Feb 2016 15:43:03 GMT 634855018
shares/win7/Artbeats-frames/Artbeats_1.MPG Mon, 24 May 2010 11:17:48 GMT 495606164
```

# Description
A class in Python used to build a directory data structure from a list of provided file paths. The tree can be traversed through and items can be searched for within a directory. The items can also be sorted either alphanumerically or by the date they were modified.

<img src="images/Directory-Tree-icon.jpg" width="200" height="200">

# Usage
## Instantiation
```python
from directory import Directory

my_directory = Directory(read_file='file_paths.txt', path='/shares/win7/Artbeats', sort='Alphanumeric')
```

## Attributes
### Get read file path
```python
my_directory.read_file
```

### Set read file path
```python
my_directory.read_file = 'file_paths.txt'
```

### Get current directory path
```python
my_directory.path
```

### Set current directory path (default is root ``'/'``)
```python
my_directory.path = '/shares/win7/Audio'
```

### Get sorting method of items
```python
my_directory.sort
```

### Set sorting method of items as alphanumeric (default)
```python
my_directory.sort = 'Alphanumeric'
```

### Set sorting method of items as date modified
```python
my_directory.sort = 'Date Modified'
```

## Methods
### Get files in current directory
```python
my_directory.get_items('Files')
```

### Get folders in current directory
```python
my_directory.get_items('Folders')
```

### Get files and folders in current directory
```python
my_directory.get_items()
```

### Search for files in current directory
```python
my_directory.get_items('Files', search_term='Mbps')
```

### Search for folders in current directory
```python
my_directory.get_items('Folders', search_term='short')
```

### Search for files and folders in current directory
```python
my_directory.get_items(search_term='test')
```

### Step into subdirectory
```python
my_directory.step('In', subdirectory='withMusic')
```

### Step out of current directory
```python
my_directory.step('Out')
```

## Workflow
Please reference the provided [test file](test_directory.py) for a workflow example.

# Dependencies
Python 3.x

# License
Licensed under the [MIT License](LICENSE)
