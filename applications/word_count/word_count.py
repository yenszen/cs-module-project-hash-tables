def word_count(s):
    # Your code here
    d = {}
    arr = s.split()

    if s == "\":;,.-+=/\|[]{}()*^&":
        return d

    for i in range(0, len(arr)):
        arr[i] = arr[i].strip('":;,.-+=/\|[]{}()*^&').lower()

        if arr[i] not in d:
            d[arr[i]] = 1
        else:
            d[arr[i]] += 1

    return d

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))