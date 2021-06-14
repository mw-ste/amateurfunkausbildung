# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 19:25:33 2021

@author: Michael
"""

import re

sign_types = {
        "KS": "Klubstation",
        "RL": "Relais",
        "PZ": "Person",
        "AB": "Ausbildung",
        "FB": "Funkbake",
        "SZ": "Experimental"
        }

# In[]
def any_match(string, patterns):
    for pattern in patterns:
        if any(re.findall(pattern, string)):
            return True
    return False

# In[]
"""
AB_A
    DN1AA-DN6ZZZ
"""
re_AB_A = [r"^DN[1-6][A-Z]{2,3}$"]

assert any_match("DN1AA",  re_AB_A)
assert any_match("DN6ZZZ", re_AB_A)

# In[]
"""
AB_E
    DN7AA-DN8ZZZ
"""
re_AB_E = [r"^DN[7-8][A-Z]{2,3}$"]

assert any_match("DN7AA",  re_AB_E)
assert any_match("DN8ZZZ", re_AB_E)

# In[]
"""
AB_E_legacy
    DNØAA-DNØZZZ
"""
re_AB_E_legacy = [r"^DN0[A-Z]{2,3}$"]

assert any_match("DN0AA",  re_AB_E_legacy)
assert any_match("DN0ZZZ", re_AB_E_legacy)

# In[]
"""
FB_A
    DA1AA-DA1ZZZ
    DBØAA-DBØZZZ
    DMØAA-DMØZZZ
    DPØAA-DP1ZZZ
"""
re_FB_A = [r"^D([AP]1|[BMP]0)[A-Z]{2,3}$"]

assert any_match("DA1AA",  re_FB_A)
assert any_match("DA1ZZZ", re_FB_A)
assert any_match("DB0AA",  re_FB_A)
assert any_match("DB0ZZZ", re_FB_A)
assert any_match("DM0AA",  re_FB_A)
assert any_match("DM0ZZZ", re_FB_A)
assert any_match("DP0AA",  re_FB_A)
assert any_match("DP1ZZZ", re_FB_A)

# In[]
"""
FB_A_gast
    DA2AA-DA2ZZZ
"""
re_FB_A_gast = [r"^DA2[A-Z]{2,3}$"]

assert any_match("DA2AA",  re_FB_A_gast)
assert any_match("DA2ZZZ", re_FB_A_gast)

# In[]
"""
FB_A_legacy
    DFØAA-DFØZZZ
    DKØAA-DKØZZZ
    DLØAA-DLØZZZ
"""
re_FB_A_legacy = [r"^D[FKL]0[A-Z]{2,3}$"]

assert any_match("DF0AA",  re_FB_A_legacy)
assert any_match("DF0ZZZ", re_FB_A_legacy)
assert any_match("DK0AA",  re_FB_A_legacy)
assert any_match("DK0ZZZ", re_FB_A_legacy)
assert any_match("DL0AA",  re_FB_A_legacy)
assert any_match("DL0ZZZ", re_FB_A_legacy)

# In[]
"""
FB_E
    DA6AA-DA6ZZZ
    DOØAA-DOØZZZ
    DP2AA-DP2ZZZ
"""
re_FB_E = [r"^D(A6|O0|P2)[A-Z]{2,3}$"]

assert any_match("DA6AA",  re_FB_E)
assert any_match("DA6ZZZ", re_FB_E)
assert any_match("DO0AA",  re_FB_E)
assert any_match("DO0ZZZ", re_FB_E)
assert any_match("DP2AA",  re_FB_E)
assert any_match("DP2ZZZ", re_FB_E)

# In[]
"""
KS_A
    DAØA-DAØZ
    DA2A-DA3Z
    DBØA-DD9Z
    DFØA-DH9Z
    DJØA-DM9Z
    DP3A-DP9Z
    DQØA-DR9Z
    
    DAØAA-DAØZZZ
    DA1AA-DA1ZZZ
    DA2AA-DA2ZZZ
    DFØAA-DFØZZZ
    DKØAA-DKØZZZ
    DLØAA-DLØZZZ
"""
re_KS_A = [r"^D(A[02-3]|[B-DF-HJ-MQ-R][0-9]|P[3-9])[A-Z]$",
           r"^D(A[0-2]|[FKL]0)[A-Z]{2,3}$"]

assert any_match("DA0A", re_KS_A)
assert any_match("DA0Z", re_KS_A)
assert any_match("DA2A", re_KS_A)
assert any_match("DA3Z", re_KS_A)
assert any_match("DB0A", re_KS_A)
assert any_match("DD9Z", re_KS_A)
assert any_match("DF0A", re_KS_A)
assert any_match("DH9Z", re_KS_A)
assert any_match("DJ0A", re_KS_A)
assert any_match("DM9Z", re_KS_A)
assert any_match("DP3A", re_KS_A)
assert any_match("DP9Z", re_KS_A)
assert any_match("DQ0A", re_KS_A)
assert any_match("DR9Z", re_KS_A)

assert any_match("DA0AA",  re_KS_A)
assert any_match("DA0ZZZ", re_KS_A)
assert any_match("DA1AA",  re_KS_A)
assert any_match("DA1ZZZ", re_KS_A)
assert any_match("DA2AA",  re_KS_A)
assert any_match("DA2ZZZ", re_KS_A)
assert any_match("DF0AA",  re_KS_A)
assert any_match("DF0ZZZ", re_KS_A)
assert any_match("DK0AA",  re_KS_A)
assert any_match("DK0ZZZ", re_KS_A)
assert any_match("DL0AA",  re_KS_A)
assert any_match("DL0ZZZ", re_KS_A)

# In[]
"""
KS_A_gast
    DA1A-DA1Z
