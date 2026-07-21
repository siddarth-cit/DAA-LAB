"""
Experiment 2
Comparative Analysis of Naive, Rabin-Karp, and KMP String Matching Algorithms
"""

import random
import time


def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    matches = []
    comparisons = 0

    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            matches.append(i)

    return matches, comparisons


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    return lps


def kmp_search(text, pattern):
    n, m = len(text), len(pattern)

    lps = compute_lps(pattern)

    i = j = 0
    comparisons = 0
    matches = []

    while i < n:
        comparisons += 1

        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                matches.append(i - j)
                j = lps[j - 1]

        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches, comparisons


def rabin_karp(text, pattern, prime=101):
    n, m = len(text), len(pattern)

    d = 256
    h = pow(d, m - 1, prime)

    pattern_hash = 0
    text_hash = 0

    matches = []
    comparisons = 0

    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % prime
        text_hash = (d * text_hash + ord(text[i])) % prime

    for i in range(n - m + 1):

        if pattern_hash == text_hash:
            matched = True

            for j in range(m):
                comparisons += 1

                if text[i + j] != pattern[j]:
                    matched = False
                    break

            if matched:
                matches.append(i)

        if i < n - m:
            text_hash = (
                d * (text_hash - ord(text[i]) * h)
                + ord(text[i + m])
            ) % prime

            if text_hash < 0:
                text_hash += prime

    return matches, comparisons


def performance():
    text = "".join(random.choices("ABCD", k=10000))
    patterns = ["AB", "ABCD", "ABCDAB", "ABCDABCD"]

    print("\nPerformance Comparison")
    print("-" * 55)
    print(f'{"Pattern":<12}{"Naive":>10}{"KMP":>10}{"RK":>10}')

    for p in patterns:
        _, n = naive_search(text, p)
        _, k = kmp_search(text, p)
        _, r = rabin_karp(text, p)

        print(f"{p:<12}{n:>10}{k:>10}{r:>10}")


def main():
    text = "AABAACAADAABAABA"
    pattern = "AABA"

    print("TEXT :", text)
    print("PATTERN :", pattern)
    print()

    n_match, n_comp = naive_search(text, pattern)
    k_match, k_comp = kmp_search(text, pattern)
    r_match, r_comp = rabin_karp(text, pattern)

    print(f"Naive      -> {n_match} Comparisons = {n_comp}")
    print(f"KMP        -> {k_match} Comparisons = {k_comp}")
    print(f"RabinKarp  -> {r_match} Comparisons = {r_comp}")

    performance()


if __name__ == "__main__":
    main()