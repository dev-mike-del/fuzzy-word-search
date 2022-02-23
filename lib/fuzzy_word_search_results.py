"""This module performs a 'fuzzy search on on JSON file"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from lib.fuzzy_word_search_work import FuzzyWordSearchWork


# Performs a 'fuzzy search' on given JSON.
# See test_input.json for JSON format
class FuzzyWordSearch:
    """
    Performs a 'fuzzy word search' on given JSON. See test_input.json for JSON format.
    Instantiate FuzzyWordSearch with the path to the JSON file as the argument. Once
    initiated, the 'run()' method will execute the 'fuzzy search' and print the
    results.
    """

    def __init__(self, json_filepath):
        FuzzyWordSearchWork().__init__(json_filepath)

    def print_results(self):
        """
        Prints fuzzy_search_dict data in formated string
        """
        for query in self.fuzzy_search_dict:
            try:
                if self.fuzzy_search_dict[query]["phrases"]:
                    print(f"\nQuery: {query}")
                    for phrase in self.fuzzy_search_dict[query]["phrases"]:
                        print(
                            f"""{self.fuzzy_search_dict[query]['phrases'].index(phrase) +1}
Phrase: {phrase['original phrase']}
Fuzzy Search: {phrase['fuzzy match']}"""
                        )
            except KeyError:
                pass

    def print_results_dict(self):
        """
        Calls 'add_phrases_to_fuzzy_search_dict()' and 'print_results()'. If
        FuzzySearch is initiated with a properly formated JSON file, calling
        'run()' with run through the class methods and print out the result.
        """
        print(self.fuzzy_search_dict)


if __name__ == "__main__":
    fuzzy_search = FuzzyWordSearch("test_input.json")
    print(
        """
Runing fuzzy_word_search.py directly will show this example. This example uses
test_input.json to demonstrait the 'fuzzy search'

This module performs a 'fuzzy search' on on JSON file. See test_input.json for
JSON format. Instantiate FuzzyWordSearch class with the path to the JSON file
as the argument. Once instantiated, the 'run()' method will execute the
'fuzzy search' and print the results. The JSON includes a list of phrases. The
current configuration allows for one extra word in the phrase. Also, the JSON
includes a list of queries. The class "FuzzyWordSearch" fuzzy searches all the
phrases in each query string. Finally, test_input.json includes a list of
solutions for testing purposes.

$ fuzzy_search = FuzzyWordSearch('test_input.json')
$ fuzzy_search.run()
"""
    )
    fuzzy_search.print_results_dict()
