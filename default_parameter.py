# Belajar Default Argument Value

def say_hello(first_name="Atikah", last_name=""):
    print(f"Hello {first_name} {last_name}")

say_hello("Farah")
say_hello(last_name="Farah")
say_hello(last_name="Miqdad", first_name="Farah") # bisa di acak juga