import os
import unittest

from rdflib import Graph


class RdflibParserTestCase(unittest.TestCase):
    def test_issue_1(self):
        """ Another test for the rdflib embedded quote problem
        See line 1578 in notation3.py:
                k = 'abfrtvn\\"\''.find(ch)
                if k >= 0:
                    uch = '\a\b\f\r\t\v\n\\"\''[k]
        """
        g = Graph()
        data_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                      'data'
                                                      ))
        g.load(os.path.join(data_file_path, '1literalPattern_with_all_punctuation.ttl'), format="turtle")
        self.assertTrue(True, "")


if __name__ == '__main__':
    unittest.main()
