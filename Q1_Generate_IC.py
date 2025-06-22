import random
state_nums=[1, 21, 22, 23, 24, 2, 25, 26, 27, 3, 28, 29, 4, 30, 5, 31, 59, 6, 32, 33, 7, 34, 35, 8, 36, 37, 38, 39, 9, 40, 10, 41, 42, 43, 44, 11, 45, 46, 12, 47, 48, 49, 13, 50, 51, 52, 53, 14, 54, 55, 56, 57, 15, 58, 16]
number=""
TABLE_SIZE1=1009
TABLE_SIZE2=2003


def generate_random_numbers(filename, count,number,state_nums):
    with open("IC_Generated", 'w') as f:
        for _ in range(count):
            number += f"{random.randint(0, 99):02d}"        #Year
            number += f"{random.randint(1,12):02d}"         #Months
            number += f"{random.randint(1, 31):02d}"        #days
            number += f"{random.choice(state_nums):02d}"    #state numbers
            number += f"{random.randint(0,9999):04d}"       #random 4 digit number
            f.write(f"{number}\n")
            number=""

def hash_ic_polynomial(ic_number,tableSize, base=37):
    hash_val = 0
    for digit in ic_number:
        hash_val = (hash_val * base + int(digit)) % tableSize
    return hash_val

def hash_division(ic_number, table_size):
    part1 = int(ic_number[0:4])
    part2 = int(ic_number[4:8])
    part3 = int(ic_number[8:12])
    folded = part1 + part2 + part3
    return folded % table_size  # Returning 0 is fine for chaining


def separate_chaining(hash_function, ic_numbers, table_size):
    hash_table = [None] * table_size
    collisions = 0

    for ic_number in ic_numbers:
        index = hash_function(ic_number, table_size)
        if hash_table[index] is None:
            hash_table[index] = [ic_number]
        else:
            hash_table[index].append(ic_number)
            if len(hash_table[index]) == 2:
                collisions += 1

    return hash_table, collisions


def print_hash_table_and_max_chain(hash_table):
    max_chain_length = 0

    for i, chain in enumerate(hash_table):
        if chain is not None:
            print(f"Index {i}: {chain} )")
            if len(chain) > max_chain_length:
                max_chain_length = len(chain)

    print("\nMaximum Chain Length:", max_chain_length)

def generate_IC():
    generate_random_numbers("IC_Generated.txt", 1000, "", state_nums)  # Generates 1000 numbers
    with open("IC_Generated", 'r') as f:
        lines = f.readlines()
        ic_numbers = [line.strip() for line in lines]
    return ic_numbers


def main():
    hash_table1 = [None] * TABLE_SIZE1
    hash_table2 = [None] * TABLE_SIZE2
    hash1=[]
    hash2=[]


    collisions1=0
    collisions2=0
    total_collisions1=0
    total_collisions2=0

    for i in range(1,11):
        ic_numbers = generate_IC()
        hash_table1, collisions1 = separate_chaining(hash_division, ic_numbers, TABLE_SIZE1)
        total_collisions1+=collisions1
        print("Round",i," Hash 1 = ", collisions1)


    for i in range(1,11):
        ic_numbers = generate_IC()
        hash_table2, collisions2 = separate_chaining(hash_division, ic_numbers, TABLE_SIZE2)
        total_collisions2 += collisions2
        print("Round ", i, "Hash2 = ", collisions2)

    print_hash_table_and_max_chain(hash_table1)

    print_hash_table_and_max_chain(hash_table2)

    print("Average Collision Count for Hash table 1:", total_collisions1/10)
    print("Average Collision Count for Hash table 2:", total_collisions2/10)



if __name__=="__main__":
    main()
