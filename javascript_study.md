# javascript_study

## 문법

### 배열 관련 !

- 배열 만들기 (Array.from)

  - Array.from({length:n},(\_, i) => num_list[i]);
  - 배열을 생성한다 -> 길이가 n개, 요소는 뒤의 num_list[i]를 반복하여 하나씩 넣음

- 배열 내부 요소 건들기 1 (map)

  - index 사용
  - ```javascript
    arr.map((num,index) => {
      if(num >= 50 && num % 2 === 0){
        arr[index] = num / 2;
      }
      else if(num < 50 && num % 2 === 1){
        arr[index] = num\*2;
      }
    });
    ```
  - map 으로 arr 배열안의 값들을 index 순서대로 하나하나 확인
  - num은 arr의 요소라고 보면 된다
  - 이 코드 같은 경우에는 arr의 배열 안의 num 값을 나눠서 다시 arr에 넣는 방식

- 배열 내부 요소 건들기 2 (reduce)
  - ```javascript
    if (num_list.length > 10) {
      return num_list.reduce((sum, num) => sum + num, 0);
    } else {
      return num_list.reduce((product, num) => product \* num, 1);
    }
    ```
  - num은 배열 내부의 요소
  - num_list 배열의 값을 더해서 sum과 product를 배출하는 방식
  - 문장 끝 부분에 ,0); 과 ,1)은 각각 sum과 product의 초기값
    
- map과 reduce 차이

  - map 메서드

    - 목적: map은 배열의 각 요소에 대해 주어진 함수를 호출하고, 그 결과를 모아 새로운 배열을 생성

    - 동작 방식: map은 원본 배열의 각 요소를 순회하면서 함수를 적용하여, 그 결과를 모은 새 배열을 반환 / 원본 배열은 변경되지 않으며, 항상 같은 길이의 새로운 배열이 반환

  - reduce 메서드

    - 목적: reduce는 배열의 각 요소를 순회하면서 주어진 함수에 따라 하나의 값으로 줄입니다. 이 값은 숫자, 문자열, 객체 등 무엇이든 될 수 있음

    - 동작 방식: reduce는 배열의 각 요소를 순차적으로 처리하면서, 누적값(accumulator)과 현재 요소를 함수로 전달하여 그 결과를 누적 가능 / 초기값을 설정할 수 있으며, 이 초기값을 시작으로 배열의 모든 요소를 처리한 후 하나의 최종 값을 반환

- 배열 해당 숫자부터 나오게 끔 하기 (slice)

  -  ```javascript
     function solution(num_list, n) {
       return num_list.slice(n);
     }
     ```
  - 얘는 배열의 크기가 5이고 n이 2일 경우 배열 [0,1,2,3,4] 중에 [3,4,5] 만 내보냄
  - 쉽게 말해서 n 값부터 인덱스 값이 나오면 된다

- 배열 인덱스 찾기 (findIndex)
  - ```javascript
    function solution(num_list) {
      return num_list.findIndex(num => num < 0);
    }
    ```
  - 가장 먼저 조건에 맞는 index 반환
  - 아니면 -1 반환

- filter
  - 배열의 각 요소를 조건에 맞게 필터링하여 새로운 배열을 반환
  - let 새로운배열 = 기존배열.filter(요소 => 조건);
  - 예시
     ```javascript
      let 숫자배열 = [1, 2, 3, 4, 5, 6];
      let 짝수들 = 숫자배열.filter(숫자 => 숫자 % 2 === 0);
      console.log(짝수들); // [2, 4, 6]
     ```
- 배열 정렬 (sort)
  - 오름차순
  - ```javascript
     const arr = [22, 11, 2, 9, 1, 5];
     arr.sort(function (a, b) {
       return a - b;
     });
     console.log(arr);
     ```
  - 내림차순
  - ```javascript
     const arr = [22, 11, 2, 9, 1, 5];
     arr.sort(function (a, b) {
       return b - a;
     });
     console.log(arr);
    ```
### 소수점

- Math.ceil(숫자) : 소수점 올림, 정수 반환
- Math.floor(숫자) : 소수점 버림, 정수 반환
- Math.round(숫자) : 소수점 반올림, 정수 반환
- 소수점 길이만큼 반올림 숫자 : 99.9876543
  - 숫자.toFixed(0) : // 100 출력
  - 숫자.toFixed(5) : // 99.98765 출력
