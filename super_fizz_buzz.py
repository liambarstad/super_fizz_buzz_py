class SuperFizzBuzz:

  def sequence(self, num):
    output = ""
    if num % 7 == 0:
      output = output + "Super"
    if num % 3 == 0:
      output = output + "Fizz"
    if num % 5 == 0:
      output = output + "Buzz"
    if num % 7 != 0 and num % 3 != 0 and num % 5 != 0:
      output = num
    return output
