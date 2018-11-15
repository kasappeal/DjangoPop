from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from ads.models import Ad


class TestMyAdsEndpoint(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.me = User.objects.create_user('me', password='mepassword')
        self.other = User.objects.create_user('other', password='otherpassword')

        self.me_ads = [
            Ad.objects.create(owner=self.me, name='me_ad_1', description='me ad 1', price=10, status=Ad.PUBLISHED),
            Ad.objects.create(owner=self.me, name='me_ad_2', description='me ad 2', price=10, status=Ad.PUBLISHED),
            Ad.objects.create(owner=self.me, name='me_ad_3', description='me ad 3', price=10, status=Ad.PUBLISHED)
        ]

        self.other_ads = [
            Ad.objects.create(owner=self.other, name='other_ad_1', description='other ad 1', price=10, status=Ad.PUBLISHED),
            Ad.objects.create(owner=self.other, name='other_ad_2', description='other ad 2', price=10, status=Ad.PUBLISHED)
        ]

    def test_user_cannot_retrieve_his_ads_if_is_not_authenticated(self):
        response = self.client.get('/api/1.0/ads/me/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_retrieves_only_its_ads(self):
        self.client.force_authenticate(self.me)
        response = self.client.get('/api/1.0/ads/me/')

        ads = response.data
        self.assertEqual(len(ads), len(self.me_ads))

        response_ads_ids = [ad.get('id') for ad in ads]
        me_ads_ids = [ad.pk for ad in self.me_ads]
        self.assertListEqual(response_ads_ids, me_ads_ids)
