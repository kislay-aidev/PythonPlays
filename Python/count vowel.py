def count_vow_cons(text):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
                
