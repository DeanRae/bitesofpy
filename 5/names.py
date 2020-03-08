NAMES = [
    "arnold schwarzenegger",
    "alec baldwin",
    "bob belderbos",
    "julian sequeira",
    "sandra bullock",
    "keanu reeves",
    "julbob pybites",
    "bob belderbos",
    "julian sequeira",
    "al pacino",
    "brad pitt",
    "matt damon",
    "brad pitt",
]


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    return list(set(name.title() for name in names))


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)

    # splicing at 1 assuming that first name is 1 word but may have two word surnames
    return sorted(names, key=lambda s: s.split()[1:], reverse=True)


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)

    return sorted([n.split()[0] for n in names], key=lambda s: len(s.split()[0]))[0]
