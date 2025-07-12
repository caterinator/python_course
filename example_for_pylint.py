"""Modul-Dokumentationsstring (Modul-Docstring): 
    Kommentar in Python, der direkt am Anfang einer .py-Datei steht und in dreifachen Anführungszeichen geschrieben wird. 
    Er dient dazu, das Modul (also die Datei) zu beschreiben: Was es tut, wofür es gedacht ist und ggf. wie man es benutzt.
"""
def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

def say_hello(name):
    """Say hello to someone"""
    print("Hello, " + name)

def main():
    """Print the result"""
    sum_result = add_numbers(5, 7)
    print(f"The sum is {sum_result}")

    say_hello("World")

if __name__ == "__main__":
    main()
