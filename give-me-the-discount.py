try:
    fullPrice = int(input("Please enter the full price of the item: "))
    discPct = int(input("Please enter the discount in percentage values: "))

    print("The discounted price for your item is $" + str(fullPrice / 100 * (100 - discPct)) + ".")
except ValueError:
    print("Please proide a valid integer value. ")