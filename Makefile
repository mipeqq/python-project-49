install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

<<<<<<< HEAD
=======
brain-calc:
	poetry run brain-calc

>>>>>>> 46f706c (Обновлены исключения; Добавлена игра brain-even; Пересобран пакет; Создана аскинема; создан скрипт brain-even.py)
build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games

