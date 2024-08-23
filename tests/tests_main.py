import pytest
from time import sleep
import ya_main
from selenium_main import *
from main import check_age, check_auth, get_cost, new_func


@pytest.mark.parametrize(
	"age, result", (
			[-1, 'Доступ запрещён'],
			[0, 'Доступ запрещён'],
			[17, 'Доступ запрещён'],
			[18, 'Доступ разрешён'],
			[20, 'Доступ разрешён'],
	)
)
def test_check_age(age, result):
	assert check_age(age) == result


@pytest.mark.parametrize(
	"login, password, result", (
			['admin', 'password', 'Добро пожаловать'],
			['', 'password', 'Доступ ограничен'],
			['admin', '', 'Доступ ограничен'],
	)
)
def test_check_auth(login, password, result):
	assert check_auth(login, password) == result


@pytest.mark.parametrize(
	"weight, result", (
			[-1, 'Ошибка ввода данных'],
			[0, 'Ошибка ввода данных'],
			[1, 'Стоимость доставки: 200 руб.'],
			[10, 'Стоимость доставки: 200 руб.'],
			[11, 'Стоимость доставки: 500 руб.'],
			[100, 'Стоимость доставки: 500 руб.'],
	)
)
def test_get_cost(weight, result):
	assert get_cost(weight) == result


@pytest.mark.skipif(True, reason="Функция пока не реализована")
def test_new_func():
	assert new_func() == ''


@pytest.mark.parametrize(
	"param, folder_name, status", (
			['path', 'New folder', 201],
			['path', 'New folder/New folder', 201],
			['path', 'New folder', 409],
			['pat', 'New folder', 400],
	)
)
def test_create_folder(param, folder_name, status):
	response = ya_main.YADisk().create_folder(param, folder_name)
	assert response.status_code == status


@pytest.mark.parametrize(
	"param, folder_name, status", (
			['pat', 'New folder', 400],
			['path', 'New folder/New folder', 204],
			['path', 'New folder', 204],
			['path', 'New folder', 404],

	)
)
def test_delete_folder(param, folder_name, status):
	response = ya_main.YADisk().delete_folder(param, folder_name)
	assert response.status_code == status


def test_check_ya_auth():
	browser.get("https://passport.yandex.ru/auth/")
	login = browser.find_element(By.ID, 'passp-field-login')
	login.send_keys('')		# Указать логин или почту
	login_get = browser.find_element(By.ID, 'passp:sign-in')
	login_get.click()
	password = wait_element(browser, by=By.ID, value='passp-field-passwd')
	password.send_keys('')		# Указать пароль
	get_continue = browser.find_element(By.XPATH, '//button[@data-t="button:action:passp:sign-in"]')
	get_continue.click()
	sleep(5)
	url = browser.current_url
	assert url == 'https://id.yandex.ru/'
