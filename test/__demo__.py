import pyfiglet

def display_project_title():
    ascii_art = pyfiglet.figlet_format("\tARP\nSNIFFER", font="slant")
    print(ascii_art, end="v1.1")

if __name__ == "__main__":
    display_project_title()