def find(s):
    arr = {
        "CU": "see you",
        ":-)": "I’m happy",
        ":-()": "I’m unhappy",
        ";-)": "wink",
        ":-P": "stick out my tongue",
        "(~.~)": "sleepy",
        "TA": "totally awesome",
        "CCC": "Canadian Computing Competition",
        "CUZ": "because",
        "TY": "thank-you",
        "YW": "you’re welcome",
        "TTYL": "talk to you later"
    }
    if s in arr:
        s = arr[s]
    return s
while True:
    try:
        s = input()
    except EOFError:
        break
    print(find(s=s))