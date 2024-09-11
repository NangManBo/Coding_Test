function solution(array, height) {
    return array.filter(num => num > height).length;
}