import math
def start_game():
    print("Welcome to the GCD finder game🧿🧿🧿🧿")
    print("Tell me a number and I will Find its GCD")
    while True:
        num=input("🔢🔢🔢🔢Enter a number to check it's GCD or type'Exit' to not play❌❌❌❌: ")
        if num.lower()=="exit":
            print("Thanks for playing 🖐🏻🖐🏻🖐🏻🖐🏻🖐🏻🖐🏻🖐🏻")
            break
        num2=input("🔢🔢🔢🔢Enter a second number or type'Exit' to not play❌❌❌❌: ")
        if num2.lower()=="exit":
            print("Thanks for playing 🖐🏻🖐🏻🖐🏻🖐🏻🖐🏻🖐🏻🖐🏻")
            break
        if not num.isdigit() or not num2.isdigit():
            print("Enter numbers only.No symbols allowed🚫🚫🚫🚫")
            continue
        a=int(num)
        b=int(num2)
        gcd=math.gcd(a,b)
        print(f"The GCD of {num} and {num2} is {gcd}\n")
start_game()