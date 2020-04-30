

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




def who_underpaid(customer_payments):
  '''calculate cost of melons and see who underpaid'''


  payments = open(customer_payments)

  for line in payments:
    order = line.split('|')

    full_name = order[1]

    first_name = full_name.split(' ')[0]


    melons = float(order[2])

    paid = float(order[3])


    expected = melons * melon_cost
    if expected != paid:
      print(f"{first_name} paid ${paid:.2f},",
            f"expected ${expected:.2f}"
          )

      if expected < paid:
        print(f"{first_name} has overpaid for their melons.")

      elif expected > paid:
        print(f"{first_name} has underpaid for their melons.")
  payments.close()

who_underpaid("customer-orders.txt")

