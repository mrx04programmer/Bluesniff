from googlesearch import search
import numpy
import sys
from brain import *

def search_google(query):
    results = []
    for j in search(query, num=10, stop=10, pause=2):
        results.append(j)
    return results

def get_search_results_text(query):
    search_results = search_google(query)
    result_text = []
    for result in search_results:
        result_text.append(result)
    
    return result_text

def main(query):
    results = get_search_results_text(query)
    for result in results:
        print(result)
        print("-"*len(result))
        
if __name__ == '__main__':
    try:
        query = str(sys.argv[1])
        main(query)
    except Exception:
        print(f"Uso : python {sys.argv[0]} 'consulta'")