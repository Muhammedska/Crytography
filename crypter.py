class Crypt:
    class vigenere:
        def crypte(text='', key=''):
            charlist = "abcdefghıjklmnopqrstuvwxyz"
            
            crypt1 = []
            crypt2 = []
            crypt3 = []

            trep = 0
            treped = ""
            output = ""

            if len(text) % len(key) == 0:
                trep = len(text) / len(key)
                treped = key*int(trep)
            else:
                calc1 = len(text) // len(key)
                calc2 = len(key) * calc1
                calc3 = len(text) - calc2
                calc4 = calc2 + calc3
                treped = (key * int(calc1))+(key[0:calc3])
            for i in text:
                crypt1.append(charlist.index(i))
            for i in treped:
                crypt2.append(charlist.index(i))

            indi = 0
            for i in crypt1:
                crypt3.append((i+crypt2[indi]) % len(charlist))
                indi += 1

            for i in crypt3:
                output += charlist[i]
            return(output)
