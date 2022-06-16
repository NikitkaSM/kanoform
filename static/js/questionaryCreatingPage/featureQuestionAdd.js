let featureQuestionCounter = 0;
const featureQuestionButton = document.getElementById('featureQuestionButton');
const featureQuestionsContainer = document.getElementById('featureQuestionsContainer');

const deleteAnswerVariant = event => {
  const button = event.target;
  const li = button.parentNode;
  const liContainer = li.parentNode;
  const answerVariants = liContainer.getElementsByClassName("feature-answer-variant");

  if (answerVariants.length === 2) {
    alert("Должно быть минимум два варианта ответа");
    return;
  }

  li.remove();
}

const addAnswerVariant = event => {
  const button = event.target;
  const questionContainer = button.parentNode;
  const answerVariantsContainer = questionContainer.querySelector("ul");
  const answerVariant = document.createElement("li");
  const answerVariantInput = document.createElement("input");
  const deleteButton = document.createElement("button");
  const answerVariants = answerVariantsContainer.getElementsByClassName("feature-answer-variant");

  answerVariantInput.setAttribute("type", 'text');
  answerVariantInput.setAttribute("class", "feature-answer-variant-input");
  deleteButton.setAttribute("type", "button");
  deleteButton.setAttribute("class", "btn");
  deleteButton.innerText = "delete";
  deleteButton.addEventListener("click", deleteAnswerVariant);

  if (answerVariants.length === 4) {
    alert("Максимальное кол-во вариантов ответа");
    return;
  }

  answerVariant.setAttribute("class", 'feature-answer-variant');
  answerVariantsContainer.append(answerVariant);
  const lastAnswerVariant = Object.entries(answerVariants).slice(-1)[0][1];

  lastAnswerVariant.append(answerVariantInput);
  lastAnswerVariant.append(deleteButton);
}

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
  const answerVariantAddButton = document.createElement('button');
  const featureDescription = document.createElement('input');

	featureDescription.setAttribute('type', 'text');
  featureDescription.setAttribute('style', 'text-align: left;');

  li.setAttribute('id', `feature-${featureQuestionCounter}`);
  li.setAttribute("class", 'featureQuestion');

  featureQuestionsContainer.append(li);

  deleteButton.addEventListener('click', deleteFeatureQuestion);

  const featureQuestionContainer = document.getElementById(`feature-${featureQuestionCounter}`);

  featureQuestionContainer.append(input);
  featureQuestionContainer.append(deleteButton);
  featureQuestionContainer.append(answerVariantAddButton);
  featureQuestionContainer.append(featureDescription);
  featureQuestionContainer.append(document.createElement("ul"));

  deleteButton.setAttribute('type', 'button');
  deleteButton.setAttribute('class', 'rounded btn delete-button');
  deleteButton.innerText = 'delete';

  answerVariantAddButton.setAttribute('class', 'answer-variant-add-button btn');
  answerVariantAddButton.setAttribute('type', 'button');
  answerVariantAddButton.innerText = 'Добавить вариант ответа';
  answerVariantAddButton.addEventListener('click', addAnswerVariant);

  input.setAttribute('type', 'text');
  input.setAttribute('class', 'container form rounded question-input feature-question');
  input.setAttribute('id', `featureInput${featureQuestionCounter}`);
  input.setAttribute('placeholder', 'Введите вопрос');

};

featureQuestionButton.addEventListener('click', addFeatureQuestion);