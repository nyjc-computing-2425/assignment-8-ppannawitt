def reverse(txt):
    """
    function return a string which is a reverse of txt

    txt: string
    return: string
    """
    if len(txt)==0:
        return ""
    if len(txt)==1:
        return txt
    return reverse(txt[1:]) + txt[0]

def is_palindrome(txt):

    """
    function return a boolean value representing whether txt is a palindrome or not

    num: string
    return: bool
    """
    if len(txt)<=1:
      return True
    return is_palindrome(txt[1:-1]) and txt[0].lower()==txt[-1].lower()

