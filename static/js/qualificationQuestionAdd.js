const qualificationQuestionButton = document.getElementById("qualificationQuestionButton");
const qualificationQuestionsContainer = document.getElementById("qualificationQuestionsContainer");
let qualificationQuestionCounter = 0;

const deleteQualificationQuestion = (event) => {
    let button = event.target;
    let li = button.parentNode;
    li.remove();
  }

const addQualificationQuestion = (event) => {
  event.preventDefault();

  if (qualificationQuestionCounter === 10) {
    alert("Максимальное кол-во вопросов");
  } else if (qualificationQuestionCounter < 10) {
    qualificationQuestionCounter++;

    const li = document.createElement("li");
    const input = document.createElement("input");
    const deleteButton = document.createElement("button");

    li.setAttribute("id", `qualification-${qualificationQuestionCounter}`);

    qualificationQuestionsContainer.append(li);

    deleteButton.addEventListener("click", deleteQualificationQuestion);

    const qualificationQuestionContainer = document.getElementById(`qualification-${qualificationQuestionCounter}`);

    qualificationQuestionContainer.append(input);
    qualificationQuestionContainer.append(deleteButton);

    deleteButton.setAttribute("class", "rounded btn delete-button qualification-question");
    deleteButton.innerText = 'delete';

    input.setAttribute("type", "text");
    input.setAttribute("class", "container form rounded question-input");
    input.setAttribute("id", `featureInput${qualificationQuestionCounter}`);
  }
}


qualificationQuestionButton.addEventListener("click", addQualificationQuestion);