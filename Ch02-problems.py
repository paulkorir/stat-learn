import math
import sys


def compute_euclidean_distance(data: list[list[int, int, int, str]], from_point=(0, 0, 0)) -> list[tuple[float, str]]:
    result = list()
    for obs in data:
        x1, x2, x3, cat = obs
        dist = math.sqrt(
            (x1 - from_point[0]) ** 2 + (x2 - from_point[1]) ** 2 + (x3 - from_point[2]) ** 2
        )
        result.append((dist, cat))
    return result


def make_prediction(distances: list[tuple[float, str]], k=1) -> str:
    # sort the distances
    distances.sort(key=lambda x: x[0])
    # get the top k
    top_k = distances[:k]
    # get the categories
    categories = [cat for _, cat in top_k]
    # get the most frequent category
    prediction = max(set(categories), key=categories.count)
    return prediction


def main():
    data = [
        [0, 3, 0, 'Red'],
        [2, 0, 0, 'Red'],
        [0, 1, 3, 'Red'],
        [0, 1, 2, 'Green'],
        [-1, 0, 1, 'Green'],
        [1, 1, 1, 'Red'],
    ]
    # compute the euclidean distance between each obs and (0, 0, 0)
    result = compute_euclidean_distance(data)
    print(f"{result = }")
    # prediction with K = 1
    prediction = make_prediction(result, k=1)
    print(f"{prediction = }")
    # prediction with K = 3
    prediction = make_prediction(result, k=3)
    print(f"{prediction = }")
    return 0


if __name__ == '__main__':
    sys.exit(main())
