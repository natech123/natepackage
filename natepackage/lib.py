

def try_me(age, sleep_av):
    """Returns how much sleep a perosn has got in their life"""
    age_in_days = age * 365
    return f"You have slept for {age_in_days * sleep_av} hours in your life, equal to {(age_in_days * sleep_av) / 24} days, or {((age_in_days * sleep_av) / 24) / 365} years"

if __name__ == "__main__":
    nate_sleep = try_me(23,6)
    print(nate_sleep)
