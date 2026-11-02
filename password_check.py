def validate_password(password, min_length):

    problems = []

    if password == "":
        problems.append("Haslo nie moze byc puste")

    if len(password) < min_length:
        problems.append(
            f"Haslo musi miec co najmniej {min_length} znakow"
        )

    if password.startswith(" ") or password.endswith(" "):
        problems.append(
            "Haslo nie moze zaczynac sie ani konczyc spacja"
        )

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    special_chars = {
        "!", "@", "#", "$",
        "%", "^", "&", "*"
    }

    score = 0
    strength = ""
    lower_char_count = 0
    upper_char_count = 0
    digit_count = 0
    special_char_count = 0

    for char in password:

        if char.islower():
            has_lower = True
            lower_char_count +=1

        if char.isupper():
            has_upper = True
            upper_char_count +=1

        if char.isdigit():
            has_digit = True
            digit_count +=1

        if char in special_chars:
            has_special = True
            special_char_count +=1

    if len(password) >= min_length:
        score += 1

    if has_lower:
        score += 1

    if has_upper:
        score += 1

    if has_digit:
        score += 1

    if has_special:
        score += 1

    if not has_lower:
        problems.append("Brak malej litery")

    if not has_upper:
        problems.append("Brak wielkiej litery")

    if not has_digit:
        problems.append("Brak cyfry")

    if not has_special:
        problems.append("Brak znaku specjalnego")

    if score == 1:
        strength = "Bardzo slabe"

    elif score == 2:
        strength = "Slabe"

    elif score == 3:
        strength = "Srednie"

    elif score == 4:
        strength = "Mocne"

    elif score == 5:
        strength = "Bardzo mocne"

    is_valid = len(problems) == 0

    stats = {
        "Liczba znakow": len(password),
        "Male litery": lower_char_count,
        "Wielkie litery": upper_char_count,
        "Cyfry": digit_count,
        "Znaki specjalne": special_char_count
}

    return is_valid, problems ,strength, stats



min_length_input = input(
    "Podaj minimalna dlugosc hasla (Enter = 12): "
)

if min_length_input == "":
    min_length = 12
else:
    try:
        min_length = int(min_length_input)
    except ValueError:
        print("Blad konfiguracji: podana wartosc nie jest liczba.")
        exit()

password = input("Prosze podaj haslo: ")

valid, problems, strengthOfPassword, statistics = validate_password(
    password,
    min_length
)

if valid:
    print(
        f"Haslo spelnia wszystkie wymagania. "
        f"Sila hasla to: {strengthOfPassword}"
    )

    print("\n=== STATYSTYKI HASLA ===")
    for key, value in statistics.items():
        print(f"{key:<20}: {value}")

else:
    print(f"Liczba bledow: {len(problems)}")

    print("\n=== STATYSTYKI HASLA ===")
    for key, value in statistics.items():
        print(f"{key:<20}: {value}")

    print(f"\nSila hasla to: {strengthOfPassword}")

    print("Wykryto bledy:")
    for problem in problems:
        print("-", problem)

test_cases = {
    "Puste haslo": "",
    "Za krotkie haslo": "admin",
    "Brak wielkiej litery": "password123!",
    "Brak cyfry": "PasswordTest!",
    "Brak znaku specjalnego": "Password1234",
    "Spacje na brzegach": " Password123!",
    "Poprawne haslo": "VeryStrongPassword2026!"
}

for test_name, password in test_cases.items():

    valid, problems, strengthOfPassword, statistics = validate_password(password, 12)

    print("\nPrzypadek:", test_name)

    if valid:
        print("WYNIK: POPRAWNE")
    else:
        print("WYNIK: NIEPOPRAWNE")

        for problem in problems:
            print("-", problem)
