from directory import Directory

my_directory = Directory(read_file='file_paths.txt', path='/shares/win7/Artbeats', sort='Alphanumeric')

"""Show initial directory items"""
print('Initial Directory Path:', my_directory.path, '\n')
#print('Files in Initial Directory:', my_directory.get_items('Files'), '\n')
#print('Folders in Initial Directory:', my_directory.get_items('Folders'), '\n')
print('Files & Folders in Initial Directory:', my_directory.get_items(), '\n')

"""Search initial directory items"""
#print('Filtered Files in Initial Directory:', my_directory.get_items('Files', search_term='Mbps'), '\n')
#print('Filtered Folders in Initial Directory:', my_directory.get_items('Folders', search_term='short'), '\n')
print('Filtered Files & Folders in Initial Directory:', my_directory.get_items(search_term='test'), '\n')

"""Step in/out of directory"""
#my_directory.step('In', subdirectory='withMusic')
my_directory.step('Out')
print('Subdirectory Path:', my_directory.path, '\n')
print('Files & Folders in Subdirectory:', my_directory.get_items(), '\n')

"""Search subdirectory items"""
print('Filtered Files & Folders in Subdirectory:', my_directory.get_items(search_term='temp'), '\n')

"""Change current directory"""
my_directory.path = '/shares/win7/Audio'
print('New Directory Path:', my_directory.path, '\n')
print('Files & Folders in New Directory:', my_directory.get_items(), '\n')

"""Sort new directory items by date modified"""
my_directory.sort = 'Date Modified'
print('Files & Folders in New Directory by Date Modified:', my_directory.get_items(), '\n')
