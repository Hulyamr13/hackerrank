import heapq
from typing import Iterable, Optional

def noPrefix(words):
    return _no_prefix_treed(words)

def char_range(c1, c2):
    for c in range(ord(c1), ord(c2) + 1):
        yield chr(c)

class Node:
    _ALLOWED_LETTERS = list(char_range("a", "j"))

    def __init__(self, depth: int, parent: "Optional[Node]"):
        assert depth == 0 or parent is not None

        self.depth = depth
        self.parent = parent
        self.word: Optional[str] = None
        self.indexes: list[int] = []
        self.children: dict[str, Optional[Node]] = {letter: None for letter in Node._ALLOWED_LETTERS}

    def set_word(self, word: str, index: int) -> None:
        assert self.word is None or self.word == word, f"Cannot reset the node word: {self.word} vs. {word}"
        self.word = word
        heapq.heappush(self.indexes, index)

    def get_min_index(self) -> int:
        return self.indexes[0]

    def get_min_index_opt(self) -> Optional[int]:
        try:
            return self.get_min_index()
        except IndexError:
            return None

    def get_indexed_non_empty_children(self) -> Iterable[tuple[str, "Node"]]:
        return ((letter, child) for letter, child in self.children.items() if child is not None)

    def get_non_empty_children(self) -> Iterable["Node"]:
        return map(lambda t: t[1], self.get_indexed_non_empty_children())

    def is_leaf(self) -> bool:
        return all(c is None for c in self.children.values())

    def is_prefixed_by_other_word(self) -> bool:
        return len(self.indexes) > 1 or self.get_closest_prefix_parent() is not None

    def is_prefix_of_other_word(self) -> bool:
        return not self.is_leaf()

    def is_prefixed_or_prefixes(self) -> bool:
        return self.is_prefix_of_other_word() or self.is_prefixed_by_other_word()

    def get_closest_prefix_parent(self) -> "Optional[Node]":
        curr = self.parent
        ret = None
        while curr is not None:
            if curr.word is not None:
                ret = curr
                break
            curr = curr.parent

        return ret

    def __lt__(self, other: "Node") -> bool:
        self_min_index = self.get_min_index_opt()
        other_min_index = other.get_min_index_opt()

        if self_min_index is None:
            return False
        else:
            return other_min_index is None or self_min_index < other_min_index

    def __repr__(self) -> str:
        return f"{self.indexes} {(self.depth)}: {self.word}"

class Trie:
    def __init__(self):
        self.root = Node(depth=0, parent=None)
        self.num_words = 0

    def insert(self, word: str, index: int) -> Optional[Node]:
        self.num_words += 1

        def _rec(curr: Node, depth: int, char_itr: Iterable[str]):
            try:
                char: str = next(char_itr)
            except StopIteration:
                curr.set_word(word, index)

                return curr if curr.is_prefixed_or_prefixes() else None

            child = curr.children[char]
            if child is None:
                child = Node(depth=depth, parent=curr)
                curr.children[char] = child

            return _rec(child, depth + 1, char_itr)

        return _rec(curr=self.root, depth=1, char_itr=iter(word))

    def insert_many(self, words: list[str], exit_early_on_bad_word: bool = True) -> Optional[Node]:
        first_checked_bad_word: Optional[Node] = None

        for index, word in enumerate(words, self.num_words):
            bad_word = self.insert(word, index)

            if bad_word and not first_checked_bad_word:
                first_checked_bad_word = bad_word
                if exit_early_on_bad_word:
                    break

        return first_checked_bad_word

def _no_prefix_treed(words):
    trie = Trie()
    first_checked_bad_word = trie.insert_many(words, exit_early_on_bad_word=True)

    if first_checked_bad_word:
        print("BAD SET", first_checked_bad_word.word, sep="\n")
    else:
        print("GOOD SET")


if __name__ == "__main__":
    n = int(input().strip())
    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
