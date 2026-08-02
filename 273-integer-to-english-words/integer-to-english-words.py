class Solution(object):
    def numberToWords(self, n):
        if n == 0: return "Zero"
        ones_map = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }

        tens_map = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }

        postfix = ["", "Thousand ", "Million ", "Billion "]
        def triplets(n):
            output = []
            hundreds = n // 100
            if hundreds:
                output.append(ones_map[hundreds] +  " Hundred")
            last_two = n % 100
            if last_two:
                if last_two < 20:
                    output.append(ones_map[last_two])
                else:
                    tens = last_two // 10
                    ones = last_two % 10
                    if tens:
                        output.append(tens_map[tens * 10])
                    if ones:
                        output.append(ones_map[ones])
            return " ".join(output)

        res = []
        i = 0 #postfix index
        while n > 0:
            triplet = n % 1000
            if triplet:
                res.append(triplets(triplet) + " " + postfix[i])
            i += 1
            n //= 1000
        res.reverse()
        final = "".join(res)
        return final[:-1]
