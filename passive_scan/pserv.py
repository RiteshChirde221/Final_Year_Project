from whatweb import *
def serv_pas(domain):
    res=whatweb(domain)
    return str(res)

# print(serv_pas('prmceam.ac.in'))

# def append_newline_every_n_chars(input_str, n=50):
#     result_str = ''
#     for i in range(0, len(input_str), n):
#         result_str += input_str[i:i+n]
#         if i + n < len(input_str):
#             result_str += '\n'
#     return result_str

# # Example usage:
# input_str = "This is a long string. It will be appended every 50 characters."
# result = append_newline_every_n_chars(input_str)
# print(result)


# serv_pas('prmceam.ac.in')




