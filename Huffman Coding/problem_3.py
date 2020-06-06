import heapq
import sys


class Node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None


    def __lt__(self, other):
        return self.frequency < other.frequency


def get_sorted_list_of_nodes_with_frequencies(data):
    character_codes = [0] * 128
    nodes = list()

    heapq.heapify(nodes)

    for character in data:
        character_codes[ord(character)] += 1

    for index, code in enumerate(character_codes):
        if code > 0:
            node = Node(chr(index), code)
            heapq.heappush(nodes, node)

    return nodes


def huffman_encoding(data):
    if data == "" or data is None:
        return data, None

    nodes = get_sorted_list_of_nodes_with_frequencies(data)
    build_huffman_tree(nodes)
    root = heapq.heappop(nodes)
    return get_binary_code(data, root), root


def get_binary_code(data, root):
    character_to_code = dict()
    get_binary_code_map(root, character_to_code, "")
    for char in character_to_code:
        data = data.replace(char, character_to_code[char])

    return data


def get_binary_code_map(node, characterToCode, code):

    if node.left is None and node.right is None:
        characterToCode[node.character] = code
        return

    if node.left is not None:
        get_binary_code_map(node.left, characterToCode, code + "0")

    if node.right is not None:
        get_binary_code_map(node.right, characterToCode, code + "1")


def build_huffman_tree(nodes):
    if len(nodes) == 1 and nodes[0].character is None:
        return

    if len(nodes) != 0:
        node1 = heapq.heappop(nodes)
        frequency1 = node1.frequency
    else:
        node1 = None
        frequency1 = 0

    if len(nodes) != 0:
        node2 = heapq.heappop(nodes)
        frequency2 = node2.frequency
    else:
        node2 = None
        frequency2 = 0

    node = Node(None, frequency1 + frequency2)
    node.left = node1
    node.right = node2

    heapq.heappush(nodes, node)

    build_huffman_tree(nodes)


def huffman_decoding(data, root):
    if data == "" or data is None:
        return data

    if root is None:
        return data
    decoded_string = ""
    index = 0

    while index is not len(data):
        string, index = decode_bit(data, index, root, decoded_string)
        decoded_string += string

    return decoded_string


def decode_bit(data, index, node, decoded_string):
    if node.left is None and node.right is None:
        return node.character, index

    if data[index] == '0':
        index = index + 1
        return decode_bit(data, index, node.left, decoded_string)

    if data[index] == '1':
        index = index + 1
        return decode_bit(data, index, node.right, decoded_string)

if __name__ == "__main__":
    codes = {}

    # Test case 1: with correct input
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # prints The size of the encoded data is: 36
    # The content of the encoded data is:  1101011101111011101111001000010111001011010001111011110100001010100001

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # prints The size of the decoded data is: 69
    # prints The content of the encoded data is: The bird is the word


    # Test case 2: with empty string
    a_great_sentence = ""

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    # returns empty data and None

    if tree is not None:
      print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
      print("The content of the encoded data is: {}\n".format(encoded_data))

      decoded_data = huffman_decoding(encoded_data, tree)

      print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
      print("The content of the encoded data is: {}\n".format(decoded_data))


    # Test case 3: with None string
    a_great_sentence = None

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    # returns None data and None for tree

    if tree is not None:
        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}\n".format(decoded_data))


    # Test case 3: with string containing single character multiple times
    a_great_sentence = "aaaaaa"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    # returns None data and None for tree

    if tree is not None:
        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}\n".format(decoded_data))

    # Test case 3: with large string containing all the characters
    a_great_sentence = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    # returns None data and None for tree

    if tree is not None:
        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}\n".format(decoded_data))
