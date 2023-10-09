import random

from faker import Faker
from starlette.testclient import TestClient

fake = Faker()


def test_get_statistic(client: TestClient, redis_data_factory, redis_client):
    redis_data_factory(
        key="Statistic:suppliers",
        name=fake.word(),
        value=fake.random_int(max=2_000),
        history=[random.randint(1, 1000) for _ in range(10)]
    )
    redis_data_factory(
        key="Statistic:brands",
        name=fake.word(),
        value=fake.random_int(max=2_000),
        history=[random.randint(1, 1000) for _ in range(10)]
    )
    redis_data_factory(
        key="Statistic:cars",
        name=fake.word(),
        value=fake.random_int(max=2_000),
        history=[random.randint(1, 1000) for _ in range(10)]
    )

    response = client.get("api/v1/statistics")
    assert response.status_code == 200
    assert len(response.json()) > 0
    for r in response.json():
        assert r['data']['name'] is not None
        assert r['data']['value'] is not None
        assert len(r['data']['history']) > 0

