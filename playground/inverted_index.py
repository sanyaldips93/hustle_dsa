from collections import defaultdict

def build_inverted_index(documents):
    inverted_index = defaultdict(set)
    
    for doc_id, text in documents.items():
        words = text.lower().split()  # Tokenization + Lowercase
        for word in words:
            inverted_index[word].add(doc_id)

    # Convert sets to sorted lists
    return {word: sorted(list(doc_ids)) for word, doc_ids in inverted_index.items()}


print(build_inverted_index({
    0: "the cat sat on the mat",
    1: "the dog sat on the log",
    2: "the cat chased the dog"
}))