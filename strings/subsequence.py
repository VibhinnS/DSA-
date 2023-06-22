def subsequence(string, final_str):
    if string == "":
        return [final_str]

    results = []
    results.extend(subsequence(string[1:], final_str + string[0]))
    results.extend(subsequence(string[1:], final_str))
    if '' in results:
        results.remove('')
    return results

# print(subsequence("abc", ""))


def subsequence(arr, final_arr):
    if arr == []:
        return [final_arr]

    results = []
    results.append(subsequence(arr[1:], final_arr + arr[0]))
    results.append(subsequence(arr[1:], final_arr))
    if [] in results:
        results.remove([])
    return results

print(subsequence([1,2,3], []))
