const featureInputClassName = "feature-answer-variant-input";
const qualificationInputClassName = "qualification-answer-variant-input";
const featureLiClassName = "feature-answer-variant";
const qualificationLiClassName = "qualification-answer-variant";
const submitButton = document.getElementById("submitFormButton");

//  TODO
//  1. Протестить получение значений из форм с помощью object.entries - done
//  2. Внедрить эту функцию в итоговый вариант после тестинга
// const getAnswerVariants = className => {
//   return document.getElementsByClassName(className);
// }
// const answerVariants = getAnswerVariants(featureInputClassName);
// 3. Добавить проверку на есть ли вообще фича вопросы и их инпуты
// 4. Добавить проверку на то, если инпут существует, то он должен быть заполнен

const getFeatureAnswerVariants = (inputClassName, liClassName) => {
  const feature_questions = [];
  const answerVariantsLiQuantity = document.getElementsByClassName("featureQuestion").length;

  for (let x = 0; x < answerVariantsLiQuantity; x++) {
    const container = document.getElementsByClassName("featureQuestion")[x];
    const featureDescription = container.getElementById
    const answerVariants = container.getElementsByClassName(featureInputClassName);
    const answerVariantsInputQuantity = answerVariants.length;

    for (let i = 0; i < answerVariantsInputQuantity; i++) {
      const answerVariant = answerVariants[i];
      
      if (answerVariant.value === "") {
				alert('Поле варианта ответа не должно быть пустым');
				return;
			}
      console.log(answerVariant.value);
    }
  }
}

submitButton.addEventListener("click", getFeatureAnswerVariants);