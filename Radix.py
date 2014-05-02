class KVEntry:
    _key = 0;
    _value = 0;

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        if value >= 0:
            _key = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        _value = value



def Sort(array):
    return RadixSortAux(array, 1)

def RadixSortAux(array, digit):
    Empty = True
    digits = [KVEntry()]*len(array)
    SortedArray = [int]*len(array)
    for i in range(0, len(array)):
        digits[i] = KVEntry()
        digits[i].key = i
        print(str((array[i]/digit) % 10) + "LOOK!!!")
        digits[i].value = (array[i]/digit) % 10
        if array[i] / digit != 0:
            Empty = False
    if Empty:
        return array

    SortedDigits = CountingSort(digits)
    for i in range(0, len(SortedArray)):
        SortedArray[i] = array[SortedDigits[i].key]
    return RadixSortAux(SortedArray, digit * 10)

def CountingSort(ArrayA):
    ArrayB = [int]*(MaxValue(ArrayA) + 1)
    ArrayC = [KVEntry()]*len(ArrayA)

    for i in range(0, len(ArrayB)):
        ArrayB[i] = 0

    for i in range(0, len(ArrayA)):
        ArrayB[ArrayA[i].value] += 1

    for i in range(1, len(ArrayB)):
        ArrayB[i] += ArrayB[i - 1]

    for i in range(len(ArrayA)-1, -1, -1):
        value = ArrayA[i].value
        index = ArrayB[value]
        ArrayB[value] -= 1
        ArrayC[index-1] = KVEntry()
        ArrayC[index-1].key = i
        ArrayC[index-1].value = value

    return ArrayC

def MaxValue(arr):
    Max = arr[0].value
    for i in range(1, len(arr)):
        if arr[i].value > Max:
            Max = arr[i].value()
    return Max