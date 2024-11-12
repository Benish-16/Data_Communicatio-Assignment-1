import matplotlib.pyplot as plt
import numpy as np

# Differential Manchester Encoding
def differential_manchester_encoding(bits):
    encoded_bits = np.empty(len(bits) * 2, dtype=int)  
    current_state = 1  # Initial state
    index = 0

    for bit in bits:
        if bit == '0':
            encoded_bits[index:index+2] = [current_state, -current_state]
        elif bit == '1':
            encoded_bits[index:index+2] = [-current_state, current_state]
            current_state = -current_state  
        index += 2

    return encoded_bits


def differential_manchester_decoding(encoded_data):
    decoded_bits = []
    current_state = 1  
    for i in range(0, len(encoded_data), 2):
        if encoded_data[i] == current_state:
            decoded_bits.append('0')
        else:
            decoded_bits.append('1')
            current_state = -current_state  

    return ''.join(decoded_bits)


def longestPalindrome(s):
    longest_palindrom = ''
    dp = np.zeros((len(s), len(s)), dtype=bool) 
    for i in range(len(s)):
        dp[i][i] = True
        longest_palindrom = s[i]
    for i in range(len(s)-1, -1, -1):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                if j-i == 1 or dp[i+1][j-1]:
                    dp[i][j] = True
                    if len(longest_palindrom) < len(s[i:j+1]):
                        longest_palindrom = s[i:j+1]
    return longest_palindrom

# Plotting the Differential Manchester Encoded Data
def plot(differential_manchester_data):
    plt.step(range(len(differential_manchester_data)), differential_manchester_data, where='post', color='grey', linewidth=4)
    plt.title('Differential Manchester Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0, color='red')
    plt.ylim(-1.5, 1.5)
    for i in range(len(differential_manchester_data)):
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
    
    # Encoding the data using Differential Manchester Encoding
    differential_manchester_data = differential_manchester_encoding(binary_data)
    print("Binary Data:", binary_data)
    print("Differential Manchester Encoded Data:", differential_manchester_data.tolist())  
    
    # Finding the longest palindrome 
    palindrome = longestPalindrome(''.join(binary_data))
    print("Longest palindrome in dataStream:", palindrome)

    # Plotting the Differential Manchester encoded data
    plot(differential_manchester_data)

    decode_choice = input("Do you want to decode the Differential Manchester encoded signal? (yes/no): ").strip().lower()
    if decode_choice == "yes":
        decoded_data = differential_manchester_decoding(differential_manchester_data)
        print("Decoded Data:", decoded_data)
    else:
        print("Decoding skipped.")
