import re

def parse_menu(file_path):
    """
    Parses a menu text file into a structured format.

    Args:
        file_path (str): Path to the text file containing the menu.

    Returns:
        list: A list of dictionaries, each containing 'name', 'description', and 'price'.
    """
    with open("C:/Users/vedant/pricing_algorithm/pricing/static/village_menu.txt", 'r') as file:
        content = file.readlines()

    # Regex to extract items, descriptions, and prices
    pattern = r"Item: (.+?)\nDescription: (.+?)\n(?:Price: \$ ([\d.]+))?"
    matches = re.findall(pattern, content)

    # Parse into a structured list of dictionaries
    menu = []
    for match in matches:
        name, description, price = match
        menu.append({
            'name': name.strip(),
            'description': description.strip(),
            'price': float(price) if price else None
        })

    return menu
