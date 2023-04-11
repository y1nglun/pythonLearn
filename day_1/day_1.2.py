def reverseWords(input):
    """将输入已空格分隔为列表"""
    inputWords = input.split(" ")
    """inputWords[-1::-1]有三个参数:
       第一个参数为-1，表示最后一个元素
       第二个元素为空，表示移动到链表末尾
       第三个元素为步长，-1表示逆向"""
    inputWords = inputWords[-1::-1]
    output = ' '.join(inputWords)
    return output


if __name__ == '__main__':
    input = "I like python"
    rw = reverseWords(input)
    print(rw)
