from selenium.webdriver.common.by import By

# --- Страница регистрации ---
REGISTER_NAME_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')  # Поле "Имя"
REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="email"]')  # Поле "Email"
REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="password"]')  # Поле "Пароль"
REGISTER_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
REGISTER_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка "Войти" из регистрации

# --- Страница входа ---
LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="name"]')  # Вход — поле email (на сайте используется name="name")
LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="Пароль"]')  # в некоторых версиях поле так называется; лучше проверять
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти"
LOGIN_RECOVER_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # Ссылка восстановить пароль
LOGIN_REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Ссылка "Зарегистрироваться"

# --- Главная страница + Шапка ---
LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка входа на главной
PROFILE_LINK = (By.XPATH, "//p[text()='Личный кабинет']")  # Кнопка Личный кабинет в шапке
CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка Конструктор в шапке
STELLAR_BURGERS_LOGO = (By.CSS_SELECTOR, 'div.AppHeader_header__logo__2D0X2')  # Логотип сайта в шапке

# --- Личный кабинет ---
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка выхода

# --- Конструктор (главный блок тестирования) ---
SECTION_BUNS = (By.XPATH, "//span[contains(text(),'Булки')]")  # Вкладка "Булки" в конструкторе
SECTION_SAUCES = (By.XPATH, "//span[contains(text(),'Соусы')]")  # Вкладка "Соусы"
SECTION_FILLINGS = (By.XPATH, "//span[contains(text(),'Начинки')]")  # Вкладка "Начинки"

# Пример локатора для проверки активного состояния вкладки
ACTIVE_TAB = (By.CSS_SELECTOR, 'div.tab_tab__1SPyG.tab_tab_type_current__2BEPc > span')

# --- Сообщения об ошибках ---
ERROR_MESSAGE = (By.CSS_SELECTOR, 'p.input__error')  # Сообщения валидации под полями

# --- Модальные окна ---
MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, 'div.Modal_modal__container__1j_lF button')  # Кнопка закрытия модального окна
