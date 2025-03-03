
# Raheek Ayman Mohamed Helal - Sec 4


def insertion_sort(scores):
    for i in range(1, len(scores)):
        key = scores[i]
        j = i - 1
        while j >= 0 and key < scores[j]:
            scores[j + 1] = scores[j]
            j -= 1
        scores[j + 1] = key

# Example usage
scores = [85, 92, 78, 90, 65, 88]
insertion_sort(scores)
print("Sorted scores:", scores)
