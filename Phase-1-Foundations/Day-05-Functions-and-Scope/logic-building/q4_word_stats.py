"""
Problem 4 - Word & character statistics (STUB).

Return THREE things from one call: word count, vowel count, longest word.

Run:
    python q4_word_stats.py
"""

def word_stats(sentence):
    """Return (word_count, vowel_count, longest_word) for the sentence."""
    words = sentence.split()        # gives a list of words
    vowel_count = 0
    longest = ""

    # TODO: count vowels - loop each character of sentence.lower(),
    #       add 1 when the character is in "aeiou"
    # TODO: find the longest word - loop `words`, keep the longest seen so far

    word_count = len(words)
    return word_count, vowel_count, longest


if __name__ == "__main__":
    wc, vc, longest = word_stats("Softpro School of AI")
    print(f"words={wc} vowels={vc} longest={longest!r}")
