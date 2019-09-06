#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 10)

    # def test_stealability(self):
    #     """Test stealability function of a product working properly"""
    #     prod = Product(generate_products(num_products=1))
    #     self.assertMultiLineEqual(f'{prod.stealability}'), 'Very stealable')

    def test_default_num_products(self):
        """Test default number of products equal to 30"""
        self.assertEqual(len(generate_products()), 30)


if __name__ == '__main__':
    unittest.main()
