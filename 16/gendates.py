from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    current_date = PYBITES_BORN
    next_birthday = PYBITES_BORN.replace(year=PYBITES_BORN.year + 1)

    # for this bite, we stop at 2020 as per README
    while current_date.year < 2020:
        current_date += timedelta(days=100)

        if current_date.year > next_birthday.year:
            yield next_birthday
            next_birthday = next_birthday.replace(year=next_birthday.year + 1)
        yield current_date
