[![Build Status](https://travis-ci.org/benpetty/Code-Katas.svg?branch=master)](https://travis-ci.org/benpetty/Code-Katas) [![Coverage Status](https://coveralls.io/repos/github/benpetty/Code-Katas/badge.svg?branch=master)](https://coveralls.io/github/benpetty/Code-Katas?branch=master)

# Code Katas 

Various coding challenges and my solutions. Descriptions in source code.

***

### Does my number look big in this? (6 kyu)

- Module: `narcissistic.py`
- Tests: `test_narcissistic.py`
- Link: https://www.codewars.com/kata/5287e858c6b5a9678200083c
  - Interesting solution by [pavel.koshev](https://www.codewars.com/users/pavel.koshev):

    ```python
    def narcissistic(value):
        return bool(value==sum([int(a) ** len(str(value)) for a in str(value)]))
    ```

***

### Sum of Digits / Digital Root (6 kyu)

- Module: `digital_root.py`
- Tests: `test_digital_root.py`
- Link: https://www.codewars.com/kata/541c8630095125aba6000c00
  - Interesting solution by [bartholomisha](https://www.codewars.com/users/bartholomisha):

    ```python
    def digital_root(n):
        return n%9 or n and 9
    ```

***

### Sort deck of cards (7 kyu)

- Module: `sort_cards.py`

- Tests: `test_sort_cards.py`

- Link: https://www.codewars.com/kata/56f399b59821793533000683/

  - Interesting solution by [zebulan](https://www.codewars.com/users/zebulan)

    ```Python
    def sort_cards(cards):
        return sorted(cards, key="A23456789TJQK".index)
    ```

***

### Sum of the first nth term of Series (7 kyu)

- Module: `sum_of_nth.py`
- Tests: `test_sum_terms.py`
- Link: http://www.codewars.com/kata/555eded1ad94b00403000071
  - Interesting Solution by [Chrisi](http://www.codewars.com/users/Chrisi):

    ```python
    def series_sum(n):
        sum = 0.0
        for i in range(0,n):
            sum += 1 / (1 + 3 * float(i))
        return '%.2f' % sum
    ```


***

### Jaden Casing Strings (7 kyu)

- Module: `jaden_casing.py`
- Tests: `test_jaden_casing.py`
- Link: https://www.codewars.com/kata/5390bac347d09b7da40006f6
  - Interesting Solution by : [Azuaron](https://www.codewars.com/users/Azuaron), [Xavierxf-](https://www.codewars.com/users/Xavierxf-), [dalvarado](https://www.codewars.com/users/dalvarado), [swerty](https://www.codewars.com/users/swerty), [felixbr](https://www.codewars.com/users/felixbr), [wo0dyn](https://www.codewars.com/users/wo0dyn) (plus 92 more warriors):

    ```python
    def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())
    ```


***

### Regex validate PIN code (7 kyu)

- Module: `validate_pin.py`
- Tests: `test_validate_pin.py`
- Link: https://www.codewars.com/kata/55f8a9c06c018a0d6e000132
  - Interesting Solution by [CrazyMerlyn](https://www.codewars.com/users/CrazyMerlyn), [pivek303](https://www.codewars.com/users/pivek303), [lechevalier](https://www.codewars.com/users/lechevalier), [aytrack](https://www.codewars.com/users/aytrack), [bugaevc](https://www.codewars.com/users/bugaevc), [andriis](https://www.codewars.com/users/andriis) (plus 18 more warriors):

    ```python
    def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()
    ```

***

### Highest and Lowest (7 kyu)

- Module: `highest_and_lowest.py`
- Tests: `test_highest_and_lowest.py`
- Link: https://www.codewars.com/kata/554b4ac871d6813a03000035
  - Interesting Solution by [Deantwo](https://www.codewars.com/users/Deantwo):

    ```python
    def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
    ```

***

### Get the Middle Character (7 kyu)

- Module: `get_middle.py`
- Tests: `test_get_middle.py`
- Link: https://www.codewars.com/kata/56747fd5cb988479af000028
  - Interesting Solution by [hiasen](https://www.codewars.com/users/hiasen), [kit9ra](https://www.codewars.com/users/kit9ra), [GNX](https://www.codewars.com/users/GNX), [niedyszyn](https://www.codewars.com/users/niedyszyn), [RandomJack](https://www.codewars.com/users/RandomJack), [pstryq](https://www.codewars.com/users/pstryq) (plus 7 more warriors):

    ```Python
    def get_middle(s):
        return s[(len(s)-1)/2:len(s)/2+1]
    ```

***

### Find the smallest integer in the array (7 kyu)

- Module: `find_smallest_int.py`
- Tests: `test_find_smallest_int.py`
- Link: https://www.codewars.com/kata/55a2d7ebe362935a210000b2
  - Interesting solution by [z423x5c6](https://www.codewars.com/users/z423x5c6), [Azuaron](https://www.codewars.com/users/Azuaron), [suic](https://www.codewars.com/users/suic), [Chrisi](https://www.codewars.com/users/Chrisi), [pivek303](https://www.codewars.com/users/pivek303), [SleepingCode](https://www.codewars.com/users/SleepingCode) (plus 27 more warriors):

  ```python
    findSmallestInt=min
  ```


***

### Multiply (8 kyu)

- Module: `multiply.py`
- Tests: `test_multiply.py`
- Link: https://www.codewars.com/kata/50654ddff44f800200000004
  - Interesting solution by [jihygk](https://www.codewars.com/users/jihygk):

  ```python
    multiply = __import__('operator').mul
  ```

***

### Forbes Top 40

- Module: `forbes_top_40.py`
- Tests: `test_multiply.py`
- Collaborated with Joey DeRosa and Rick Valenzuela to find the solution I implemented.


***

### Count Code

- Module: `count_code.py`

- Tests: `test_count_code.py`

- Link: [http://codingbat.com/prob/p186048](http://codingbat.com/prob/p186048)

***

### Double Char

- Module: `double_char.py`
- Tests: `test_double_char.py`
- Link: [http://codingbat.com/prob/p170842](http://codingbat.com/prob/p170842)

***

