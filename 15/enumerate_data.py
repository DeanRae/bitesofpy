names = "Julian Bob PyBites Dante Martin Rodolfo".split()
countries = "Australia Spain Global Argentina USA Mexico".split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    # assuming that the length of both lists is always equal, we can use
    # enumerate to get the index while looping through one list, then use
    # the index to access the matching value in the other index

    for i, name in enumerate(names):
        print(f"{i+1}. {name:<11}{countries[i]}")

