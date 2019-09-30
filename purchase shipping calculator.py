purchase=float(input("Please enter your purchase:"))
if purchase>=50:
  total=float(purchase)
  print("This is your total: {0:.2f}, have a nice day".format(total))
if purchase<50:
  total=float(purchase)+10
  print("This is your total with shipping: {0:.2f}".format(total))
