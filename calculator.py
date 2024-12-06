import datetime
import inflect
import sys

def main():
    dob = input("Your date of birth (YYYY-MM-DD): ")

    age_in_mins = age_in_minutes(dob)

    if age_in_mins is None:
        print("Invalid Date")
        sys.exit(1)

    print(num_to_word(age_in_mins))



def age_in_minutes(dob):

    try:
        dob_datetime = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
    except ValueError:
        return None

    today = datetime.date.today()

    age = today - dob_datetime
    return age.days*24*60

def num_to_word(s):
    p = inflect.engine()
    return p.number_to_words(s, andword="").capitalize() + " minutes"



if __name__ == "__main__":
    main()