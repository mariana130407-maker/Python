"""
Documentation
"""
import numpy as np

def information():
    """Displays the purpose and author of the program."""
    print("The author of this program is Yatsenko Mariana from K-13.")
    print("This program prints a sequence of elements under the main diagonal of a square matrix in a spiral order.")
    print("Variant 99: Spiral traversal from the bottom-left corner counterclockwise under the main diagonal.")

def check_n(n):
    """Checks if n is a positive integer."""
    if n <= 0:
        raise ValueError("Enter a positive integer (n > 0)")
    return int(n)

def create(n):
    """Creates an n x n matrix filled with pseudo-random real numbers from the interval [0.25; 0.75)."""
    matrix = np.random.uniform(0.25, 0.75, size=(n, n))
    return matrix

def traversal(matrix):
    """Performs a spiral traversal (counterclockwise) of the elements under the main diagonal starting from the bottom-left corner."""
    n = len(matrix)
    triangle = [[matrix[i][j] for j in range(i)] for i in range(1, n)]
    result = []
    top = 0
    bottom = len(triangle) - 1
    left = 0
    right = max(len(row) for row in triangle) - 1

    while top <= bottom and left <= right:
        for i in range(bottom, top - 1, -1):
            if left < len(triangle[i]):
                result.append(triangle[i][left])
        left += 1
        for j in range(left, right + 1):
            if top < len(triangle) and j < len(triangle[top]):
                result.append(triangle[top][j])
        top += 1
        for i in range(top, bottom + 1):
            if right < len(triangle[i]):
                result.append(triangle[i][right])
        right -= 1
        for j in range(right, left - 1, -1):
            if bottom < len(triangle) and j < len(triangle[bottom]):
                result.append(triangle[bottom][j])
        bottom -= 1

    print("Spiral traversal of elements under the main diagonal:")
    for value in result:
        print(f"{value:.1f}", end=" ")
    print()

def main():
    """Main function to handle input, matrix creation, and traversal."""
    try:
        n = int(input("Enter the size of the square matrix (n): "))
        check_n(n)
        matrix = create(n)

        print("\nGenerated Matrix:")
        print(matrix)

        print("\nSpiral Traversal (under the main diagonal):")
        traversal(matrix)

    except (ValueError, TypeError, EOFError) as e:
        print("***** Error")
        print(e)
    except KeyboardInterrupt:
        print("\nProgram aborted by user.")

if __name__ == "__main__":
    information()
    main()
