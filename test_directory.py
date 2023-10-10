from directory import Directory
import logging

directory = Directory(read_file_name='file_paths.txt', path='/shares/win7/Artbeats', sort_by='Alphanumeric')

"""Show initial directory items"""
print('Initial Directory Path:', directory.path, '\n')
#print('Files in Initial Directory:', directory.get_items(type_='Files'), '\n')
#print('Folders in Initial Directory:', directory.get_items(type_='Folders'), '\n')
print('Files & Folders in Initial Directory:', directory.get_items(), '\n')

"""Search initial directory items"""
#print('Filtered Files in Initial Directory:', directory.get_items(type_='Files', search_term='Mbps'), '\n')
#print('Filtered Folders in Initial Directory:', directory.get_items(type_='Folders', search_term='short'), '\n')
print('Filtered Files & Folders in Initial Directory:', directory.get_items(search_term='test'), '\n')

"""Step in/out of directory"""
#directory.step(direction='In', subdirectory='withMusic')
directory.step(direction='Out')
print('Subdirectory Path:', directory.path, '\n')
print('Files & Folders in Subdirectory:', directory.get_items(), '\n')

"""Search subdirectory items"""
print('Filtered Files & Folders in Subdirectory:', directory.get_items(search_term='temp'), '\n')

"""Change current directory"""
directory.path = '/shares/win7/Audio'
print('New Directory Path:', directory.path, '\n')
print('Files & Folders in New Directory:', directory.get_items(), '\n')

"""Sort new directory items by date modified"""
directory.sort_by = 'Date Modified'
print('Files & Folders in New Directory by Date Modified:', directory.get_items(), '\n')
