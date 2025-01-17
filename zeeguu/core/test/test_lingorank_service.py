from unittest import TestCase

from zeeguu.core.test.model_test_mixin import ModelTestMixIn

import zeeguu.core
from zeeguu.core.test.rules.rss_feed_rule import RSSFeedRule
from zeeguu.core.test.test_data.mocking_the_web import (
    url_formation_professionelle,
    url_spiegel_militar,
)
from zeeguu.core.elastic.indexing import document_from_article
from zeeguu.core.content_retriever.article_downloader import download_feed_item

from datetime import datetime

from unittest.mock import patch


session = zeeguu.core.db.session


class ArticleDownloaderTest(ModelTestMixIn, TestCase):
    def setUp(self):
        super().setUp()
        self.dummy_feed_item = {
            "title": "Some Title",
            "published_datetime": datetime.now(),
            "summary": "Some Summary",
        }

    @patch(
        "zeeguu.core.language.services.lingo_rank_service.retrieve_lingo_rank",
        return_value=2.1,
    )
    def test_download_french_article(self, lr_mock):

        feed = RSSFeedRule().feed_fr

        art1 = download_feed_item(
            session, feed, self.dummy_feed_item, url_formation_professionelle
        )

        es_document = document_from_article(art1, session)
        assert es_document["lr_difficulty"] == 2.1

    def test_download_german_article(self):

        feed = RSSFeedRule().feed1

        art1 = download_feed_item(
            session, feed, self.dummy_feed_item, url_spiegel_militar
        )

        es_document = document_from_article(art1, session)
        assert es_document["lr_difficulty"] == None
