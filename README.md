# Snake Game

## Съдържание
* [Защо точно Snake Game?](#Защо-точно-Snake-Game?)
* [Какво е новото тук?](#Какво-е-новото-тук?)
* [Как се играе?](#Как-се-играе?)
* [Функционалност](#Функционалност)
* [Как да настроите и стартирате играта?](#Как-да-настроите-и-стартирате-играта?)
* [Източници](#Източници)

## Защо точно Snake Game?
  Snake Game е една добре позната на всички ни още от детството игра, която неминуемо изскочи в съзнанието ми при избора на тема за проект. Но както винаги, целта на кой да е проект не е да повтаря миналото, а да го надгражда. Надявам се ще се убедите, че в скромния си стремеж да пресъздам играта от малкия екран на GSM-ите и вълнението, което тя предизвикваше (и вярвам, че все още предизвиква), съм успяла не само да постигна задачата си, но и да предложа нов „прочит“ на играта, а именно разнообразена версия, още по-чаровна и завладяваща. 

## Какво е новото тук?
  Освен основните заподозрени - вечно гладната и неуморимо кръжаща змия и „възраждащата се“ червена ябълка, в игралното поле се появява образът на Жълтицата - тя, досущ като Ябълката, се появява на непредсказуемо място с разликата, че ако не бъде взета навреме, сменя позицията си. Бъде ли грабната обаче, в портфейла на ненаситната змия се прибавят допълнителни 3 точки - резултат, равняващ се на 3 погълнати плода. Така златната монета се явява златна възможност за трупане на точки в играта. С напрдването на резултата в играта змията започва да се движи все по-бързо, което в даден момент значително затруднява играча.
  
## Как се играе?
 Целта на играта е да се събират колкото е възможно повече точки. Играта започва веднага след стартиране на програмата, като змията се появява в горния ляв ъгъл на екрана и се направлява от играча чрез стрелките на клавиатурата. При сблъсък на главата на змията с тялото й или с контура на игралното поле играта приключва и зазвучава сигнал за край.
 През цялото време се отчита текущ резултат, брой взети монети и достигнато ниво, както и най-добро постижение досега в игрите. След края на всяка игра на екрана се изписва резултатът от текущото изпълнение, както и рекорд от игрите. В случай, че рекордът е подновен, се записва на мястото на предния.
 
 ## Функционалност
 За графичния интрфейс и като цяло за визуализацията на играта е използван Tkinter, а за фоновата музика и звуковите сигнали при улавяне на ябълка/монета и при край на играта - библиотеката pygame. "Рисуването" на фигурите е осъществено с Tkinter Canvas. Змията представлява свързана последователност от квадрати, а ябълката и монетата са цветни кръгове с произволно разположение върху игралното поле, като за тях е използван методът random. В началото змията се състои от 3 части (квадрати), като с всяко улавяне на плод се добавя по една част (квадрат), ябълката изчезва и се появява на ново място - произволно и непредсказуемо, на игралното поле. Монета се появава всеки път, когато текушият резултат от играта е кратен на 5. През цялото време се отчита броят на събраните точки и уловените монети, също както се вижда и рекордът от всички реализирани до момента игри. Най-високият резултат (с цел да бъде запазен и след изключване на програмата) се записва в текстов файл и всеки път при поставяне на нов рекорд се актуализират данните във файла. За да бъдат избегнати нежелани смущения във визуализацията на играта, опцията за преоразмеряване на прозореца на игралното поле е преустановена. След приключване на играта се излиза чрез натискане на бутона Exit в долния десен ъгъл.

## Как да настроите и стартирате играта?
  Като за начало трябва да инсталирате файловете локално с командата:
  ```
  $ git clone https://github.com/GitHubDiligentUser/SnakeGame.git
  ```
  Както обикновено, чрез терминала или командния панел достъпвате до директорията на проекта. След това, за да стартирате програмата, е необходимо да изтеглите всички модули, записани в тектовия файл reguirements.txt, чрез командата
  ```
  $ pip install -r requirements.txt
  ```
  За да се уверите, че всичко е свалено успешно, въведете командата
  ```
  $  pip check
  ```
  Трябва да получите съобщение "No broken requirements found."
  За стартиране на тестовете използвайте следната команда в терминала:
  ```
  $ python -m unittest
  ```

## Източници
Аудиозаписите са взети от github.com/GenXCoding/Learn-With-me и от https://www.youtube.com/watch?v=znveZhlltV8
