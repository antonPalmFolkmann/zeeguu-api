# coding=utf-8
#
from unittest import TestCase

from zeeguu_api.tests.api_test_mixin import APITestMixin


class Test(APITestMixin, TestCase):

    def test_get_possible_translations(self):
        translations = self.api_post('/get_possible_translations/de/en',
                                               dict(context="das ist sehr schon", url="lalal.is", word="schon", title="lala"))

        assert "nice" in translations.data


    def test_get_possible_translations2(self):
        translations = self.api_post('/get_possible_translations/de/en',
                                               dict(context=u"Da sich nicht eindeutig erkennen lässt, "
                                                            u"ob Emojis Männer oder eben doch womöglich "
                                                            u"glatzköpfig Frauen darstellen,",
                                                    url="lalal.is", word=u"glatzköpfig", title="lala"))

        assert "bald" in translations.data
