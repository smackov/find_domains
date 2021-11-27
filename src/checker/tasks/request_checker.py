import logging
import socket

from ..models import Domain


logger = logging.getLogger(__name__)


def check(domain: Domain):
    """
    Try resolve domain name.
    """
    try:
        ip = socket.gethostbyname(domain.full_domain_name)
        logger.info(f'{domain.full_domain_name}: has been resolved with ip={ip}')
        domain.set_request_check(True)
    except socket.gaierror:
        logger.info(f'{domain.full_domain_name}: has not been resolved')
        domain.set_request_check(False)


def request_checker():
    logger.info(f'Start {request_checker.__name__} task')
    domains_should_be_checked = Domain.objects.filter(request_check_result__isnull=True)[:10]
    for domain in domains_should_be_checked:
        check(domain)
