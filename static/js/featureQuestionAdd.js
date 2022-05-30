let featureQuestionCounter = 0
const featureQuestionButton = document.getElementById('featureQuestionButton')
const featureQuestionsContainer = document.getElementById(
	'featureQuestionsContainer'
)

const deleteFeatureQuestion = event => {
	let button = event.target
	let li = button.parentNode
	li.remove()
}

const addFeatureQuestion = event => {
	event.preventDefault();

	if (featureQuestionCounter === 19) {
		alert('Максимальное кол-во вопросов')
	} else if (featureQuestionCounter < 19) {
		featureQuestionCounter++

		const li = document.createElement('li')
		const deleteButton = document.createElement('button')
		const input = document.createElement('input')

		li.setAttribute('id', `feature-${featureQuestionCounter}`)

		featureQuestionsContainer.append(li)

		deleteButton.addEventListener('click', deleteFeatureQuestion)

		const featureQuestionContainer = document.getElementById(
			`feature-${featureQuestionCounter}`
		)

		featureQuestionContainer.append(input)
		featureQuestionContainer.append(deleteButton)

		deleteButton.setAttribute('type', 'button')
		deleteButton.setAttribute('class', 'rounded btn delete-button')
		deleteButton.innerText = 'delete'

		input.setAttribute('type', 'text')
		input.setAttribute(
			'class',
			'container form rounded question-input feature-question'
		)
		input.setAttribute('id', `featureInput${featureQuestionCounter}`)
		input.setAttribute('placeholder', 'Введите вопрос')
	}
}

featureQuestionButton.addEventListener('click', addFeatureQuestion)
