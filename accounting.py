
def who_underpaid(customer_payments):
  '''calculate cost of melons and see who underpaid'''

  #defined txt file
  payments = open(customer_payments)

  #iterate through all lines in file
  for line in payments:

    #split lines into lists
    order = line.split('|')

    #defined first name
    full_name = order[1]

    first_name = full_name.split(' ')[0]


    melons = float(order[2])

    paid = float(order[3])

    #calculate the expected cost of melons
    expected = melons * melon_cost
    if expected != paid:
      print(f"{first_name} paid ${paid:.2f},",
            f"expected ${expected:.2f}"
          )

      #state whether a customer overpaid or underpaid
      if expected < paid:
        print(f"{first_name} has overpaid for their melons.")

      elif expected > paid:
        print(f"{first_name} has underpaid for their melons.")
  payments.close()

who_underpaid("customer-orders.txt")

