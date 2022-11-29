let date = new Date();

const renderCalendar = () => {
  const viewYear = date.getFullYear();
  const viewMonth = date.getMonth();

  //지난 달 마지막 Date, 이번 달 마지막 Date
  //새로운 Date객체를 생성할 때, 파라미터 date에 해당하는 부분에 0을 전달하게 되면, 지난달의 마지막 날의 date 객체가 생성
  //같은 원리로 파라미터 다음달의 0번째 날을 뽑으면, 이번달의 마지막 날 date객체가 생성
  const prevLast = new Date(viewYear, viewMonth, 0);
  const thisLast = new Date(viewYear, viewMonth + 1, 0);

  const PLDate = prevLast.getDate();
  const PLDay = prevLast.getDay();

  const TLDate = thisLast.getDate();
  const TLDay = thisLast.getDay();

  //전체 달력에 필요한 날짜 만들어주기
  //date 기본 배열들
  const prevDates = [];
  const thisDates = [...Array(TLDate + 1).keys()].slice(1);
  const nexDates = [];

  //prevDates 계산
  if (PLDay !== 6) {
    for (let i = 0; i < PLDay + 1; i++) {
      prevDates.unshift(PLDate - i);
    }
  }

  //nextDates 계산
  for (let i = 1; i < 7 - TLDay; i++) {
    nexDates.push(i);
  }
  //dates 합치기
  const dates = prevDates.concat(thisDates, nexDates);
  //dates 정리
  dates.forEach((date, i) => {
    dates[i] = `<div class="date">${date}</div>`;
  });
  //dates 그리기
  document.querySelector('.dates').innerHTML = dates.join('');
  //현재 년도와 월,일 출력
  document.querySelector('.year-month').textContent = `${viewYear}년 ${viewMonth + 1}월`;
};
renderCalendar();
//이번달,다음달을 보여줄 nav 구현
const prevMonth = () => {
  date.setMonth(date.getMonth() - 1);
  renderCalendar();
};
const nextMonth = () => {
  date.setMonth(date.getMonth() + 1);
  renderCalendar();
};
const goToday = () => {
  date = new Date();
  renderCalendar();
};

//Writing and Comment
const dateWriting = document.createElement('div');
const dateComment = document.createElement('div');
function dateWrite() {
  const Dates = document.body.querySelectorAll('.date');

  Dates[1].appendChild(dateComment);
  Dates[1].appendChild(dateWriting);

  dateWriting.classList.add('myPageWriting');
  dateComment.classList.add('myPageComment');

  dateWriting.innerHTML = '1';
  dateComment.innerHTML = '2';
  //나중에는 해당 dateWriting을 누르면 해당 게시물만 함수 실행이 되도록 하기
}
dateWrite();

function myWritingModal() {
  console.log('Hello');
}
function myCommentModal() {}
dateWriting.addEventListener('click', myWritingModal);
dateComment.addEventListener('click', myCommentModal);
