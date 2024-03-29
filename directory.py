import re
from collections import OrderedDict
from datetime import datetime


class Directory():
    """ A class used to build a directory data structure from a list of provided file paths. 
    The tree can be traversed through and items can be searched for within a directory. 
    The items can also be sorted either alphanumerically or by the date they were modified.

    Author
    ------
    Sean O'Hara

    Attributes
    ----------
    read_file: str
        The path of the file to read with the list of file paths.
            ex: ``'file_paths.txt'``

    path: str
        The path to set as the current directory (default is root ``'/'``).
            ex: ``'/shares/win7/Artbeats'``

    sort: str
        The sorting method used to order items.
            ``'Alphanumeric'`` (default) or ``'Date Modified'``

    Methods
    -------
    get_items(type_='All', search_term=None):
        Returns the files and/or folders in the current directory.
        
    step(direction, subdirectory=None):
        Steps in/out of a directory and updates the directory lists.
    """
    def __init__(self, read_file, path='/', sort='Alphanumeric'):
        self.read_file = read_file
        self.path = path
        self.sort = sort
        self._file_data = None
        self._file_regex = re.compile(
                '(?P<path>.*?\.?(?:264|flv|m2t|m2ts|mov|mp4|m4v|sdp|ts|aac|m4a|wav|bmp|gif|jpg|jpeg|tif|tiff|png|m3u8|'
                'm3u|pls|jspf|xspf|mpg|mpeg|mp1|mp2|mp3|m1v|m1a|m2a|mpa|mpv)) (?P<date>(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun),'
                ' \d{2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{4} \d{2}:\d{2}:\d{2}) GMT \d+\n', re.I
        )
        self._directory = OrderedDict()
        self._directory_lists = {'All': [], 'Files': [], 'Folders': []}

    @property
    def read_file(self):
        """ Get/set the read_file attribute and update the directory lists (except on init). """
        return self._read_file

    @read_file.setter
    def read_file(self, value):
        if not isinstance(value, str) or not value.endswith('.txt'):
            raise ValueError('Invalid read file attribute specified')
        self._read_file = value
        if hasattr(self, '_file_data'):  # block on init
            self._read_file_data()

    @property
    def path(self):
        """ Get/set the path attribute and update the directory lists (except on init). """
        return self._path

    @path.setter
    def path(self, value):
        if not isinstance(value, str):
            raise TypeError('Invalid path attribute specified')
        self._path = value
        if hasattr(self, '_directory'):  # block on init
            self._traverse_directory()

    @property
    def sort(self):
        """ Get/set the sort attribute and update the directory lists (except on init). """
        return self._sort

    @sort.setter
    def sort(self, value):
        if value not in ('Alphanumeric', 'Date Modified'):
            raise ValueError('Invalid sort attribute specified')
        self._sort = value
        if hasattr(self, '_file_data'):  # block on init
            self._parse_file_data()

    def get_items(self, type_='All', search_term=None):
        """ Returns the files and/or folders in the current directory. An optional
        search_term parameter may be specified to return a filtered list of items.

        Parameters
        ----------
        type_: str
            ``'All'`` (default), ``'Files'``, ``'Folders'``

        search_term: str
            Optional parameter
                ex: ``'.mp4'``

        Returns
        -------
        list
            The files and/or folders in the current directory.
        """
        if type_ not in ('All', 'Files', 'Folders'):
            raise ValueError('Invalid type parameter specified')
        if search_term and not isinstance(search_term, str):
            raise TypeError('Invalid search term parameter specified')

        if self._file_data is None:
            self._read_file_data()

        items = self._directory_lists[type_]            
        if not search_term:
            return items  # return unfiltered items
        else:
            if not items:
                raise AttributeError('No items to search')
            return [item for item in items if search_term.lower() in item.lower()]  # return filtered items

    def step(self, direction, subdirectory=None):
        """ Steps in/out of a directory and updates the directory lists.

        Parameters
        ----------
        direction: str
            ``'In'`` or ``'Out'``

        subdirectory: str
            Only required when direction parameter is ``'In'``
                ex: ``'Subdirectory 1'``

        Returns
        -------
        None
        """
        if direction not in ('In', 'Out'):
            raise ValueError('Invalid direction parameter specified')
        if direction == 'In' and (subdirectory is None or not isinstance(subdirectory, str)):
            raise ValueError('Missing or invalid subdirectory parameter specified')

        path_items = self._path.strip('/').split('/')
        if direction == 'In':
            path_items.append(subdirectory)  # add subdirectory to items
        else:
            del path_items[-1]  # delete last item
        self.path = '/' + '/'.join(path_items)

    def _read_file_data(self):
        try:
            with open(self._read_file, encoding='utf8') as f:
                self._file_data = f.read()
        except FileNotFoundError:
            raise AttributeError('File does not exist')
        self._parse_file_data()

    def _parse_file_data(self):
        # ex: [['shares', 'win7', 'Artbeats', '1920x1080-Artbeats-3-v2.mp4', 'Tue, 22 Oct 2013 15:48:42']]
        iter = re.finditer(self._file_regex, self._file_data)
        all_path_items = [file.group('path').split('/') + [file.group('date')] for file in iter]
        if self._sort == 'Date Modified':
            all_path_items.sort(key=lambda date: datetime.strptime(date[-1], '%a, %d %b %Y %H:%M:%S'), reverse=True)
        self._build_directory(all_path_items)
    
    def _build_directory(self, all_path_items):
        # ex: OrderedDict([('shares', {'win7': {'Artbeats': {'1920x1080-Artbeats-3-v2.mp4': 'File'}}})])
        self._directory.clear()
        for path_items in all_path_items:
            branch = self._directory
            for item in path_items[:-2]:  # -2 index to not include date modified
                branch = branch.setdefault(item, OrderedDict())
            branch[path_items[-2]] = 'File'  # mark all files w/ 'File' tag string to differentiate from subdirectory
        self._traverse_directory()

    def _traverse_directory(self):
        current_branch = self._directory  # initialize
        for item in self._path.strip('/').split('/'):
            if item in current_branch:
                current_branch = current_branch[item]  # traverse through directory
            else:
                raise AttributeError('Invalid path specified')
        self._build_directory_lists(current_branch)

    def _build_directory_lists(self, current_branch):
        self._directory_lists = {type_: [] for type_ in self._directory_lists}  # reinitialize
        for item in current_branch:
            if current_branch[item] == 'File':
                self._directory_lists['Files'].append(item)  # files only
            else:
                self._directory_lists['Folders'].append(item)  # folders only
            self._directory_lists['All'].append(item)  # files and folders
        if self._sort == 'Alphanumeric':
            self._directory_lists = {type_: sorted(self._directory_lists[type_], key=lambda item: item.lower()) for type_ in self._directory_lists}
