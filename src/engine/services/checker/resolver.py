import logging
import socket

from engine.models import Domain


logger = logging.getLogger(__name__)


def resolve_domain(domain: Domain) -> bool:
    """
    Checking if the domain can be resolved.
    """
    try:
        ip = socket.gethostbyname(domain.name)
        resolve_success = True
        logger.info(f'{domain}: has been resolved with ip={ip}')
        domain.update_resolve_check_information(True)
    except socket.gaierror:
        logger.info(f'{domain}: has not been resolved')
        domain.update_resolve_check_information(False)
        resolve_success = False
    return resolve_success
