def cipher(text, shift, encrypt=True):
    """"
     Encrypts text using a caesar cypher.

    Parameters
    ----------
    text : obj
      A string that you wish to encrypt.
    shift : int
      A number indicating how much you would like to shift each letter in the text by.
    encrypt: bool
        Takes either True or False depending on whether you want to encrypt/decrypt the function
        (shifts upward if set to false and not used for decryption). Assumes True.

    Returns
    -------
    The new encrypted text.

    Examples
    --------
    >>> from cipher_tn2472 import cipher_tn2472
    >>> cipher_tn2472.cipher("Dtwvwu", 2, encrypt = False)
    >>> 'Brutus'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text