from lib.fuzzy_word_search_results import FuzzyWordSearch

class FWSearch(FuzzyWordSearch):
    """docstring for FWSearch"""
    def __init__(self, json_filepath):
        FuzzyWordSearch.__init__(self, json_filepath)

    def fwsprint(self):
        return self.print_results()

    def fwsdict(self):
        return self.print_results_dict()

    

