const figureEle = document.getElementsByTagName('figure');

//마우스 올려졌을 때
function knowSizefunc(event) {
  const HideBar = document.createElement('div');
  const myProfile = document.createElement('div');
  const myPosting = document.createElement('div');
  const plustButton = document.createElement('button');
  const figureElement = event.target;
  const eleWidth = event.toElement.offsetWidth;
  const eleHeight = event.toElement.offsetHeight;

  //appendChild하는 부분
  figureElement.appendChild(HideBar);
  HideBar.appendChild(myProfile);
  HideBar.appendChild(myPosting);
  HideBar.appendChild(plustButton);

  //클래스리스트 추가
  HideBar.classList.add('hideBar');
  myProfile.classList.add('myProfile');
  myPosting.classList.add('myPosting');
  plustButton.classList.add('plustButton');
  //스타일의 속성 바꾸는 부분
  HideBar.style.width = eleWidth + `px`;
  HideBar.style.height = eleHeight + `px`;
  myProfile.innerHTML = '마광팔';
  myPosting.innerText = '야옹';
  plustButton.innerHTML = '더보기';
}

function wait(sec) {
  let start = Date.now(),
    now = start;
  while (now - start < sec * 1000) {
    now = Date.now();
  }
}

//마우스 out됐을때
function removeElefunc(event) {
  const removeEle = document.querySelector('figure :nth-child(2)');
  wait(0.05);
  removeEle.remove();
}
//모든 imgs에 addEventListener해주기.
for (let i = 0; i < figureEle.length; i++) {
  figureEle[i].addEventListener('mouseenter', knowSizefunc);
  figureEle[i].addEventListener('mouseleave', removeElefunc);
}
