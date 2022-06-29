const submitButton = document.getElementById("form-container");

function getCookie(cookieName) {
  const name = cookieName + "=";
  const cookieDecoded = decodeURIComponent(document.cookie); //to be careful
  const cookieArr = cookieDecoded.split('; ');
  let response;
  cookieArr.forEach(val => {
    if (val.indexOf(name) === 0) response = val.substring(name.length);
  })
  return response;
}

const getQuestionaryName = () => {
  const questionaryNameInput = document.getElementById("questionary-name");
  if (questionaryNameInput.value === "") {
    alert("У анкеты должно быть название");
    return;
  }

  return questionaryNameInput.value;
}

const getFeatureQuestions = () => {
  const featureQuestionsLi = document.getElementsByClassName("featureQuestion");
  const featureQuestionsLiLength = featureQuestionsLi.length;
  const featureQuestions = []

  if (featureQuestionsLiLength === 0) {
    alert("Должен быть минимум один вопрос характеристики");
    return;
  }

  for (let i = 0; i < featureQuestionsLiLength; i++) {

    const featureQuestionContainer = featureQuestionsLi[i];
    const featureNameInput = featureQuestionContainer.querySelector("#feature-name");
    const featureDescriptionInput = featureQuestionContainer.querySelector("#feature-description");

    if (featureDescriptionInput.value === "" || featureNameInput.value === "") {
      alert("Поля описания или имя характеристики не должны быть пустыми");
      return;
    }

    const featureQuestion = {}
    featureQuestion.feature_name = featureNameInput.value;
    featureQuestion.feature_description = featureDescriptionInput.value;

    featureQuestions.push(featureQuestion);
  }

  return featureQuestions;
}

const getQualificationQuestions = () => {
  const qualificationQuestionsLi = document.getElementsByClassName("qualificationQuestion");
  const qualificationQuestionsLiLength = qualificationQuestionsLi.length;
  const qualificationQuestions = [];

  for (let x = 0; x < qualificationQuestionsLiLength; x++) {

    const qualificationQuestionContainer = qualificationQuestionsLi[x];
    const qualificationQuestionInput = qualificationQuestionContainer.querySelector("#qualification-question");
    const answerVariantsLi = qualificationQuestionContainer.getElementsByClassName("qualification-answer-variant");
    const answerVariantsLength = answerVariantsLi.length;
    const qualificationQuestion = {};
    qualificationQuestion.answer_variants = [];

    if (qualificationQuestionInput.value === "") {
      alert("Поле квалификационного вопроса не должно быть пустым");
      return;
    }

    if (answerVariantsLength === 0 || answerVariantsLength === 1) {
      alert("Вопросов ответа на квалификационный вопрос должно быть минимум 2");
      return;
    }

    for (let n = 0; n < answerVariantsLength; n++) {
      const answerVariantLi = answerVariantsLi[n];
      const answerVariantInput = answerVariantLi.querySelector("#qualification-answer-variant-input");

      if (answerVariantInput.value === "") {
        alert("Поле варианта ответа на квалификационный вопрос не должно быть пустым");
        return;
      }

      qualificationQuestion.answer_variants.push(answerVariantInput.value);
    }

    qualificationQuestion.question = qualificationQuestionInput.value;

    answerVariantsLength <= 2 ?
      (
        qualificationQuestion.is_multiple = false
      )
      : (
        qualificationQuestion.is_multiple = true
      );

    qualificationQuestions.push(qualificationQuestion);

    return qualificationQuestions;
  }
}

const sendRequest = event => {
  event.preventDefault();
  const featureQuestions = getFeatureQuestions();
  const qualificationQuestions = getQualificationQuestions();
  const questionaryName = getQuestionaryName();

  const questionary = {
    name: questionaryName,
    feature_questions: featureQuestions,
    qualification_questions: qualificationQuestions
  }

  const csrftoken = getCookie("csrftoken");

  axios.post("/api/questionary/", questionary, {
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    }
  })
    .then(response => {
      console.log(response.data)
    })
    .catch(error => {
      console.log(error)
    });
}

submitButton.addEventListener("submit", sendRequest);