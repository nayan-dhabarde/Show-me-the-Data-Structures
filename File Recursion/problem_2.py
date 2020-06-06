import os

def find_files(suffix, path):
    output = []

    if path is None:
        return

    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
        else:
            return []
    else:
        if not os.path.isdir(path):
            return
        dir_list = os.listdir(path)
        for directory in dir_list:
            output_list = find_files(suffix, os.path.join(path, directory))
            for single_path in output_list:
                output.append(single_path)

    return output


# Test case 1: With existing directory and correct format
print(find_files(".c", "testdir"))
# Output:
# ['testdir//subdir1//a.c',
# 'testdir//subdir3//subsubdir1//b.c',
# 'testdir//subdir5//a.c',
# 'testdir//t1.c']

# Test case 2:  With existing directory and different format
print(find_files(".h", "testdir"))
# Output:
# ['testdir//subdir1//a.h',
# 'testdir//subdir3//subsubdir1//b.h',
# 'testdir//subdir5//a.h',
# 'testdir//t1.h']

# Test case 3:  With non-existing directory and correct format
print(find_files(".c", "tesir"))
# Output:
# None

# Test case 4: With non-existing directory and empty format
print(find_files("", "tesir"))
# Output:
# None

# Test case 5: With non-existing directory and empty format
print(find_files("", ""))
# Output:
# None

# Test case 6: With None values
print(find_files(None, None))
# Output:
# None




