from circle import calculate_area as circle_area
from rectangle import calculate_area as rectangle_area

def get_positive_float(prompt):
    """Helper function to get a positive float from the user."""
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculate_circle():
    radius = get_positive_float("Enter the radius of the circle: ")
    area = circle_area(radius)

    print(f"\nThe area of the circle is: {area:.2f}\n")


def calculate_rectangle():
    length = get_positive_float("Enter the length: ")
    width = get_positive_float("Enter the width: ")

    area = rectangle_area(length, width)

    print(f"\nThe area of the rectangle is: {area:.2f}\n")


def main():

    while True:

        print("\n===== AREA CALCULATOR =====")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            calculate_circle()

        elif choice == "2":
            calculate_rectangle()

        elif choice == "3":
            print("\nThank you for using the program!")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")
            continue

        # Try again menu
        while True:
            again = input("Do you want to calculate again? (y/n): ").strip().lower()

            if again == "y":
                break

            elif again == "n":
                print("\nThank you for using the program!")
                return

            else:
                print("Invalid input. Please enter y or n.")


if __name__ == "__main__":
    main()