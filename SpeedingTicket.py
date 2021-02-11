def CalculateFine():
    fine = 10 * over_speed
    print("Fine: ${}\n".format(fine))

def PrintSummary():
    if over_speed <= 0:
        print("Not speeding\n")
    elif over_speed > 80:
        print("Go to jail\n")
        wanted.append(name)
    elif over_speed >= 50:
        print("Loose license\n")

wanted = ["Jess", "Josh", "Josiah", "Ryan"]
repeat = "yes"

while repeat == "yes" or "y" or "yep":
  name = input("Name:")
  if name in wanted:
      print("{} has a warrant for their arrest. Send them to jail! \n".format(name))
  else:
      try:
          speed = int(input("What is the speed of the car? "))
          limit = int(input("What is the speed limit? "))
          over_speed = speed - limit
      except ValueError:
          print("Please enter a valid number")

      if over_speed >= 1 and over_speed < 50:
          CalculateFine()
      else:
          PrintSummary()
  repeat = input("Do you want to enter another speeder?")
