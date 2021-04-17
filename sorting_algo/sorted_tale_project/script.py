import utils
import sorts
print('here we start')
bookshelf = utils.load_books('books_small.csv')
long_bookshelf = utils.load_books('books_large.csv')
for book in bookshelf:
  book['author_lower'] = book['author'].lower()
  book['title_lower'] = book['title'].lower()

for book in long_bookshelf:
  book['author_lower'] = book['author'].lower()
  book['title_lower'] = book['title'].lower()

bookshelf_v1 = bookshelf[:]
bookshelf_v2 = bookshelf[:]

def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

def by_total_length(book_a, book_b):
  return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])

sort1 = sorts.bubble_sort(bookshelf, by_title_ascending)

# print('sorting by title .........')
# for book in sort1:
#   print(book['title'])

sort2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
# print('\nsorting by author name .........')
# for book in sort1:
#   print(book['author'])

#sort3 = sorts.bubble_sort(long_bookshelf, by_total_length)
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) -1, by_author_ascending)

sorts.quicksort(long_bookshelf, 0, len(bookshelf_v2) -1, by_author_ascending)

for book in bookshelf_v2:
  print(book['author'])


