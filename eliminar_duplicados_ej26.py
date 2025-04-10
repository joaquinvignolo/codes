def removeDuplicates(nums):
    if not nums:
        print("La lista está vacía.")
        return 0

    k = 1  #se empieza desde el segundo índice porque el primer número ya estará bien posicionado
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k

#pedimos al usuario que ingrese la lista
entrada = input("Ingresá una lista de números separados por coma: ")
nums = list(map(int, entrada.split(','))) #convierte los strings en int separados por coma
nums.sort() #ordena la lista de menor a mayor

k = removeDuplicates(nums)
print(f"\nCantidad de elementos únicos: {k}")
print(f"Nueva lista: {nums[:k]}")