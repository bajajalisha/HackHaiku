import random

exception_dict = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[]}

vowel_counts = list(exception_dict.keys())


#artsy/poetic words

one_vowel = ['sky','blue','life','cloud','hole','yes','bliss','hue',
             'zeal','red','grey','black','love','glee','heart','soul',
             'skin','bones','moon'] 

two_vowels = ['dappled','dulcet','nectar','happy','sublime','alone',
              'abyss','azure','verdant','hollowed','empty','silence']

three_vowels = ['seraphim','effulgent','daffodils','happily','gossamer',
                'staccato','crescendo','cicadas','poetry','entropy']

four_vowels = ['vermillion','cerulean','serenity','arcadian','ethereal',
               'ephemeral','eternity','iridescent']

#words functions

def exception_checker(word):
		result = False
		exception_list = exception_dict.values()
		
		for i in exception_list:
				if word in i:
						result = True

		return result

def exception_vowels(word):
		vowel = 0
		for key, value in exception_dict.items():    
				if word == value:
						vowel = key
		return vowel
      
def exception_adder(vowel_sounds, word):
    if 0 <= vowel_sounds <= 7:
        exception_dict[vowel_sounds].append(word)
    elif vowel_sounds <= 0:
        print("Error: Number of vowels sounds is too low")
    elif vowel_sounds >= 7:
        print("Error: Number of vowels sounds is too high")
        
def add_words(vowels_allowed, word_list):
    if vowels_allowed == 1:
        word_list.append(random.choice(one_vowel))
        return word_list
    
    elif vowels_allowed == 2:
        word_list.append(random.choice(two_vowels))
        return word_list
    
    elif vowels_allowed == 3:
        random_num = random.choice([1,2])
        if random_num == 1:
            word_list.append(random.choice(three_vowels))
            return word_list
        else:
            word_list.append(random.choice(one_vowel))
            word_list.append(random.choice(two_vowels))
            return word_list
        
    elif vowels_allowed == 4:
        random_num = random.choice([1,2,3])
        if random_num == 1:
            word_list.append(random.choice(four_vowels))
            return word_list
        elif random_num == 2:
            word_list.append(random.choice(two_vowels))
            word_list.append(random.choice(two_vowels))
            return word_list
        else:
            word_list.append(random.choice(one_vowel))
            word_list.append(random.choice(three_vowels))
            return word_list
        
    elif vowels_allowed == 5:
        random_num = random.choice([1,2])
        if random_num == 1:
            word_list.append(random.choice(three_vowels))
            word_list.append(random.choice(two_vowels))
            return word_list
        else:
            word_list.append(random.choice(one_vowel))
            word_list.append(random.choice(four_vowels))
            return word_list
        
    elif vowels_allowed == 6:
        random_num = random.choice([1,2,3])
        if random_num == 1:
            word_list.append(random.choice(four_vowels))
            word_list.append(random.choice(two_vowels))
            return word_list
        elif random_num == 2:
            word_list.append(random.choice(three_vowels))
            word_list.append(random.choice(three_vowels))
            return word_list
        else:
            word_list.append(random.choice(one_vowel))
            word_list.append(random.choice(three_vowels))
            word_list.append(random.choice(two_vowels))
            return word_list
            
    elif vowels_allowed == 7:
        random_num = random.choice([1,2,3,4])
        if random_num == 1:
            word_list.append(random.choice(four_vowels))
            word_list.append(random.choice(three_vowels))
            return word_list
        elif random_num == 2:
            word_list.append(random.choice(three_vowels))
            word_list.append(random.choice(three_vowels))
            word_list.append(random.choice(one_vowel))
            return word_list
        elif random_num ==3:
            word_list.append(random.choice(four_vowels))
            word_list.append(random.choice(one_vowel))
            word_list.append(random.choice(two_vowels))
            return word_list
        else:
            word_list.append(random.choice(two_vowels))
            word_list.append(random.choice(three_vowels))
            word_list.append(random.choice(two_vowels))
            return word_list                
    
