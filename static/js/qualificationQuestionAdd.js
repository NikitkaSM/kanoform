let qualificationQuestionForm = document.querySelectorAll(
	'.qualification-question-form'
)
let formContainer = document
	.getElementById('form-container')
	.getElementsByTagName('div')[0]
let addButton = document.getElementById('add-qualification-question-button')
let totalForms = document.getElementById('id_form-TOTAL_FORMS')

let formNum = qualificationQuestionForm.length - 1
addButton.addEventListener('click', qualificationQuestionFormAdd)

function qualificationQuestionFormAdd(event) {
	event.preventDefault()
	let newForm = qualificationQuestionForm[0].cloneNode(true)
	let formRegex = RegExp(`form-(\\d){1}-`, 'g')

	formNum++
	newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`)
	formContainer.insertBefore(newForm, addButton)

	totalForms.setAttribute('value', `${formNum + 1}`)
	console.log('Text')
}
