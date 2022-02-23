import json


# Performs a 'fuzzy search' on given JSON.
# See test_input.json for JSON format
class FuzzyWordSearch(object):
    """
    Performs a 'fuzzy word search' on given JSON. See test_input.json for JSON format.
    Initiate FuzzyWordSearch with the path to the JSON file as the argument. Once
    initiated, the 'run()' method will execute the 'fuzzy search' and print the
    results.
    """

    def __init__(self, json_filepath):
        super(FuzzySearch, self).__init__()
        # Opening JSON file
        f = open(json_filepath)
        # returns JSON object as a dictionary
        self.data = json.load(f)
        # creates a dictionary for the results
        self.fuzzy_search_dict = {}
        # iterates through queries and adds them as keys in fuzzy_search_dict
        for query in self.data["queries"]:
            # the value is a dictionary.
            # end format = {query:{phrase:value, fuzzy match:value},}
            self.fuzzy_search_dict[query] = {}

    def check_if_words_match(self, query, phrase):
        """
        Called in the method 'add_phrases_to_fuzzy_search_dict()'. Takes a
        string query and a string phrase. If more than one word in phrase is
        in query, calls method 'check_if_in_range()' which returns False or a
        dictionary with the start index and end index of the matched words
        within the query.
        """
        # list for words in matching phrase
        words = []
        # iterate over each word in phrase
        for word in phrase.split():
            # if the word is present in the query continue
            if word in query.split():
                # Add the word to the list 'words'
                words.append(word)
        # If more than one word in the list 'words' continue
        if len(words) >= 2:
            # Call method 'check_if_in_range()' to return dict of the start
            # index and the end index of the matching phrase within the query
            result = self.check_if_in_range(query, words)
            return result
        else:
            return False

    def check_if_in_range(self, query, list_of_words):
        """
        Called in the method 'check_if_words_match()'. Takes a string query
        and a list of string words (list_of_words). Defines start index and
        end index for query with allowance of one additional word. If more
        than one additional word, returns False
        """
        # value set to reduce
        index_start = 1000000
        # value set to increase
        index_end = 0
        # list_of_words holds words from matching phrases.
        for word in list_of_words:
            # var i will hold the index of the word in the query
            i = query.split().index(word)
            # adjust the vars 'index_start' and 'index_end' accordingly.
            if i <= index_start:
                index_start = i
            if i > index_end:
                index_end = i
        # If word count in list_of_words covers the index spread return indexes
        if (len(list_of_words)) < abs(index_end - index_start):
            return False
        else:
            return {"index start": index_start, "index end": index_end}

    def add_phrases_to_fuzzy_search_dict(self):
        """
        Search all phrases against each query. Calls 'check_if_words_match()'
        to return dictionary containing the index start and index end for the
        matched phrase within the query. Returns an updated fuzzy_search_dict
        with matching phrases and fuzzy match string from query.
        """
        for query in self.fuzzy_search_dict:
            for phrase in self.data["phrases"]:
                words_match = self.check_if_words_match(query, phrase)
                if words_match:
                    try:
                        if self.fuzzy_search_dict[query]["phrases"]:
                            pass
                    except KeyError:
                        self.fuzzy_search_dict[query]["phrases"] = []
                    fuzzy_match_str = " ".join(
                        query.split()[
                            words_match["index start"] : words_match["index end"] + 1
                        ]
                    )
                    self.fuzzy_search_dict[query]["phrases"].append(
                        {"original phrase": phrase, "fuzzy match": fuzzy_match_str}
                    )
        return self.fuzzy_search_dict

    def print_results(self):
        """
        Prints fuzzy_search_dict data in formated string
        """
        for query in self.fuzzy_search_dict:
            try:
                if self.fuzzy_search_dict[query]["phrases"]:
                    print(f"\n\n\nQuery: {query}")
                    for phrase in self.fuzzy_search_dict[query]["phrases"]:
                        print(
                            f"""{self.fuzzy_search_dict[query]['phrases'].index(phrase) +1}
Phrase: {phrase['original phrase']}
Fuzzy Search: {phrase['fuzzy match']}"""
                        )
            except KeyError:
                pass

    def run(self):
        """
        Calls 'add_phrases_to_fuzzy_search_dict()' and 'print_results()'. If
        FuzzySearch is initiated with a properly formated JSON file, calling
        'run()' with run through the class methods and print out the result.
        """
        self.add_phrases_to_fuzzy_search_dict()
        self.print_results()


# fuzzy_search = FuzzyWordSearch('test_input.json')
# fuzzy_search.run()
