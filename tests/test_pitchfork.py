from pitchfork.pitchfork import search, Review, MultiReview
import unittest


class TestReview(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.review = search('mogwai', 'come on')

    def test_review(self):
        self.assertIsInstance(self.review, Review)

    def test_review_album(self):
        self.assertEqual(self.review.album(), "Come On Die Young")

    def test_reviev_artist(self):
        self.assertEqual(self.review.artist(), 'Mogwai')

    def test_review_label(self):
        self.assertEqual(self.review.label(), 'Chemikal Underground')

    def test_review_year(self):
        self.assertEqual(self.review.year(), '1999/2014')

    def test_review_url(self):
        self.assertEqual(self.review.url, '/reviews/albums/19466-mogwai-come-on-die-young-deluxe-edition/')


class TestMultiReview(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.multi_review = search('radiohead', 'ok computer')

    def test_multi_review(self):
        self.assertIsInstance(self.multi_review, MultiReview)

    def test_multi_review_album(self):
        self.assertEqual(self.multi_review.album(), "OK Computer: Collector's Edition")

    def test_multi_review_artist(self):
        self.assertEqual(self.multi_review.artist(), 'Radiohead')

    def test_multi_review_label(self):
        self.assertEqual(self.multi_review.label(), 'Capitol')

    def test_multi_review_year(self):
        self.assertEqual(self.multi_review.year(), '2009')

    def test_multi_review_url(self):
        self.assertEqual(self.multi_review.url, '/reviews/albums/12938-pablo-honey-collectors-edition-the-bends-collectors-edition-ok-computer-collectors-edition/')


if __name__ == '__main__':
    unittest.main()
