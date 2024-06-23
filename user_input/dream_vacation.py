poll_results = {}

poll_active = True
while poll_active:
    name = input("\nWhat's your name?")
    response = input("\nIf you could visit any place in the world where would it be?")

    poll_results[name] = response

    repeat = input("\nWould you like to let someone else answer? (yes/no) ")
    if repeat == 'no':
        break

print("\n---poll results---")
for name, place in poll_results.items():
    print(f"{name} would like to visit {place}")