

# 1
def count_nucleotides(filename):
    data = open(filename).readlines()[0]
    nucleotides = ["A", "C", "G", "T"]
    return [data.count(x) for x in nucleotides]


print(count_nucleotides("rosalind_dna.txt"))

# 2
def translate_to_rna(filename):
    data = open(filename).readlines()[0]
    return data.replace("T", "U")


print(translate_to_rna("rosalind_rna.txt"))


# 3
def complement_dna(filename):
    data = open(filename).readlines()[0][:-1]
    print(type(data))
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return "".join(reversed([complement.get(base) for base in data]))

print(complement_dna("rosalind_revc.txt"))

# 4
def fibbonacci(filename):
    data = open(filename).readlines()[0]
    m, n = data.split(" ")
    m = int(m)
    n = int(n)
    seq = [1, 1]
    for i in range(2, m):
        seq.append(seq[-2]*n + seq[-1])
    return seq[-1]

print(fibbonacci("rosalind_fib.txt"))

# 5

def gc_content(filename):
    data = open(filename).readlines()
    data2 = dict()
    key = ""
    for i in data:
        if i[0] == ">":
            key = i[:-1]
            data2[key] = ""
        else:
            data2[key] += i[:-1]
    print(data2.keys())

    highest = ["a", 0]

    for key, value in data2.items():
        print(key)
        res = (value.count("C") + value.count("G")) * 100/ len(value)
        print(res)
        highest = [key, res] if res > highest[1] else highest
    return highest

print(gc_content("rosalind_gc.txt"))


# 6
def hamming_distance(filename):
    data = open(filename).read().splitlines()
    hamm_len = 0
    for i,j in zip(data[0], data[1]):
        if j != i: hamm_len += 1

    return hamm_len

print(hamming_distance("rosalind_hamm.txt"))

# 7

# 8

# 9

# 10
