def get_num_words(file_path):
 with open(file_path) as f:
  num_words = f.read().split()
  print(f"{len(num_words)} words found in the document")

def get_num_chars(file_path):
 with open(file_path) as f:
  words_split = f.read().lower().split()
  e_count = 0
  t_count = 0
  a_count = 0
  o_count = 0
  i_count = 0
  n_count = 0
  s_count = 0
  r_count = 0
  h_count = 0
  d_count = 0
  l_count = 0
  m_count = 0
  u_count = 0
  c_count = 0
  f_count = 0
  y_count = 0
  w_count = 0
  p_count = 0
  g_count = 0
  b_count = 0
  v_count = 0
  k_count = 0
  x_count = 0
  j_count = 0
  q_count = 0
  z_count = 0
  æ_count = 0
  â_count = 0
  ê_count = 0
  ë_count = 0
  ô_count = 0

  for i in words_split:
   if (i.count('e')):
    e_count += i.count('e')
   if (i.count('t')):
    t_count += i.count('t')
   if (i.count('a')):
    a_count += i.count('a')
   if (i.count('o')):
    o_count += i.count('o')
   if (i.count('i')):
    i_count += i.count('i')
   if (i.count('n')):
    n_count += i.count('n')
   if (i.count('s')):
    s_count += i.count('s')
   if (i.count('r')):
    r_count += i.count('r')
   if (i.count('h')):
    h_count += i.count('h')
   if (i.count('d')):
    d_count += i.count('d')
   if (i.count('l')):
    l_count += i.count('l')
   if (i.count('m')):
    m_count += i.count('m')
   if (i.count('u')):
    u_count += i.count('u')
   if (i.count('c')):
    c_count += i.count('c')
   if (i.count('f')):
    f_count += i.count('f')
   if (i.count('y')):
    y_count += i.count('y')
   if (i.count('w')):
    w_count += i.count('w')
   if (i.count('p')):
    p_count += i.count('p')
   if (i.count('g')):
    g_count += i.count('g')
   if (i.count('b')):
    b_count += i.count('b')
   if (i.count('v')):
    v_count += i.count('v')
   if (i.count('k')):
    k_count += i.count('k')
   if (i.count('x')):
    x_count += i.count('x')
   if (i.count('j')):
    j_count += i.count('j')
   if (i.count('q')):
    q_count += i.count('q')
   if (i.count('z')):
    z_count += i.count('z')
   if (i.count('æ')):
    æ_count += i.count('æ')
   if (i.count('â')):
    â_count += i.count('â')
   if (i.count('ê')):
    ê_count += i.count('ê')
   if (i.count('ë')):
    ë_count += i.count('ë')
   if (i.count('ô')):
    ô_count += i.count('ô')

  return{
   'e': e_count,
   't': t_count,
   'a': a_count,
   'o': o_count,
   'i': i_count,
   'n': n_count,
   's': s_count,
   'r': r_count,
   'h': h_count,
   'd': d_count,
   'l': l_count,
   'm': m_count,
   'u': u_count,
   'c': c_count,
   'f': f_count,
   'y': y_count,
   'w': w_count,
   'p': p_count,
   'g': g_count,
   'b': b_count,
   'v': v_count,
   'k': k_count,
   'x': x_count,
   'j': j_count,
   'q': q_count,
   'z': z_count,
   'æ': æ_count,
   'â': â_count,
   'ê': ê_count,
   'ë': ë_count,
   'ô': ô_count, 
  }
 
def get_directionaries(file_path):
 with open(file_path) as f:
  word_directory = len(f.read().split())
  char_directory= get_num_chars(file_path)

  print(f"============ BOOKBOT ============")
  print(f"Analyzing book found at books/frankenstein.txt...")
  print(f"----------- Word Count ----------")
  print(f"Found {word_directory} total words")
  print(f"--------- Character Count -------")
  for key, value in char_directory.items():
   print(f"{key}: {value}")
  print(f"============= END ===============")

