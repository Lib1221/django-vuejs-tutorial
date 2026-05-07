import json
from pathlib import Path

import pytest
from django.urls import reverse


@pytest.fixture
def index_response(client):
    return client.get(reverse("index"))


def test_index_returns_200(index_response):
    assert index_response.status_code == 200


def test_index_uses_index_template(index_response):
    template_names = [t.name for t in index_response.templates if t.name]
    assert "index.html" in template_names


def test_index_renders_vue_mount_point(index_response):
    body = index_response.content.decode()
    assert '<div id="app">' in body
    assert "<demo></demo>" in body


def test_index_loads_main_webpack_bundle(index_response):
    body = index_response.content.decode()
    assert "/static/bundles/app.js" in body


def test_webpack_stats_file_is_valid():
    stats_path = Path(__file__).resolve().parent.parent / "webpack-stats.json"
    assert stats_path.is_file(), f"webpack-stats.json missing at {stats_path}"

    data = json.loads(stats_path.read_text())
    assert data["status"] == "done"
    assert "main" in data["chunks"]
    assert any(asset.endswith("app.js") for asset in data["chunks"]["main"])
