# A for loop is effective for going through a list, but you shouldnt modify a list in a for loop. Python  wont be able to
# keep track of the items in the list. To modify a list as you work through it use a while loop. Using while loops with 
# lists and dictionaries allows you to collect, store, and organize lots of input to examine later.

# Say we have a list of new but unverified users, after we verify them we can move them to a list of verified users. We can
# use a while loop to take the users from the unconfirmed list as we verify them and add them to the confirmed list. 

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
print(*confirmed_users, sep="\n")