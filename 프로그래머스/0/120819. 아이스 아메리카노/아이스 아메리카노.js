function solution(money) {
    return Array.from({length:2},(_,i) => (i === 0) ? Math.floor(money / 5500) : money % 5500  );
}