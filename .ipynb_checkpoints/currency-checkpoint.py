# Basic Currency Converter

print("Currency Converter")
print("1. USD to INR")
print("2. INR to USD")
print("3. USD to EUR")
print("4. EUR to USD")

choice = int(input("Enter your choice (1-4): "))
amount = float(input("Enter the amount: "))

# Fixed exchange rates (example values)
USD_TO_INR = 83.0
INR_TO_USD = 1 / 83.0
USD_TO_EUR = 0.92
EUR_TO_USD = 1 / 0.92

if choice == 1:
    print("Converted amount:", amount * USD_TO_INR, "INR")
elif choice == 2:
    print("Converted amount:", amount * INR_TO_USD, "USD")
elif choice == 3:
    print("Converted amount:", amount * USD_TO_EUR, "EUR")
elif choice == 4:
    print("Converted amount:", amount * EUR_TO_USD, "USD")
else:
    print("Invalid choice")
