import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """    
    path_list = []
    
    return _find_files(suffix, path, path_list)

def _find_files(suffix, path, path_list):

    # find all the files and directory under the current *path*
    sub = os.listdir(path)
    # append path of the files end with suffix to the path list
    for element in sub:
        element_path = os.path.join(path,element)
        if element_path.endswith(suffix):
            path_list.append(element_path)
        elif os.path.isdir(element_path):
            _find_files(suffix, element_path,path_list)
    
    return path_list


# Test Case
path = "./testdir"
suffix = ".c"
print(find_files(suffix, path))
# Expected result: ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']
suffix2 = ".h"
print(find_files(suffix2, path))
# Expected result: ['./testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h', './testdir/subdir1/a.h']
suffix3 = ".abc"
print(find_files(suffix3, path))
# Expected result: []