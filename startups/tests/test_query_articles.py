import json
import pytest
from graphene_django.utils.testing import graphql_query

from startups.models import Articles, Categories

@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        return graphql_query(*args, **kwargs, client=client)

    return func

@pytest.fixture(autouse=True)
def create_article():
    Categories.objects.create(name="Crypto")
    article = Articles.objects.create(
        title="Bitcoin is the future",
        link="https://www.coindesk.com/bitcoin-is-the-future",
        processed=False,
    )
    article.article_categories.add(Categories.objects.get(name="Crypto"))

@pytest.mark.django_db
def test_query_articles(client_query):
    response = client_query(
        '''
        query {
          articles {
            edges {
              node {
                id
                title
                link
                processed
                articleCategories {
                  id
                  name
                }
              }
            }
          }
        }
        '''
    )

    content = json.loads(response.content)
    assert 'errors' not in content
    assert content['data']['articles']['edges'][0]['node']['title'] == 'Bitcoin is the future'
    assert content['data']['articles']['edges'][0]['node']['link'] == 'https://www.coindesk.com/bitcoin-is-the-future'
    assert content['data']['articles']['edges'][0]['node']['processed'] == False
    assert content['data']['articles']['edges'][0]['node']['articleCategories'][0]['name'] == 'Crypto'
    assert content['data']['articles']['edges'][0]['node']['articleCategories'][0]['id'] == '1'

@pytest.mark.django_db
def test_query_articles_filtered_by_category(client_query):
    response = client_query(
        '''
        query {
          articles(articleCategories_Name_In: ["Crypto"]) {
            edges {
              node {
                id
                title
                link
                processed
                articleCategories {
                  id
                  name
                }
              }
            }
          }
        }
        '''
    )

    content = json.loads(response.content)
    assert 'errors' not in content
    assert content['data']['articles']['edges'][0]['node']['title'] == 'Bitcoin is the future'
    assert content['data']['articles']['edges'][0]['node']['link'] == 'https://www.coindesk.com/bitcoin-is-the-future'
    assert content['data']['articles']['edges'][0]['node']['processed'] == False
    assert content['data']['articles']['edges'][0]['node']['articleCategories'][0]['name'] == 'Crypto'
    assert content['data']['articles']['edges'][0]['node']['articleCategories'][0]['id'] == '1'
