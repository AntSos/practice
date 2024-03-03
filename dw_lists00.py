
l1 = [9, 8, 7]
l2 = [2, 3]
lstr = ["Alix", "Parent", "Price", "Xenomorph", "contex", "Felix", 'simba', 'sambo', 'samba']



#Concatenate 2 list, takin the shortes lenght first

def concatenate_shortest (l1, l2):
    if len (l1) <= len (l2):
        shortest = l1
        longest = l2
    else: 
        shortest = l2
        longest = l1
    
    return shortest + longest


#Count elements in a list that end in a specific caracter

def count_endswith (lstr):
    count = 0
    for w in lstr:
        if w.endswith ("x"):
            count += 1
    
    return count

#Find and separete words with a specific string inside a list
def words_with (lstr):
    words_with_sstr = []

    for w in lstr:
        if "rph" in w: #Specific caracter str
            words_with_sstr.append (w)
   
    return words_with_sstr        

#Find and separete words that beging and end with a specifc str

def words_with_b_e (lstr):
    words_with_str_b_e = []
    for w in lstr:
        if w.startswith ("A") and w.endswith ("x"):
            words_with_str_b_e.append (w)
    
    return words_with_str_b_e


#Filter words with specif patern of separate strings 

def is_samba_words (word):
    s_index = word.find ("s")
    if s_index == -1:
        return False
    
    rest_after_s = word [s_index + 1:]
    m_index = rest_after_s.find ("m")
    
    if m_index == -1:
        return False
    
    rest_after_m = rest_after_s [m_index + 1:]
    return "b" in rest_after_m


#Filter the words
def filter (lstr):
    samba_words = []
    for w in lstr:
        if is_samba_words (w):
            samba_words.append (w)
            
    return samba_words

if __name__ == "__main__":

   l3 = concatenate_shortest (l1, l2)
   print (l3)

   lends_x =count_endswith (lstr)
   print (lends_x)

   ww_str = words_with (lstr)
   print (ww_str)
   
   ww_b_e = words_with_b_e (lstr)
   print (ww_b_e)

   is_s = filter (lstr)
   print (is_s)
