class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res = -1
        hashMap = {}
        for n in nums:
            # cal sum of digit of n
            temp = n
            digitSum = 0
            while temp:
                digitSum += temp % 10
                temp = temp // 10
            
            # add to hashMap key is digit sum and value is max of n and prev max
            if digitSum not in hashMap:
                hashMap[digitSum] = n
            else:
                res = max(hashMap[digitSum] + n , res)
                hashMap[digitSum] = max(n, hashMap[digitSum])
        return res
            
        
        
        # Initialize a dictionary to store the maximum number for each digit sum

        digit_sum_max_num = defaultdict(int)


        # Iterate through each number in the given list

        for num in nums:

            # Calculate the sum of digits for the current number

            digit_sum = 0

            temp_num = num

            while temp_num:

                digit_sum += temp_num % 10

                temp_num //= 10


            # If the sum of digits has been seen before,

            # check if the current number contributes to a larger max sum

            if digit_sum in digit_sum_max_num:

                max_sum = max(max_sum, digit_sum_max_num[digit_sum] + num)

          

            # Update the maximum number for the current digit sum

            digit_sum_max_num[digit_sum] = max(digit_sum_max_num[digit_sum], num)

      

        # Return the maximum sum of two numbers having the same sum of digits

        return max_sum
                