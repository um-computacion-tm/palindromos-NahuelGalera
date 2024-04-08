import unittest

def es_palindrome(mystring):
    for indice in range(0, len(mystring)):
        print(mystring[indice] + " --> " + mystring[-(indice +1)])
        if mystring[indice] !=  mystring[-(indice+1)]:
            print("no es\n")
            return False
    return True
    return mystring[0] == mystring[-1]


class TestPalindrome(unittest.TestCase):
    def test_a(self):
        resultado = es_palindrome('a')
        self.assertEqual(resultado, True)

    def test_b(self):
        resultado = es_palindrome('B')
        self.assertEqual(resultado, True)

    def test_aa(self):
        resultado = es_palindrome('aa')
        self.assertEqual(resultado, True)

    def test_ab(self):
        resultado = es_palindrome('ab')
        self.assertEqual(resultado, False)

    def test_aCa(self):
        resultado = es_palindrome('aCa')
        self.assertEqual(resultado, True)

    def test_aCs(self):
        resultado = es_palindrome('aCs')
        self.assertEqual(resultado, False)

    def test_ABBA(self):
        resultado = es_palindrome('ABBA')
        self.assertEqual(resultado, True)

    def test_ABCA(self):
        resultado = es_palindrome('BACB')
        self.assertEqual(resultado, False)

    def test_ABCBA(self):
        resultado = es_palindrome('ABCBA')
        self.assertEqual(resultado, True)

    def test_ABCCBA(self):
        resultado = es_palindrome('ABCCBA')
        self.assertEqual(resultado, True)

    def test_ZBCCBA(self):
        resultado = es_palindrome('ZBCCBA')
        self.assertEqual(resultado, False)

    def test_neuquen(self):
        resultado = es_palindrome('neuquen')
        self.assertEqual(resultado, True)

    def test_neuqueM(self):
        resultado = es_palindrome('neuqueM')
        self.assertEqual(resultado, False)

unittest.main()