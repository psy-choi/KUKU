function handleCategoryChange(selectElement) {
  
  let selectedValue = selectElement.value;
  if (selectedValue) {
    window.location.href = '/pictures/' + selectedValue + '/' +'None';
  } else {
    window.location.href = '/pictures/';  // 선택하지 않은 경우 메인 페이지로 이동
  }
}