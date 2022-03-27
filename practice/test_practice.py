from sklearn.decomposition import DictionaryLearning


nums = [2,4,6,8]
string = "Parth"
Dictionary = {'a':1,'b':2,'c':3,'device':4}

def test_even_items_in_lists():
    #assert [x%2 for x in nums] == [0,0,0,0]
    assert all([x%2 == 0 for x in nums]), "List has atleast one odd element"

def test_check_upper_case_in_first_letter():
    assert string[0].isupper(), "First letter of string is not in upper case"

def test_min_list_length():
    assert len(nums) >= 3, "List has less than 3 elements"

def test_key_in_dict():
    assert ("device" in Dictionary), "Dictionary does not have device"