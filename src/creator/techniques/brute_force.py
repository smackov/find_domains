from itertools import product

from checker.models import Domain


def generator(sings: set, length: int, zone: str):
    for combination in product(sings, repeat=length):
        name = ''.join(combination)
        full_domain_name = name + zone
        Domain.objects.get_or_create(
            name=name,
            full_domain_name=full_domain_name
        )