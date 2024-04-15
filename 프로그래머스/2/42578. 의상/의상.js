function solution(clothes) {
    const hashmap = clothes.reduce((acc, [name, type]) => {
        acc.set(type, (acc.get(type) || 0) + 1)
        return acc
    }, new Map())

    let result = 1
    hashmap.forEach((value) => {
        result *= value + 1
    })
    
    return result - 1;
}