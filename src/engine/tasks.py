import logging

from celery import shared_task

from engine.services.checker.resolver import resolve_domain
from .models import Domain


logger = logging.getLogger(__name__)


@shared_task()
def resolve_domains() -> None:
    """
    Получаем список доменов, которые готовы к проверке.

    Проверяем резолвиться ли домен (можно получить IP по имени домена).
    Если IP получается получить - значит, что домен уже занят =(
    """
    logger.info(f'Start {resolve_domains.__name__} task')
    domains = Domain.objects.filter(request_check_result__isnull=True)[:10]

    for domain in domains:
        resolve_domain(domain)
