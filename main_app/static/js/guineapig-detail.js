const dateInput = document.getElementById('id_date')

const picker = MCDatepicker.create({
  el: '#id_date',
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date(),
  theme: {
    theme_color: '#6CE898'
  }
})

dateInput.addEventListener("click", (evt) => {
  picker.open()
})