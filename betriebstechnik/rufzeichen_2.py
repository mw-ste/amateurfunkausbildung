# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:14:06 2021

@author: Michael
"""

import re

"""
"KS": "Klubstation",
"RL": "Relais",
"PZ": "Person",
"AB": "Ausbildung",
"FB": "Funkbake",
"SZ": "Experimental"
"""

# In[]
def any_match(string, patterns):
    for pattern in patterns:
        if any(re.findall(pattern, string)):
            return True
    return False

# In[]

re_AB_A = [r"^DN[1-6][A-Z]{2,3}$"]
re_AB_E = [r"^DN[07-8][A-Z]{2,3}$"]


re_FB_A = [r"^DA[12][A-Z]{2,3}$",
           r"^D[BFKLMP]0[A-Z]{2,3}$",
           r"^DP1[A-Z]{2,3}$"]
re_FB_E = [r"^D(A6|O0|P2)[A-Z]{2,3}$"]


re_KS_A = [r"^DA[0-35][A-Z]$",
           r"^DP[013-9][A-Z]$",
           r"^D[BCDFGHJKLMQR][0-9][A-Z]$",
           r"^D[ABCDFGHJKLMP]0[A-Z]{2,3}$",
           r"^DA[12][A-Z]{2,3}$",
           r"^DP1[A-Z]{2,3}$"]
re_KS_E = [r"^DA[46-9][A-Z]$",
           r"^DN0[A-Z]$",
           r"^DO[0-9][A-Z]$",
           r"^DP2[A-Z]$",
           r"^DA6[A-Z]{2,3}$",
           r"^D[NO]0[A-Z]{2,3}$",
           r"^DP2[A-Z]{2,3}$"]


re_PZ_A = [r"^DA[124][A-Z]{2,3}$",
           r"^D[BFKLM][1-9][A-Z]{2,3}$",
           r"^D[DGHJ][0-9][A-Z]{2,3}$"]
re_PZ_E = [r"^DA6[A-Z]{2,3}$",
           r"^DO[1-9][A-Z]{2,3}$"]


re_RL_A = [r"^DA[1-2][A-Z]{2,3}$",
           r"^D[BFKLMP]0[A-Z]{2,3}$",
           r"^DP1[A-Z]{2,3}$"]
re_RL_E = [r"^DA6[A-Z]{2,3}$",
           r"^DO0[A-Z]{2,3}$",
           r"^DP2[A-Z]{2,3}$"]


re_SZ_A = [r"^DA5[A-Z]{2,3}$",
           r"^DP[01][A-Z]{2,3}$"]
re_SZ_E = [r"^DA4[A-Z]{2,3}$",
           r"^DP2[A-Z]{2,3}$"]


# In[]
res = {"AB_A" : re_AB_A,
       "AB_E" : re_AB_E,
       "FB_A" : re_FB_A,
       "FB_E" : re_FB_E,
       "KS_A" : re_KS_A,
       "KS_E" : re_KS_E,
       "PZ_A" : re_PZ_A,
       "PZ_E" : re_PZ_E,
       "RL_A" : re_RL_A,
       "RL_E" : re_RL_E,
       "SZ_A" : re_SZ_A,
       "SZ_E" : re_SZ_E}

# In[]
def identify_sign(call_sign):
    matches = [r for r in res if any_match(call_sign, res[r])]
    if not any(matches):
        print("invalid call sign", call_sign)
    else:
        for m in matches:
            print(m)
                
                
def identify_sign_repl():
    while True:
        call_sign = input("Call sign: ").upper()
        if not call_sign:
            break
        
        identify_sign(call_sign)
                
                
# In[]
def generate_call_signs():
    import exrex
    import random
    
    while True:
        random_type = [key for key in res][random.randint(1, len(res)) - 1]
        random_res = res[random_type]
        random_re = random_res[random.randint(1, len(random_res)) - 1]
        
        generated = exrex.getone(random_re)
        print(generated)
        
        if input().lower() in ["exit", "quit", "q"]:
            break
        
        print(random_re)
        identify_sign(generated)
        
        if input().lower() in ["exit", "quit", "q"]:
            break
        
# In[]
generate_call_signs()