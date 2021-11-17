// navdrop
document.getElementById('me').addEventListener('click', function() {
  document.getElementById('bod').style.transform  = 'scale(1)';
  document.querySelector('.drop').style.display = 'flex';
})
document.getElementById('bod').addEventListener('click', function() {
  document.getElementById('bod').style.transform ='scale(0)';
  document.querySelector('.drop').style.display = 'none';
})
// POSTMODAL
document.getElementById('dabade').addEventListener('click', function() {
  document.getElementById('bod2').style.transform  = 'scale(1)';
  document.querySelector('.modal').style.display = 'block';
})
document.getElementById('bod2').addEventListener('click', function() {
  document.getElementById('bod2').style.transform ='scale(0)';
  document.querySelector('.modal').style.display = 'none';
})
// followmodal
document.getElementById('f').addEventListener('click', function(){
  document.getElementById('bod4').style.transform  = 'scale(1)';
  document.getElementById('followerlistdiv').style.display = 'flex';
})
document.getElementById('bod4').addEventListener('click', function(){
  document.getElementById('bod4').style.transform  = 'scale(0)';
  document.getElementById('followerlistdiv').style.display = 'none';
})
// following
document.getElementById('fing').addEventListener('click', function(){
  document.getElementById('bod5').style.transform  = 'scale(1)';
  document.getElementById('followinglistdiv').style.display = 'flex';
})
document.getElementById('bod5').addEventListener('click', function(){
  document.getElementById('bod5').style.transform  = 'scale(0)';
  document.getElementById('followinglistdiv').style.display = 'none';
})
