import numpy as np
import matplotlib.pyplot as plt

# Manchester Encoding
def manchester_encoding(bits):
    encoded_bits = np.empty(len(bits) * 2, dtype=int) 
    index = 0

    for bit in bits:
        if bit == '0':
            encoded_bits[index:index+2] = [1, -1]
        elif bit == '1':
            encoded_bits[index:index+2] = [-1, 1]
        index += 2

    return encoded_bits

# Manchester Decoding
def manchester_decoding(encoded_data):
    decoded_data = []

    for i in range(0, len(encoded_data), 2):
        if np.array_equal(encoded_data[i:i+2], [1, -1]):
            decoded_data.append('0')
        elif np.array_equal(encoded_data[i:i+2], [-1, 1]):
            decoded_data.append('1')

    return ''.join(decoded_data)

# Finding Longest Palindrome 
def longestPalindrome(s):
    longest_palindrom = ''
    dp = np.zeros((len(s), len(s)), dtype=bool)  
    for i in range(len(s)):
        dp[i][i] = True
        longest_palindrom = s[i]
    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s)):  
            if s[i] == s[j]:
                if j - i == 1 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if len(longest_palindrom) < len(s[i:j + 1]):
                        longest_palindrom = s[i:j + 1]                
    return longest_palindrom

# Plotting Manchester Encoded Data
def plot(manchester_data):
    plt.step(range(len(manchester_data)), manchester_data, where='post', color='grey', linewidth=4)
    plt.title('Manchester Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0, color='red')
    plt.ylim(-1.5, 1.5)
    for i in range(len(manchester_data)):
        plt.axvline(i, color='black', linestyle='--')
    plt.show()

if __name__ == '__main__':
  
    try:
        size = int(input("Enter the number of bits you want to input: "))
        if size <= 0:
            print("The size must be a positive integer.")
            exit()
    except ValueError:
        print("Invalid input. Please enter an integer value.")
        exit()

    binary_data = []
    print(f"Enter the binary data (0 or 1) for {size} bits:")
    for i in range(size):
        while True:
            bit = input(f"Bit {i+1}: ")
            if bit in ['0', '1']:
                binary_data.append(bit)
                break
            else:
                print("Invalid input. Only binary values (0 or 1) are allowed.")

    # Encoding the data using Manchester
    manchester_data = manchester_encoding(binary_data)
    print("Binary Data:", binary_data)
    print("Manchester Encoded Data:", manchester_data.tolist())  
    
    # Finding the longest palindrome
    palindrome = longestPalindrome(''.join(binary_data))
    print("Longest palindrome in dataStream:", palindrome)

    # Plotting the Manchester encoded data
    plot(manchester_data)

    decode_choice = input("Do you want to decode the Manchester encoded signal? (yes/no): ").strip().lower()
    if decode_choice == "yes":
        decoded_data = manchester_decoding(manchester_data)
        print("Decoded Data:", decoded_data)
    else:
        print("Decoding skipped.")
