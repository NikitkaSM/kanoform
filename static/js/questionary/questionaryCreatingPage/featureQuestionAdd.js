let featureQuestionCounter = 0;
const featureQuestionButton = document.getElementById('featureQuestionButton');
const featureQuestionsContainer = document.getElementById('featureQuestionsContainer');


const deleteFeatureQuestion = event => {
  const questions = document.getElementsByClassName('featureQuestion');

  if (questions.length === 1) {
    alert("Должен быть как минимум один вопрос");
    return;
  }

  let button = event.target;
  let li = button.parentNode;

  li.remove();

  featureQuestionCounter -= 1;

  let second_counter = 1;

  for (let i = 0; i < featureQuestionCounter; i++) {
    const questions_element_removed = Object.entries(questions)[i][1];
    questions_element_removed.removeAttribute('id');
  }

  for (let x = 0; x < featureQuestionCounter; x++) {
    const questions_element_added = Object.entries(questions)[x][1];

    questions_element_added.setAttribute(
      'id',
      `feature-${second_counter}`
    );
    second_counter++;
  }
};

const addFeatureQuestion = event => {
  event.preventDefault();
  
  if (featureQuestionCounter >= 20) {
    alert('Максимальное кол-во вопросов');
    return;
  }

  featureQuestionCounter++;

  const li = document.createElement('li');
  const deleteButton = document.createElement('button');
  const input = document.createElement('input');
  const featureDescriptionInput = document.createElement('input');

	featureDescriptionInput.setAttribute('type', 'text');
  featureDescriptionInput.setAttribute('style', 'text-align: left;');
  featureDescriptionInput.setAttribute("placeholder", "Введите описание характеристики");
  featureDescriptionInput.setAttribute("id", "feature-description");

  li.setAttribute('id', `feature-${featureQuestionCounter}`);
  li.setAttribute("class", 'featureQuestion');

  featureQuestionsContainer.append(li);

  deleteButton.addEventListener('click', deleteFeatureQuestion);

  const featureQuestionContainer = document.getElementById(`feature-${featureQuestionCounter}`);

  featureQuestionContainer.append(input);
  featureQuestionContainer.append(deleteButton);
  featureQuestionContainer.append(featureDescriptionInput);
  featureQuestionContainer.append(document.createElement("ul"));

  deleteButton.setAttribute('type', 'button');
  deleteButton.setAttribute('class', 'rounded btn delete-button');
  deleteButton.innerText = 'delete';


  input.setAttribute('type', 'text');
  input.setAttribute('class', 'container form rounded question-input feature-question');
  input.setAttribute("id", "feature-name");
  input.setAttribute('placeholder', 'Введите вопрос');

};

featureQuestionButton.addEventListener('click', addFeatureQuestion);