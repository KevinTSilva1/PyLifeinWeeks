userAge = int(input("What is your current age? "))

years_reaming = 90 - userAge
days_reaming = years_reaming * 365
months_reaming = years_reaming * 12
weeks_reaming = years_reaming * 52

print(f"You have {days_reaming} days, {weeks_reaming} weeks, {months_reaming} months left.")
