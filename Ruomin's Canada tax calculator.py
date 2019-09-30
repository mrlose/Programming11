province=""
country=input("Please enter your country: ")
purchase=input("Please enter your purchase: ")
if country=="canada":
  province=input("Please enter your province: ")
else:
  print("Have a nice day")
if province=="ab" or province=="nt" or province=="nu" or province=="yt":
  total=int(purchase)*1.05
  print("This is your total with tax:")
  print(total)
if province=="bc":
  total=int(purchase)*1.12
  print("This is your total with tax:")
  print(round(total,2))
if province=="mb" or province=="on":
  total=int(purchase)*1.13
  print("This is your total with tax:")
  print(round(total,2))
if province=="nb" or province=="nl" or province=="ns" or province=="pe" or province=="qc":
  total=int(purchase)*1.15
  print("This is your total with tax:")
  print(round(total,2))
if province=="sk":
  total=int(purchase)*1.11
  print("This is your total with tax:")
  print(round(total,2))
