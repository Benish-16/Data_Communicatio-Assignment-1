import numpy as np
import matplotlib.pyplot as plt

# NRZ-I Encoding
def nrz_i_encoding(data):
    encoded_data = np.empty(len(data), dtype=int)
    current_level = 1 

    for i, bit in enumerate(data):
        if bit == '1':
            current_level = -current_level  
        encoded_data[i] = current_level
    
    return encoded_data

# NRZ-I Decoding
def nrz_i_decoding(encoded_data):
    decoded_data = []
    current_level = 1 

    for level in encoded_data:
        if level == current_level:
            decoded_data.append('0')
        else:
            decoded_data.append('1')
            current_level = -current_level 
    
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
                if j - i == 1 or dp[i + 1][j - 1] is True:
                    dp[i][j] = True
                    if len(longest_palindrom) < len(s[i:j + 1]):
                        longest_palindrom = s[i:j + 1]                
    return longest_palindrom

# Plotting NRZ-I Encoded Data
def plot(nrz_i_data):
    plt.step(range(len(nrz_i_data)), nrz_i_data, where='post', color='grey', linewidth=4)
    plt.title('NRZ-I Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0, color='red')
    plt.ylim(-1.5, 1.5)  
    for i in range(len(nrz_i_data)):
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

    # Encoding the data using NRZ-I
    nrz_i_data = nrz_i_encoding(binary_data)
    print("Binary Data:", binary_data)
    print("NRZ-I Encoded Data:", nrz_i_data.tolist())  
    
    # Finding the longest palindrome
    palindrome = longestPalindrome(''.join(binary_data))
    print("Longest palindrome in dataStream:", palindrome)

    # Plotting the NRZ-I encoded data
    plot(nrz_i_data)

    decode_choice = input("Do you want to decode the NRZ-I encoded signal? (yes/no): ").strip().lower()
    if decode_choice == "yes":
        decoded_data = nrz_i_decoding(nrz_i_data)
        print("Decoded Data:", decoded_data)
    else:
        print("Decoding skipped.")
