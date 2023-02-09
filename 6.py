def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


def my_function(**foo):
  print("something " + foo["aa"])

my_function(bb="new", aa="important")