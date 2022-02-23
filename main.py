from lib.fuzzy_word_search_results import FuzzyWordSearch


fuzzy_search = FuzzyWordSearch("json/test_input.json")

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

$ fuzzy_search = FuzzyWordSearch('json/test_input.json')
$ fuzzy_search.run()
"""
    )

fuzzy_search.print_results_dict()
