import logging
import socket

from .models import Domain


logger = logging.getLogger(__name__)


def resolve_domain(domain: Domain):
    """
    Попробовать получить IP по переданному домену.
    """
    try:
        ip = socket.gethostbyname(domain.full_domain_name)
        logger.info(f'{domain.full_domain_name}: has been resolved with ip={ip}')
        domain.set_request_check(True)
    except socket.gaierror:
        logger.info(f'{domain.full_domain_name}: has not been resolved')
        domain.set_request_check(False)
