import random
import string


def get_random_password() -> str:
    let_num = string.ascii_uppercase + string.ascii_lowercase + string.digits
    n = random.randrange(8, len(let_num), 1)
    password = "".join(random.sample(let_num, n))
    return password


print(get_random_password())
