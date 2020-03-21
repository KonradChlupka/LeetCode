class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letter_dict = {letter: i for i, letter in enumerate(order)}
        for i_word in range(len(words) - 1):
            pair_ordered = False
            for a, b in zip(words[i_word], words[i_word + 1]):
                if letter_dict[a] < letter_dict[b]:
                    pair_ordered = True
                    break
                elif letter_dict[a] > letter_dict[b]:
                    return False
            if pair_ordered:
                continue
            if len(words[i_word]) > len(words[i_word + 1]):
                return False
        return True
