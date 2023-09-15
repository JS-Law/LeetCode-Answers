def canConstruct(ransomNote, magazine):
    m_dict = {}
    for c in magazine:
        if c not in m_dict:
            m_dict[c] = 1
        else:
            m_dict[c] += 1
    print(m_dict)
    for ch in ransomNote:
        if ch not in m_dict or m_dict[ch] == 0:
            print(ransomNote, m_dict)
            print("False")
        else:
            m_dict[ch] -= 1
            print(ransomNote, m_dict)
    print("True")



ransomNote = "aaab"
magazine = "bbaa"
canConstruct(ransomNote, magazine)