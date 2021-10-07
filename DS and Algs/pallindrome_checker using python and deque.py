from Deque import Deque
def pal_checker(a_string):
    char_deque = Deque()
    for ch in a_string:
        char_deque.add_rear(ch)
        
    still_ok = True
    
    while char_deque.size() > 1 and still_ok:
        x = char_deque.remove_front()
        y = char_deque.remove_rear()
        if x != y:
            still_ok = False
    return still_ok
print(pal_checker('madam'))
print(pal_checker('fuck'))
print(pal_checker('radar'))
