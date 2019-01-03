import collections
import re
import sys
import time


def tokenize(string):
    """Convert string to lowercase and split into words (ignoring
    punctuation), returning list of words.
    """
    return re.findall(r'\w+', string.lower())

def count_ngrams(lines):
    """For each line find all unique word sequences up to max length
    then add to collection"""
    ngrams = collections.Counter()
    line_count = 0
    for line in lines:
        words = tokenize(line)
        length = len(words)
        current = 0
        queue = []
        max_length = 8
        for i in range(length+1):
            for j in range(i+1,i+1+max_length):
                if j <= length:
                    queue.append(tuple(words[i:j]))
        print(line_count)
        line_count += 1
        for ngram in set(queue):
            ngrams[ngram] += 1
    return ngrams

def print_most_frequent(ngrams, num=1200):
    with open("pattern.txt", "w") as handle:
        for gram, count in ngrams.most_common(num):
            data = '{0}:{1}'.format(count, ';'.join(gram))
            print(data)
            if count > 99:
                handle.write(data + '\n')
    print('')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python ngrams.py filename')
        sys.exit(1)

    start_time = time.time()
    with open(sys.argv[1]) as f:
        ngrams = count_ngrams(f)
    print_most_frequent(ngrams)
    elapsed_time = time.time() - start_time
print('Took {:.03f} seconds'.format(elapsed_time))
