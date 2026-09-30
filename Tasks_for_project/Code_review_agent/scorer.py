# True  = bug expected
# False = no bug expected
import os
from main import review_code
test_files = {
    "1_test_sql_injection.py" : True,
    "2_test_hardcoded_secret.py" : True,
    "3_test_md5_password_hashing.py" : True,
    "4_test_missingKey.py" : True,
    "5_test_unclosed_file.py" : True,
    "6_test_safe_divison.py" : False,
    "7_test_password_check.py" : False,
}

passed = 0 

for filename , expected_bug in test_files.items():
    with open(os.path.join("test/",filename)) as file:
        code = file.read()
        findings = review_code(code)

        print(findings)
        
        if(
            expected_bug and findings  or
            not expected_bug and not findings
        ):
            passed+=1
            print(f"{filename} -> PASS")
            print("="*50)
            
        else:
            print(f"{filename} -> FAIL")
            print("="*50)
            

print(f"Score: {passed}/{len(test_files)}")