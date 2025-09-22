import sys
from stats import get_num_words, get_num_chars, get_directionaries

def get_book_text(file_path):
 with open(file_path) as f:
  file_contents = f.read()
  return file_contents; 

def main():
 if (len(sys.argv) != 2):
  print(f"Usage: python3 main.py <path_to_book>")
 print(get_book_text(sys.argv[1]))
 print(get_num_words(sys.argv[1]))
 print(get_num_chars(sys.argv[1]))
 print(get_directionaries(sys.argv[1]))

main()