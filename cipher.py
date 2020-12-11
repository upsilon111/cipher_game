from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']






def caesar(cipher_direction, start_text, shift_amount):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char


  print(f"The {cipher_direction}d is {end_text}")



print(logo)



should_continue = True

while should_continue:


  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26

  caesur(cipher_direction = direction, start_text = text, shift_amount = shift)

  result = input("Do you want to go again: Y or N? \n")
  if result == "N".lower():
    should_continue = False
    print("Bye!")