"""
re_KS_A_gast = [r"^DA1[A-Z]$"]

assert any_match("DA1A", re_KS_A_gast)
assert any_match("DA1Z", re_KS_A_gast)

# In[]
"""
KS_A_legacy
    DBØAA-DBØZZZ
    DCØAA-DCØZZZ
    DDØAA-DDØZZZ
    DGØAA-DGØZZZ
    DHØAA-DHØZZZ
    DJØAA-DJØZZZ
    DMØAA-DMØZZZ
"""
re_KS_A_legacy = [r"^D[B-DGHJM]0[A-Z]{2,3}$"]

assert any_match("DB0AA",  re_KS_A_legacy)
assert any_match("DB0ZZZ", re_KS_A_legacy)
assert any_match("DC0AA",  re_KS_A_legacy)
assert any_match("DC0ZZZ", re_KS_A_legacy)
assert any_match("DD0AA",  re_KS_A_legacy)
assert any_match("DD0ZZZ", re_KS_A_legacy)
assert any_match("DG0AA",  re_KS_A_legacy)
assert any_match("DG0ZZZ", re_KS_A_legacy)
assert any_match("DH0AA",  re_KS_A_legacy)
assert any_match("DH0ZZZ", re_KS_A_legacy)
assert any_match("DJ0AA",  re_KS_A_legacy)
assert any_match("DJ0ZZZ", re_KS_A_legacy)
assert any_match("DM0AA",  re_KS_A_legacy)
assert any_match("DM0ZZZ", re_KS_A_legacy)

# In[]
"""
KS_A_ext
    DPØA-DP1Z
    DPØAA-DP1ZZZ
"""
re_KS_A_ext = [r"^DP[0-1][A-Z]{1,3}$"]

assert any_match("DP0A",   re_KS_A_ext)
assert any_match("DP1Z",   re_KS_A_ext)
assert any_match("DP0AA",  re_KS_A_ext)
assert any_match("DP1ZZZ", re_KS_A_ext)

# In[]
"""
KS_E
    DA7A-DA9Z
    DNØA-DNØZ
    DOØA-DO9Z
    
    DA6AA-DA6ZZZ
    DNØAA-DNØZZZ
"""
re_KS_E = [r"^D(A[7-9]|N0|O[0-9])[A-Z]$",
           r"^D(A6|N0)[A-Z]{2,3}$"]

assert any_match("DA7A",   re_KS_E)
assert any_match("DA9Z",   re_KS_E)
assert any_match("DN0A",   re_KS_E)
assert any_match("DN0Z",   re_KS_E)
assert any_match("DO0A",   re_KS_E)
assert any_match("DO9Z",   re_KS_E)

assert any_match("DA6AA",  re_KS_E)
assert any_match("DA6ZZZ", re_KS_E)
assert any_match("DN0AA",  re_KS_E)
assert any_match("DN0ZZZ", re_KS_E)

# In[]
"""
KS_E_gast
    DA6A-DA6Z
"""
re_KS_E_gast = [r"^DA6[A-Z]$"]

assert any_match("DA6A", re_KS_E_gast)
assert any_match("DA6Z", re_KS_E_gast)


# In[]
"""   
KS_E_legacy
    DOØAA-DOØZZZ
    
KS_E_ext
    DP2A-DP2Z
    DP2AA-DP2ZZZ
    
KS_SZ_A
    DA5A-DA5Z
    
KS_SZ_E
    DA4A-DA4Z
    
PZ_A
    DB1AA-DB9ZZZ
    DB1AA-DB9ZZZ
    DDØAA-DD9ZZZ
    DF1AA-DF9ZZZ
    DGØAA-DG9ZZZ
    DHØAA-DH9ZZZ
    DJØAA-DJ9ZZZ
    DK1AA-DK9ZZZ
    DL1AA-DL9ZZZ
    DM1AA-DM9ZZZ
    
PZ_A_gast
    DA1AA-DA1ZZZ
    
PZ_A_legacy
    DA2AA-DA2ZZZ
    
PZ_A_legacy_gast    

PZ_E
    DO1AA-DO9ZZZ

PZ_E_gast
    DA6AA-DA6ZZZ
    
RL_A
    DA1AA-DA1ZZZ
    DA2AA-DA2ZZZ
    DBØAA-DBØZZZ
    DMØAA-DMØZZZ
    DPØAA-DP1ZZZ
    
RL_A_legacy
    DFØAA-DFØZZZ
    DKØAA-DKØZZZ
    DLØAA-DLØZZZ
    
RL_E
    DA6AA-DA6ZZZ
    DOØAA-DOØZZZ
    DP2AA-DP2ZZZ
    
SZ_A
    DA5AA-DA5ZZZ
    DPØAA-DP1ZZZ

SZ_E
    DA4AA-DA4ZZZ
    DP2AA-DP2ZZZ

"""