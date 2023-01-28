import hashlib
import sys

import requests
from requests import Response


def request_api_data(query_char: str) -> Response:
    """Returns the response"""
    url = f"https://api.pwnedpasswords.com/range/{query_char}"
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}")
    return res


def get_password_leaks_count(hashes, hash_to_check: str) -> int:
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password: str) -> int:
    """
    ie:
    original password: password123
    SHA-1 Hash: CBFDAC6008F9CAB4083784CBD1874F76618D2A97
    Anonymous search: CBFDA ( first five characters of the hash)
    Get all hashed passwords that starts with CBFDA
    """ 
    sha1password = hashlib.sha1(password.encode("utf8")).hexdigest().upper()
    first_chars, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first_chars)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"{password} was found {count} times. You should change it.")
        else:
            print(f"{password} was not found. Carry on!")
    return "done!"


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
