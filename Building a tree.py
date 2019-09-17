Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def print_tree(height):
    i = 0
    num_spaces = int(height - 1)
    tree = (" " * num_spaces) + "#" + (" " * num_spaces) + "\n"
    num_hashes = 1 
    while i < (height - 1):
        num_spaces -= 1
        num_hashes += 2
        tree += (" " * num_spaces) + ("#" * num_hashes) + (" " * num_spaces) + "\n"
        i += 1
    print(tree)
    return tree

