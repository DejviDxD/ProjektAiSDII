import heapq
from collections import defaultdict, Counter


class Huffman:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    # Obliczanie częstości występowania każdego znaku w tekście
    frequency = Counter(text)

    # Tworzenie kolejki priorytetowej z węzłami
    priority_queue = [Huffman(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    # Budowanie drzewa Huffmana
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged = Huffman(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(priority_queue, merged)

    return priority_queue[0] if priority_queue else None


def generate_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + '0', codebook)
        generate_codes(node.right, prefix + '1', codebook)
    return codebook


def huffman_encoding(data):
    tree = build_huffman_tree(data)
    codebook = generate_codes(tree)
    encoded_text = ''.join(codebook[char] for char in data)
    return encoded_text, codebook


def huffman_decoding(encoded_data, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}
    current_code = ""
    decoded_text = ""

    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codebook:
            decoded_text += reverse_codebook[current_code]
            current_code = ""

    return decoded_text


# Przykład użycia
if __name__ == "__main__":
    text = "W laboratorium chemik uzywal polimerow do stworzenia nowej polisyntezatorowej substancji."
    encoded_text, codebook = huffman_encoding(text)
    decoded_text = huffman_decoding(encoded_text, codebook)

    print("Original text:", text)
    print("Encoded text:", encoded_text)
    print("Decoded text:", decoded_text)
