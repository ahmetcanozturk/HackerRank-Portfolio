# solution to the HackerRank problem "Designer PDF Viewer"
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
# When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently.
# Ahmetcan Ozturk
import math

def designerPdfViewer(h, word):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    maxi = -math.inf
    for item in word:
        idx = alphabet.index(item)
        if (h[idx] > maxi):
            maxi = h[idx]
    return maxi * len(word)

if __name__ == '__main__':
    #h = list(map(int, input().rstrip().split()))
    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

    print("word: ")
    word = input()

    result = designerPdfViewer(h, word)

    print("output :\n" + str(result) + '\n')