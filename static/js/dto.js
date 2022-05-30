const submitButton = document.getElementById('submitFormButton');
const basedInput = document.getElementById('based-feature-input');

const postRequest = () => {
	let notNullInputs = [];
	for (let i = 1; i < 20; i++) {
		let input = document.getElementById(`featureInput${i}`);
		if (input === null) {
			break;
		} else {
			notNullInputs.push(input.value);
		}
	}
	if (notNullInputs.length === 0) {
		alert('Вопросов характеристик должно быть больше чем 1');
	}
}

submitButton.addEventListener('click', postRequest);
