/* 
var hw = document.getElementById('hw');
hw.addEventListener('click', function(){
    localStorage.counter = Number(localStorage + 1);
    alert('Hello World');
})
*/



function clickCounter() {
    if(typeof(Storage) !== "undefined") {
        if (localStorage.counter) {
            localStorage.counter = Number(localStorage.counter) + 1;
            alert('if문 실행완료')
        }

        else {
            localStorage.counter = 1;
            alert('else 문 실행완료')
        }

        document.getElementById("result").innerHTML = localStorage.counter + "번 클릭했습니다."
    }

    else {
        document.getElementById("result").innerHTML = "웹 스토리지를 지원하지 않습니다."
    }

}