function solution(numbers) {
    return numbers.map((v)=>v*2)
}

//map메소드는 단순 배열 생성 뿐만 아니라 데이터 추출도 가능하다.
//name:..., age:... 를 가진 객체에 대해서 obj.map((v)=>obj['name'], obj['age'])를 수행하면 객체에서 name과 age에 해당하는 밸류들을 다 뽑아줌.
