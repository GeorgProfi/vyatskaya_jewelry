function aboba() {
    const delivery = {
    ''
    };
    var e = document.getElementById("inputDevCopm");
    var value = e.value;
    var text = e.options[e.selectedIndex].text;
    var sum = document.getElementById("summa_order");
    //sum.innerHTML = text
    alert(text)
}
document.querySelector("#submit").onclick = function(){
  alert("Вы нажали на кнопку");
}