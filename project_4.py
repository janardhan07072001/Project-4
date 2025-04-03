import random

def coin_toss():
    """Simulate a single coin toss and return the result."""
    return random.choice(["Heads", "Tails"])

def multiple_tosses(num_flips):
    """Perform multiple coin tosses and count the results."""
    heads_count = 0
    tails_count = 0

    for _ in range(num_flips):
        result = coin_toss()
        print(f"Flip result: {result}")
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1

    return heads_count, tails_count

def main():
    """Main function to interact with the user."""
    while True:
        try:
            num_flips = int(input("Enter the number of coin flips: "))
            if num_flips <= 0:
                print("Please enter a positive number.")
                continue

            heads, tails = multiple_tosses(num_flips)

            print("\nResults Summary:")
            print(f"Heads: {heads} ({(heads / num_flips) * 100:.2f}%)")
            print(f"Tails: {tails} ({(tails / num_flips) * 100:.2f}%)")

            choice = input("Do you want to flip again? (yes/no): ").strip().lower()
            if choice != 'yes':
                print("Thanks for playing!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
