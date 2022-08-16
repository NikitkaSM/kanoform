const questionaryId = window.location.pathname.slice(15, 17)

const questionaryShow = () => {
  axios
    .get(`/api/questionary/${questionaryId}`)
    .then(response => {
      const questionary = response.data
      const qualificationQuestionsContainer = document.getElementsByClassName(
        'qualification-questions'
      )[0]
      const featureQuestionsContainer =
        document.getElementsByClassName('feature-questions')[0]

      if (questionary.qualification_questions.length !== 0) {
        questionary.qualification_questions.map(qQuestion => {
          const div = document.createElement('div')
          const h1 = document.createElement('h1')
          const answerVariantsContainer = document.createElement('div')
          answerVariantsContainer.setAttribute(
            'style',
            'display: flex; justify-content: center; flex-direction: column;'
          )

          div.setAttribute('class', 'qualification-question')
          h1.innerText = qQuestion.question

          qualificationQuestionsContainer.append(div)
          div.append(h1)

          qQuestion.answer_variants.map(answerVariant => {
            const input = document.createElement('input')
            const p = document.createElement('p')

            p.innerHTML = `<input type="radio">${answerVariant}</input>`
            input.setAttribute('type', 'radio')
            input.setAttribute('name', 'qAnswerVariant')
            p.setAttribute('style', 'margin: 0 !important;')
            div.setAttribute(
              'style',
              'display: flex; margin-left: auto; margin-right: auto; flex-direction: column'
            )

            div.append(answerVariantsContainer)
            answerVariantsContainer.append(p)
          })
        })
      }

      questionary.feature_questions.map(fQuestion => {
        const mainContainer = document.createElement('div')
        const featureName = document.createElement('h1')
        const featureDescription = document.createElement('span')
        const typicalQuestions = document.createElement('div')
        const firstQuestionContainer = document.createElement('div')
        const secondQuestionContainer = document.createElement('div')
        const thirdQuestionContainer = document.createElement('div')
        const firstQuestion = document.createElement('h3')
        const secondQuestion = document.createElement('h3')
        const thirdQuestion = document.createElement('h3')
        const thirdsAnswerVariantsContainer = document.createElement('div')
        const numberContainer = document.createElement('div')
        const inputContainer = document.createElement('div')

        numberContainer.setAttribute('id', 'numberContainer')
        inputContainer.setAttribute('id', 'inputContainer')
        thirdsAnswerVariantsContainer.setAttribute('id', 'thirdQuestion')

        firstQuestion.innerText =
          'Насколько вам понравится наличие такой характеристики в продукте?'
        secondQuestion.innerText =
          'А если эта характеристика будет отсутствовать или слабо выражена?'
        thirdQuestion.innerText = 'Насколько для вас важна эта характеристика?'
        thirdQuestion.setAttribute('style', 'display: block !important;')
        firstQuestionContainer.append(firstQuestion)
        secondQuestionContainer.append(secondQuestion)
        thirdQuestionContainer.append(thirdQuestion)
        thirdQuestionContainer.append(thirdsAnswerVariantsContainer)
        thirdsAnswerVariantsContainer.append(numberContainer)
        thirdsAnswerVariantsContainer.append(inputContainer)

        firstQuestionContainer.setAttribute('id', 'firstQuestion')
        secondQuestionContainer.setAttribute('id', 'secondQuestion')

        const questions = [
          firstQuestionContainer,
          secondQuestionContainer,
          thirdQuestionContainer,
        ];
        const firstQuestionAnswerVariants = [
          'Мне это нравится',
          'Я ожидаю, что эта характеристика будет в продукте',
          'Я отношусь к ней нейтрально',
          'Я могу ее терпеть',
          'Мне это не нравится',
        ]
        const secondQuestionAnswerVariants = [
          'Мне это нравится',
          'Я ожидаю это',
          'Я отношусь к этому нейтрально',
          'Я могу это терпеть',
          'Мне это не нравится',
        ]
        const thirdQuestionAnswerVariants = [
          '1',
          '2',
          '3',
          '4',
          '5',
          '6',
          '7',
          '8',
          '9',
        ]
        featureName.innerText = fQuestion.feature_name
        featureName.setAttribute('style', 'margin: 0 !important;')
        featureDescription.innerText = fQuestion.feature_description

        featureQuestionsContainer.append(mainContainer)
        mainContainer.append(featureName)
        mainContainer.append(featureDescription)
        mainContainer.append(typicalQuestions)
        questions.map(question => typicalQuestions.append(question))

        firstQuestionAnswerVariants.map(answerVariant => {
          const question = document.createElement('h3')
          const p = document.createElement('p')
          const container = document.getElementById('firstQuestion')
          container.setAttribute(
            'style',
            'display: flex; justify-content: center; flex-direction: column; margin: 40px;'
          )
          p.innerHTML = `<input type="radio"/>${answerVariant}`
          container.append(p)
        })

        secondQuestionAnswerVariants.map(answerVariant => {
          const question = document.createElement('h3')
          const p = document.createElement('p')
          const container = document.getElementById('secondQuestion')
          container.setAttribute(
            'style',
            'display: flex; justify-content: center; flex-direction: column;'
          )
          p.innerHTML = `<input type="radio"/>${answerVariant}`
          container.append(p)
        })

        thirdQuestionAnswerVariants.map(answerVariant => {
          const p = document.createElement('p')
          const input = document.createElement('input')
          const container = document.getElementById('thirdQuestion')
          const numberContainer = document.getElementById('numberContainer')
          const inputContainer = document.getElementById('inputContainer')

          inputContainer.setAttribute(
            'style',
            'display: flex; flex-direction: row; justify-content: center; margin-bottom: 20px;'
          )
          numberContainer.setAttribute(
            'style',
            'display: flex; flex-direction: row; justify-content: center;'
          )

          input.setAttribute('type', 'radio')
          input.setAttribute('style', 'margin-left: 2px !important;')
          p.innerHTML = answerVariant
          p.setAttribute(
            'style',
            'margin-left: 5px; margin-right: 5px; margin-top: 0 !important; margin-bottom: 2px !important;'
          )
          container.append(numberContainer)
          container.append(inputContainer)

          inputContainer.append(input)
          numberContainer.append(p)
        })
      })

      const header = document.getElementsByClassName('header')[0]
      const questionaryName = (header.querySelector('h1').innerText =
        questionary.name)
      const questionaryAuthor = (header.querySelector(
        'p'
      ).innerText = `Автор: ${questionary.user.username}`)
    })
    .catch(error => console.log(error))
}
const init = () => {
  questionaryShow()
}

init()
