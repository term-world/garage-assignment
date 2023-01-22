import inventory
from inventory.Item import FixtureSpec

class KeypadCracker(FixtureSpec):

  def __init__(self):
    super().__init__()

  def use(self):
    print(f"KEYPAD CODE: {self.first_half()}{self.second_half()}")
  
  def first_half(self) -> str:
    # Prompt user to enter a number (1-12) from the keyboard
    birth_month = input("Input month you were born [1-12]: ")
    # Convert birth_month to integer; store as birth_month_number
    birth_month_number = int(birth_month)
    # Create separate variable to keep track of alterations to 
    # birth_month_number -- we need the original for the final
    # calculation!
    running_number = birth_month_number
    # Multiply our running_number by 3
    running_number = running_number * 3
    # Add 6 to our running_number
    running_number = running_number + 6
    # Divide running_number by 3
    running_number = running_number // 3
    # Substract birth_month_number FROM running_number, store
    # as a separate variable to input into the keypad
    first_digit = running_number - birth_month_number
    # To derive the second digit, subtract 1 from the first digit
    second_digit = first_digit - 1
    # Display program output to the user
    return f"{first_digit}{second_digit}"

  def second_half(self) -> str:
    # Prompt user to enter a number (1-31) from the keyboard
    birth_day = input("Input day you were born [1-31]: ")
    # Convert birthday to integer; store as birth_day_number
    birth_day_number = int(birth_day)
    # Create separate variable to keep track of alterations to 
    # birth_day_number -- we need the original for the final
    # calculation!
    running_number = birth_day_number
    # Add 1 to running_number
    running_number = running_number + 1
    # Mulitiply running_number by 2 (doubling it)
    running_number = running_number * 2
    # Add 4 to running_number
    running_number = running_number + 4
    # Divide running_number by 2
    running_number = running_number // 2
    # Subtract birth_day_number from running_number
    running_number -= birth_day_number
    # Set aside the current value of running_number as the
    # third_digit of the code
    third_digit = running_number
    # Multiply running_number by 2 (double it)
    running_number = running_number * 2
    # Add 3 to running_number
    running_number = running_number + 3
    # Find the remainder of the running_number divided by 5
    # (Hint: this uses the modulus operator)
    fourth_digit = running_number % 5
    return f"{third_digit}{fourth_digit}"

def main():
  obj = KeypadCracker()
  obj.use()

if __name__ == "__main__":
  main()
