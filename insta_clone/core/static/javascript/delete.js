// delete
document.getElementById('fa').addEventListener('click', function(){
  document.getElementById('op').focus();
})
document.getElementById('dele').addEventListener('click', function() {
  document.getElementById('bod3').style.transform  = 'scale(1)';
  document.querySelector('.deletemodal').style.display = 'block';
})
document.getElementById('bod3').addEventListener('click', function() {
  document.getElementById('bod3').style.transform ='scale(0)';
  document.querySelector('.deletemodal').style.display = 'none';
})
