(function () {
  'use strict'

  document.querySelector('#navbarSideCollapse').addEventListener('click', function () {
    document.querySelector('.offcanvas-collapse').classList.toggle('open')
  })
})()

let startDate = document.getElementById('startDate')

startDate.addEventListener('change',(e)=>{
  let startDateVal = e.target.value
  document.getElementById('startDateSelected').innerText = startDateVal
})

var myModal = new bootstrap.Modal(document.getElementById('ventana-modal'), options)