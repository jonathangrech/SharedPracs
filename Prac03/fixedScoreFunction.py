def main():
    score = float(input("Enter score: "))
    result = find_result(score)

    print(result)


def find_result(score):
    if 0 <= score < 50:
        result = "Bad"
    elif score < 90:
        result = "Passable"
    elif score <= 100:
        result = "Excellent"
    else:
        result = "Invalid Score"

    return result

main()