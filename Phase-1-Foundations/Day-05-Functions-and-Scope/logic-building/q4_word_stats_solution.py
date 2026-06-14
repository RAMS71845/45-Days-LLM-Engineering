"""
Problem 4 - Word & character statistics (SOLUTION).

Run:
    python q4_word_stats_solution.py

Logic-building note:
  Three sub-problems hiding in one task. Solve each with a pattern you know:
    - word count  -> len(.split())
    - vowel count -> COUNTER pattern (loop chars, +1 on a hit)
    - longest word-> "BEST SO FAR" pattern (keep a champion, update on a longer one)
  Then return all three at once - Python packs them into a tuple, and the caller
  unpacks with `wc, vc, longest = word_stats(...)`.
"""

def word_stats(sentence):
    """Return (word_count, vowel_count, longest_word)."""
    words = sentence.split()                # split on whitespace -> list of words

    vowel_count = 0                         # counter pattern
    for ch in sentence.lower():             # lower() so A and a both count
        if ch in "aeiou":
            vowel_count += 1

    longest = ""                            # best-so-far pattern
    for w in words:
        if len(w) > len(longest):           # found a longer one? it's the new champion
            longest = w

    return len(words), vowel_count, longest  # multiple return values (a tuple)


if __name__ == "__main__":
    samples = [
        "Softpro School of AI",
        "Logic building is the real skill",
        "Python",
    ]
    for s in samples:
        wc, vc, longest = word_stats(s)     # unpack the returned tuple
        print(f"{s!r}")
        print(f"   words={wc}  vowels={vc}  longest={longest!r}\n")
