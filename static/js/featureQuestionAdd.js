let featureQuestionCounter = 0;
const featureQuestionButton = document.getElementById('featureQuestionButton');
const featureQuestionsContainer = document.getElementById('featureQuestionsContainer');

const deleteFeatureQuestion = event => {
  let button = event.target;
  let li = button.parentNode;

  li.remove();

  featureQuestionCounter -= 1;

  const questions = document.getElementsByClassName("featureQuestion");
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
  if (featureQuestionCounter >= 19) {
    alert('Максимальное кол-во вопросов');
    return;
  }
  featureQuestionCounter++;

  const li = document.createElement('li');
  const deleteButton = document.createElement('button');
  const input = document.createElement('input');
  const answerVariantAddButton = document.createElement('button');

  li.setAttribute('id', `feature-${featureQuestionCounter}`);
  li.setAttribute("class", 'featureQuestion');

  featureQuestionsContainer.append(li);

  deleteButton.addEventListener('click', deleteFeatureQuestion);

  const featureQuestionContainer = document.getElementById(`feature-${featureQuestionCounter}`);

  featureQuestionContainer.append(input);
  featureQuestionContainer.append(deleteButton);


  deleteButton.setAttribute('type', 'button');
  deleteButton.setAttribute('class', 'rounded btn delete-button');
  deleteButton.innerText = 'delete';

  input.setAttribute('type', 'text');
  input.setAttribute('class', 'container form rounded question-input feature-question');
  input.setAttribute('id', `featureInput${featureQuestionCounter}`);
  input.setAttribute('placeholder', 'Введите вопрос');

};

featureQuestionButton.addEventListener('click', addFeatureQuestion);