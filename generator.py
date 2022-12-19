# kid math generator
import random

# output string questions
def generator(n, ops, d):
    n_times = 0
    output_strs = []
    outputs = []
    ops_list = ['+', '-', '*', '/']
    n_questions = 0

    # generate the nth question
    def generate_n_q():
        # initiate starter digit
        output_str = str(random.randrange(1, d))
        # generate number of k operands in the nth question
        k_ops = random.randrange(1, ops+1)
        ops_times = 0
        while ops_times < k_ops:
            output_str = generate_k_ops(output_str, d)
            ops_times += 1
        return output_str, output_str

    # generate the kth operands
    def generate_k_ops(output_str, d):
        num_to_append = random.randrange(0, d)
        ops_to_append = random.choice(ops_list)
        output_str += (str(ops_to_append) + str(num_to_append))
        return output_str
    

    while n_questions < n:
        output_str, output = generate_n_q()
        output_strs.append(output_str)
        outputs.append(output)
        n_questions += 1
    return outputs, output_strs

def main():
    outputs, output_strs = generator(2, 2, 10)
    print(outputs, output_strs)


if __name__ == "__main__":
    main()