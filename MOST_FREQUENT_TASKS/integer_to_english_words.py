class Solution:
    def convert_digit(self, num: int) -> str:
        digit_mapping = {
            0: '',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }
        return digit_mapping[num]

    def convert_irregular_tens(self, num: int) -> str:
        irregular_tens_mapping = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        return irregular_tens_mapping[num]

    def convert_tens(self, num: int) -> str:
        ten_mapping = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }
        return ten_mapping[num]

    #   converts triplet number (1-3 digits) to string representation
    def process_triplet(self, num_str: str) -> str:
        result = ''

        #   process hundreds
        if len(num_str) == 3:
            hundreds = int(float(num_str[0]))
            hundreds_str = self.convert_digit(hundreds)
            if len(hundreds_str) > 0:
                result += hundreds_str + ' Hundred'

            tens = int(float(num_str[1:]))
        else:
            tens = int(float(num_str))

        #   process tens
        if 10 <= tens <= 19:
            tens_str = self.convert_irregular_tens(tens)
        elif tens > 19:
            tens_str = f'{self.convert_tens(tens // 10)}'
            digits = self.convert_digit(tens % 10)
            if len(digits) > 0:
                tens_str += f' {digits}'
        else:
            tens_str = self.convert_digit(tens)

        if len(tens_str) > 0:
            if len(result) > 0:
                result += ' '

            result += tens_str

        return result

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        num_str = str(num)
        triplets = []
        converted_triplets = []
        i = len(num_str) - 1

        #   create array of triplets (str of three digits)
        while i >= 0:
            counter = 0
            triplet = ''
            while i >= 0 and counter < 3:
                triplet = num_str[i] + triplet
                i -= 1
                counter += 1

            triplets.insert(0, triplet)

        triplets_mapping = {
            0: '',
            1: ' Thousand',
            2: ' Million',
            3: ' Billion'
        }

        #   processing all triplets, iterating from back
        i = len(triplets) - 1
        mapping_position = 0
        while i >= 0 and mapping_position < len(triplets_mapping):
            converted_triplet = self.process_triplet(triplets[i])

            if len(converted_triplet) > 0:
                converted_triplet = converted_triplet + triplets_mapping[mapping_position]
                converted_triplets.insert(0, converted_triplet)

            i -= 1
            mapping_position += 1

        return ' '.join(converted_triplets).strip()


solution = Solution()
num = 1000010
print(solution.numberToWords(num))
