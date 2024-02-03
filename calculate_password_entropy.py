import math

def calculate_password_entropy(upwd):
   # Calculate the frequency of each character in the password
   char_counts = {}
   for char in upwd:
       char_counts[char] = char_counts.get(char, 0) + 1

   # Calculate the total number of characters in the password
   total_chars = len(upwd)

   # Calculate the entropy
   entropy = 0
   for count in char_counts.values():
       probability = count / total_chars
       entropy -= probability * math.log2(probability)

   return entropy


# Example usage
password = input("Enter your password: ")
entropy = calculate_password_entropy(upwd)
print(f"Password: {password}, Entropy: {entropy:.2f}")

