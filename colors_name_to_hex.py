from webcolors import name_to_hex
from print_color import print

def color_name_to_code(color_name):
    try:
        hex_code = name_to_hex(color_name.strip().lower())
        return hex_code
    except ValueError as e:
        print(f"Error: Invalid color name '{color_name}'")
        return None

colorName = input("Enter Color name :")
result = color_name_to_code(color_name=colorName)

if result:
    print(f"Hex-code of color {colorName}  is  {result}",color=f'{colorName}')

else:
    print("Invalid color Name !")    