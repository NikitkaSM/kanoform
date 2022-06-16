const qualificationQuestionButton = document.getElementById('qualificationQuestionButton');
const qualificationQuestionsContainer = document.getElementById('qualificationQuestionsContainer');
let qualificationQuestionCounter = 1;

const deleteAnswerVariant = event => {
  const button = event.target;
  const li = button.parentNode;
  const liContainer = li.parentNode;
  const answerVariants = liContainer.getElementsByClassName("qualification-answer-variant");

  if (answerVariants.length === 2) {
    alert('Должно быть минимум два варианта ответа');
    return;
  }

  li.remove();
}

const addAnswerVariant = event => {
  const button = event.target;
  const questionContainer = button.parentNode;
  const answerVariantsContainer = questionContainer.querySelector('ul');
  const answerVariant = document.createElement('li');
  const answerVariantInput = document.createElement("input");
  const deleteButton = document.createElement("button");
  const answerVariants = answerVariantsContainer.getElementsByClassName("qualification-answer-variant");

  answerVariantInput.setAttribute("type", 'text');
  answerVariantInput.setAttribute("class", "qualification-answer-variant-input");
  deleteButton.setAttribute("type", "button");
  deleteButton.setAttribute("class", "btn");
  deleteButton.innerText = "delete";
  deleteButton.addEventListener("click", deleteAnswerVariant);

  if (answerVariants.length === 4) {
    alert("Максимальное кол-во вариантов ответа");
    return;
  }

  answerVariant.setAttribute('class', 'qualification-answer-variant');
  answerVariantsContainer.append(answerVariant);
  const lastAnswerVariant = Object.entries(answerVariants).slice(-1)[0][1];

  lastAnswerVariant.append(answerVariantInput);
  lastAnswerVariant.append(deleteButton);

};

const deleteQualificationQuestion = event => {
  const questions = document.getElementsByClassName('qualificationQuestion');

  if (questions.length === 1) {
    alert('Должен быть как минимум один вопрос');
    return;
  }

  const button = event.target;
  const li = button.parentNode;

  li.remove();
  qualificationQuestionCounter -= 1;

  let second_counter = 1;

  for (let i = 0; i < qualificationQuestionCounter - 1; i++) {
    const questions_element_removed = Object.entries(questions)[i][1];
    questions_element_removed.removeAttribute('id');
  }

  for (let x = 0; x < qualificationQuestionCounter - 1; x++) {
    const questions_element_added = Object.entries(questions)[x][1];

    questions_element_added.setAttribute('id', `qualification-${second_counter}`);
    second_counter++;
  }
};

const addQualificationQuestion = event => {
  event.preventDefault();

  if (qualificationQuestionCounter >= 11) {
    alert('Максимальное кол-во вопросов');
    return;
  }

  const answerVariantAddButton = document.createElement('button');
  const li = document.createElement('li');
  const input = document.createElement('input');
  const deleteButton = document.createElement('button');

  li.setAttribute('id', `qualification-${qualificationQuestionCounter}`);
  li.setAttribute('class', 'qualificationQuestion');

  qualificationQuestionsContainer.append(li);

  input.setAttribute('type', 'text');
  input.setAttribute('class', 'container form rounded question-input');
  input.setAttribute('id', `featureInput${qualificationQuestionCounter}`);
  input.setAttribute('placeholder', 'Введите вопрос');

  deleteButton.setAttribute('type', 'button');
  deleteButton.addEventListener('click', deleteQualificationQuestion);

  answerVariantAddButton.setAttribute('class', 'answer-variant-add-button btn');
  answerVariantAddButton.setAttribute('type', 'button');
  answerVariantAddButton.innerText = 'Добавить вариант ответа';
  answerVariantAddButton.addEventListener('click', addAnswerVariant);

  const qualificationQuestionContainer = document.getElementById(`qualification-${qualificationQuestionCounter}`);

  qualificationQuestionContainer.append(input);
  qualificationQuestionContainer.append(deleteButton);
  qualificationQuestionContainer.append(answerVariantAddButton);
  qualificationQuestionContainer.append(document.createElement('ul'));

  deleteButton.setAttribute('class', 'rounded btn delete-button qualification-question');
  deleteButton.innerText = 'delete';

  qualificationQuestionCounter++;
};

qualificationQuestionButton.addEventListener('click', addQualificationQuestion);
