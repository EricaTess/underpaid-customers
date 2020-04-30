melon_cost = 1.00

customer1_name = "Joe"
customer1_melons = 5
customer1_paid = 5.00

customer2_name = "Frank"
customer2_melons = 6
customer2_paid = 6.00

customer3_name = "Sally"
customer3_melons = 3
customer3_paid = 3.00

customer4_name = "Sean"
customer4_melons = 9
customer4_paid = 9.50

customer5_name = "David"
customer5_melons = 4
customer5_paid = 4.00

customer6_name = "Ashley"
customer6_melons = 3
customer6_paid = 2.00

def who_underpaid(name, melons, paid):
  expected = melons * melon_cost
  if expected != paid:
    print(f"{name} paid ${paid:.2f},",
          f"expected ${expected:.2f}"
          )

who_underpaid(customer6_name, customer6_melons, customer6_paid)

