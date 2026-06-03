from art import logo


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide,
}

def calculator():
  print(logo)

  num1 = float(input("What is the first number ?: "))
  while True:
    for symbol in operations:
      print(symbol)

    operation_symbol = input("Type a math operation: ")
    if operation_symbol not in operations:
      print("Invalid operation. Please choose one of the available symbols.")
      continue

    num2 = float(input("What is the next number?: "))
    if operation_symbol == '/' and num2 == 0:
      print("Error: Cannot divide by zero. Please enter a different number.")
      continue

    calculation = operations[operation_symbol]
    answer = calculation(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    continue_calc = input(
      f"Type 'y' to continue calculating with {answer}, 'n' to exit, or 'new' for a brand new calculation: "
    ).lower()

    if continue_calc == 'y':
      num1 = answer
    elif continue_calc == 'new':
      calculator()
      return
    else:
      print("\nGoodbye.")
      break

calculator()
