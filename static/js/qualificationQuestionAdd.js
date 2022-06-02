const qualificationQuestionButton = document.getElementById(
	'qualificationQuestionButton'
);
const qualificationQuestionsContainer = document.getElementById(
	'qualificationQuestionsContainer'
);
let qualificationQuestionCounter = 1;

const deleteQualificationQuestion = event => {
	let button = event.target;
	let li = button.parentNode;

	li.remove();
	qualificationQuestionCounter -= 1;
	for (let i; i < qualificationQuestionCounter; i++) {
		let question = document
			.getElementById(`qualification-${i}`)
			.removeAttribute('id');
		if (question === null || undefined) {
			console.log(i);
		} else {
			question.setAttribute('id', `qualification-${i}`);
		}
	}
};

const addQualificationQuestion = event => {
	event.preventDefault();

	if (qualificationQuestionCounter === 11) {
		alert('Максимальное кол-во вопросов');
	} else if (qualificationQuestionCounter < 11) {
		const li = document.createElement('li');
		const input = document.createElement('input');
		const deleteButton = document.createElement('button');
		const addAnswerVariantButton = document.createElement('button');

		addAnswerVariantButton.setAttribute('type', 'button');

		li.setAttribute('id', `qualification-${qualificationQuestionCounter}`);

		qualificationQuestionsContainer.append(li);

		deleteButton.addEventListener('click', deleteQualificationQuestion);

		const qualificationQuestionContainer = document.getElementById(
			`qualification-${qualificationQuestionCounter}`
		);

		qualificationQuestionContainer.append(input);
		qualificationQuestionContainer.append(deleteButton);
		qualificationQuestionContainer.append(addAnswerVariantButton);

		deleteButton.setAttribute(
			'class',
			'rounded btn delete-button qualification-question'
		);
		deleteButton.innerText = 'delete';

		input.setAttribute('type', 'text');
		input.setAttribute('class', 'container form rounded question-input');
		input.setAttribute('id', `featureInput${qualificationQuestionCounter}`);
		console.log(qualificationQuestionCounter);

		qualificationQuestionCounter++;
	}
};

qualificationQuestionButton.addEventListener('click', addQualificationQuestion);
