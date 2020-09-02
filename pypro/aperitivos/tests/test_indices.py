import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.aperitivos.models import Video
from pypro.django_assertions import assert_contains


@pytest.fixture
def videos(db):
    return mommy.make(Video, 3)


@pytest.fixture
def resp(client, videos):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp, videos):
    for v in videos:
        assert_contains(resp, v.titulo)


def test_conteudo_video(resp, videos):
    for v in videos:
        assert_contains(resp, reverse('aperitivos:video', args=(v.slug,)))
