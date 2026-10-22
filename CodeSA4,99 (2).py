"""
Documentation
"""
def information():
    """Notification of the purpose of the program and the author of the program"""
    print("The author of this program is Yatsenko Mariana from K-13")
    print("Variant 99")


def _min_sub(sequence, M):
    """Finds all the shortest subsequences with a sum of at least M, considering circular arrangement."""
    n = len(sequence)
    min_length = float('inf')
    results = []

    left = 0
    a = 0

    for right in range(2 * n):
        a += sequence[right % n]

        while a >= M and right - left + 1 <= n:
            length = right - left + 1
            if length < min_length:
                min_length = length
                results = [(left % n, length)]
            elif length == min_length:
                if (left % n, length) not in results:
                    results.append((left % n, length))

            a -= sequence[left % n]
            left += 1

    return results


def _check():
    """Checks and gets input from the user."""
    try:
        M = int(input("Enter M (>= 2): "))
        if M < 2:
            print("Error: M must be >= 2")
            return None

        print("Enter the elements of the sequence:")

        sequence = list(map(int, input().split()))


        if not sequence:
            print("Error: the sequence cannot be empty")
            return None

        return M, sequence

    except ValueError:
        print("*****error")
        return None

def main():
    """Main function of the program."""
    try:
        information()
        user_input = _check()
        if user_input is None:
            print("The program has been terminated due to an error")
            return

        M, sequence = user_input
        subsequences = _min_sub(sequence, M)

        print("THE WORK IS DONE")
        if not subsequences:
            print("No matching subsequences found")
        for start, length in subsequences:
            print(f"Start: {start}, Length: {length}")

    except KeyboardInterrupt:
        print("\nprogram aborted")


if __name__ == "__main__":
    main()
