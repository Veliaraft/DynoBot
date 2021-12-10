Основная логика бота в файле Play.py. На основе полученных координат мы смотрим поле перед динозавриком, и определяем препятствие по изменению цвета.

По компьютерному зрению здесь определение координат динозаврика. Я сделал двумя способами
1) Через PyAutoGui - locate_on_screen
Сфотал динозавра, обрезал его от головы до ног, сохранил в dyno.png - она найдёт координаты клона на экране.
2) Через OpenCV.
Ищет координаты на основе файла Dino.png.

Запускать с файла DynoBot.py. Для испольования pyautogui или cv2 оставить раскомментированной нужную из двух последних строк.

В чём же здесь именно компьютерное зрение?
Мне не хотелось описывать вручную координаты игрового поля для нахождения динозавра. Пусть компьютер сам ищет своего динозавра!
Тестировал на двух компьютерах с разрешениями 1366x768 и 1280x720 - на обоих работало одинаково погано, но работало.
(It's alive! It's working! I'm scare.)
Поганость обусловлена логикой Play(). Он написан достаточно тупо.

Сразу оговорюсь (просто чтобы не ломали голову)
1) Не делал проверку на переключение рабочей среды и т.д. - он просто любит реагировать на цвет, потому бот любит на тёмной теме понафигобесить в коде) Это святое)))
2) В логике Play() прописан сдвиг левой координаты наблюдаемого пространства - это сделано для ускоряющегося темпа игры, чтобы с течением времени динозавр начинал раньше прыгать. Если игра рестартнулась - координата не сбрасывается, а это значит что диноаврик будет прыгать раньше, чем ему положено.