const qualificationQuestionButton = document.getElementById('qualificationQuestionButton');
const qualificationQuestionsContainer = document.getElementById('qualificationQuestionsContainer');
let qualificationQuestionCounter = 1;
let answerVariantCounter = 0;

const addAnswerVariant = event => {
  const button = event.target;
  const questionContainer = button.parentNode;
  const answerVariantsContainer = questionContainer.querySelector('ul');
  const answerVariant = document.createElement('li');
  const answerVariants = document.getElementsByClassName('qualificationAnswerVariant');

  if (answerVariants.length === 2) {
    alert('Должно быть минимум два варианта ответа');
    return;
  }

  answerVariant.setAttribute('class', 'qualificationAnswerVariant');
  
  answerVariantsContainer.append(answerVariant);


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
