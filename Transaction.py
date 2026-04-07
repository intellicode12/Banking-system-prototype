def show_transactions(user):
    print("\nTransaction History:")
    if not user["transactions"]:
        print("No transactions yet.")
        return

    for t in user["transactions"]:
        print("-", t)
