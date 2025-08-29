# Script to check functionality of regular expressions.

import re

if __name__ == "__main__":
    test_strings = ["Test 123 A",
                    "Test 123 B",
                    "Test 123 C",
                    "Test 123 D",
                    "test 123 a",
                    "test 123 b",
                    "test 123 c",
                    "test 123 d",
                    "A&B",
                    "&amp;]
    
    # Match example.
    exp_1 = r"[Tt][Ee][Ss][Tt] .*[A-Ca-c]"

    exp_1_comp = re.compile(exp_1)

    for test_string in test_strings:
        result = exp_1_comp.match(test_string)
        print(result, "\n")

    # Find example.
    exp_2 = r"\w{1}$"
    
    exp_2_comp = re.compile(exp_2)

    for test_string in test_strings:
        result = exp_2_comp.findall(test_string)
        print(result, "\n")

    # Replace example.
    exp_3 = r"&(?!amp;)"
    exp_3_comp = re.compile(exp_3)

    exp_4 = r"&amp;"
    exp_4_comp = re.compile(exp_4)
    
    for test_string in test_strings:
        result = re.sub(exp_3, exp_4, test_string)
        print(result, "\n")
