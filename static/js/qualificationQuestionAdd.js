const qualificationQuestionButton = document.getElementById(
  'qualificationQuestionButton'
);
const qualificationQuestionsContainer = document.getElementById(
  'qualificationQuestionsContainer'
);
let qualificationQuestionCounter = 1;

const deleteQualificationQuestion = event => {
  const questions = document.getElementsByClassName('qualificationQuestion');
  console.log("test");
  let button = event.target;
  let li = button.parentNode;

  li.remove();
  qualificationQuestionCounter -= 1;

  let second_counter = 1;

  for (let i = 0; i < qualificationQuestionCounter - 1; i++) {
    const questions_element_removed = Object.entries(questions)[i][1];
    questions_element_removed.removeAttribute('id');
  }

  for (let x = 0; x < qualificationQuestionCounter - 1; x++) {
    const questions_element_added = Object.entries(questions)[x][1];

    questions_element_added.setAttribute(
      'id',
      `qualification-${second_counter}`
    );
    second_counter++;
  }
};

const addQualificationQuestion = event => {
  event.preventDefault();

  if (qualificationQuestionCounter >= 11) {
    alert('Максимальное кол-во вопросов');
    return;
  }
  const li = document.createElement('li');
  const input = document.createElement('input');
  const deleteButton = document.createElement('button');
  const addAnswerVariantButton = document.createElement('button');

  addAnswerVariantButton.setAttribute('type', 'button');

  li.setAttribute('id', `qualification-${qualificationQuestionCounter}`);
  li.setAttribute('class', 'qualificationQuestion');

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

  qualificationQuestionCounter++;

};

qualificationQuestionButton.addEventListener('click', addQualificationQuestion);