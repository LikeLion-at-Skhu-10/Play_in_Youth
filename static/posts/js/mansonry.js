const figureEle = document.getElementsByTagName('figure');

//마우스 올려졌을 때
function knowSizefunc(event) {
  const HideBar = document.createElement('div');
  const myProfile = document.createElement('div');
  const myPosting = document.createElement('div');
  const plusButton = document.createElement('button');
  const figureElement = event.target;
  const eleWidth = event.toElement.offsetWidth;
  const eleHeight = event.toElement.offsetHeight;
  const myModal = document.querySelector('.myModal');
  const closeButton = document.querySelector('.myModal :first-child');
  const screenY = window.scrollY;

  //appendChild하는 부분
  figureElement.appendChild(HideBar);
  HideBar.appendChild(myProfile);
  HideBar.appendChild(myPosting);
  HideBar.appendChild(plusButton);

  //클래스리스트 추가
  HideBar.classList.add('hideBar');
  myProfile.classList.add('myProfile');
  myPosting.classList.add('myPosting');
  plusButton.classList.add('plusButton');

  //스타일의 속성 바꾸는 부분
  HideBar.style.width = pxtoRem(eleWidth) + `rem`;
  HideBar.style.height = pxtoRem(eleHeight) + `rem`;
  const myProfileWidth = myProfile.style.width;
  myProfile.style.height = myProfileWidth;
  myProfile.innerHTML = '마광팔';
  myPosting.innerText = '야옹';
  plusButton.innerHTML = '더보기';
  myModal.style.top = screenY + `px`;

  //eventListener하는 부분
  plusButton.addEventListener('click', showModal);
  closeButton.addEventListener('click', closeModal);
}

//modal 조작하는 함수 2개
function showModal(event) {
  const body = document.getElementsByTagName('body')[0];
  document.querySelector('.myModal').style.display = 'flex';
  body.classList.add('scrollLock');
}
function closeModal() {
  const body = document.getElementsByTagName('body')[0];
  document.querySelector('.myModal').style.display = 'none';
  body.classList.remove('scrollLock');
}

//px에서 rem으로 변환하는 함수
function pxtoRem(mypx) {
  num = mypx * 0.0625;
  return num;
}

//지연 함수
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
//안에 있는 글 내용 바꾸기
function change(post,comment,author,date){
  document.body.querySelector('.myModalContentTextText').textContent = post;
  document.body.querySelector('.commentAraText').textContent = comment;
  document.body.querySelector('.UserName').textContent = author;
  document.body.querySelector('.PostingDate').textContent = date;

}
//이미지 클릭했을 때 모달 띄워줄꺼임. 쿠쿠루삥뽕
function findUrl(event){
  const selectedImgUrl = event.path[2].children[0].src;
  const ModalContent = document.body.querySelector(".myModalContent img");
  document.body.querySelector(".myModalContent img").src = `${selectedImgUrl}`;
}
//모든 imgs에 addEventListener해주기.
for (let i = 0; i < figureEle.length; i++) {
  figureEle[i].addEventListener('mouseenter', knowSizefunc);
  figureEle[i].addEventListener('mouseleave', removeElefunc);
  figureEle[i].addEventListener('click',findUrl);
}


