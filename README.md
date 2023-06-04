

**Описание:**
Проект «API для Yatube» предоставляет доступ к постам, комментариям, группам и подпискам постов социальной сети Yatube, в зависимости от статуса пользователя(аутентифицированного или гостя).

**Установка**
**Как запустить проект:**

Клонировать репозиторий и перейти в него в командной строке:[^1].
git clone git@github.com:yandex-praktikum/api_final_yatube.git[^2].
cd kittygram[^3].

Cоздать и активировать виртуальное окружение:
python3 -m venv env
source env/bin/activate

Установить зависимости из файла requirements.txt:
python3 -m pip install --upgrade pip
pip install -r requirements.txt

Выполнить миграции:
python3 manage.py migrate

Запустить проект:
python3 manage.py runserver

**Примеры**
