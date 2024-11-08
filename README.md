# Support Telegram Bot

## Описание

Этот бот служит для автоматизации работы службы поддержки, позволяя пользователям задавать вопросы, а администраторам — отвечать на них. Он предоставляет интерфейс для начала и окончания смены для администраторов, а также возможность пользователям задавать вопросы и получать ответы от администрации. 

Бот использует библиотеку `aiogram` для взаимодействия с Telegram API, а также SQLite для хранения данных пользователей и администраторов.

## Код создан на основе IDeF0 диаграммы

[ссылка на диаграмму](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=support-tg-bot.drawio#R%3Cmxfile%3E%3Cdiagram%20name%3D%22%D0%A1%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0%20%E2%80%94%201%22%20id%3D%22VsIl_wmOL8zB-NCBbUsj%22%3E7V1Zc6PKFf41erSLZhM8ylqSVN1JTTKpyp28MRIjkysLRcJj%2B%2F76sHTD6dPdgBCLJPwiQwva0Gf9ztKaGPOX978cvcPzl3Dj7ya6tnmfGIuJrpvEduI%2FychHNqLrrp6NbI%2FBJhsjxcC34E%2BfDmp09DXY%2BCfuwigMd1Fw4AfX4X7vryNuzDsewzf%2Bsp%2Fhjv%2BvB2%2FrCwPf1t5OHP13sImes1FHnxbjf%2FWD7TP7z8R2s29ePHYxfZPTs7cJ38CQsZwY82MYRtnRy%2Fvc3yWrx9Ylu2%2Bl%2BDZ%2FsKO%2Fj%2BrcsPv9zfn6j%2FU%2FV8vD94%2B%2F7%2F6z3f7rywOd5Ze3e6UvPFlok1n6%2BWSln0%2Fg2JgsyMTR0uPscx7fnR6Q9HOZXqCng%2FEBYTPEx0Z6bLOL45Endu%2BK3Rt%2FmuDTAv8uu3GWflKmOkUfjEzH8HW%2F8ZM31SbG09tzEPnfDt46%2BfYt5sx47Dl62cVnJD6k7%2BwfI%2F9duZgkJ1HM3H744kfHj%2FgSeoNuUKpSviYuPX8rmIQwyj8DBrHpmEf5cptPXZAuPqDUO4OSupSS7gws7YISp6DnjFEpH18w2sYjK0Yfk656QXYZIxSfmkCfeKUjngjeLtju4%2BN1vOL%2BMR5I6BHEgjejX7wEm01y%2B9PRPwV%2Fej%2FSqRLqHsJgH6XLZz1NrEUy12sUnjLVkUx9io7hH%2F483IXxvIt9uE9m%2BRnsdngo3EdU4%2BhWO3xBTJ4vDJEtDE3CFmZXbGGIbIFp4%2B83s0RTJsTYeadTsOYpxctWdru%2FEdRm5RKBNbAkS8DGjv7Oi4Jf%2FPSydaH%2F4WvCDoACNk%2BBXP%2ByKU7h63Ht07ugvkQTYREXJoq849aPhIlSMuWv3ZxyplygdSDQKyCFSyrKusYrYnuXCN4m%2BBUfbpNDQeNm6jmT3CkY14EqQAYhUw7Z1PHLwdlvQvJbkHTMZprEAPQq6dbYJN2y3ccp4ahgG1YzYZfN5aK5OpZ3e2z00414zW3eXJLGylqYK3%2FMnug3HRv9DAupQFLQ4Fz6mXr1XB3Tz5Hb2yWwf7kVzDEO8JjpaaV97sogL0dukE1iVltkGSTrzCK7AkfNvv6NQWPIJzNAzIXowXkvCYDd%2Fzgd0pWSMJDIEOdDdsrFo%2BahHMZjezSYV8ceYERmBUPopj4Bnqhvh4AogmsmCIctQBjGBlEWhw%2B9IMiViibgAPt%2Fr0kUMQ1oPGSSM4svcA7vmcKgX3MGRwfmRQP%2FeS7E4jI94gqhIp3dVYYG23vgOXgYmz1eupCSKGIDE5ofz7t%2Fl5y8kMhzQIUFWNt8zaEehxYE%2Bhhlz38LShzE5JyWQrVYp2uWqNNJiT5rX6crYrXtMcNNkLoN2jK8T2nrOvVIa3RGWkm8NSEt1KQzTlax5poCYtvgeAXUHAIVNoAlBORdboQPegjDm6boxxkyxujMj9NFYiQu2Dd6Gh6j53Ab7r3dshhFjltxzW9heKCL%2FF8%2Fij7o6iXrz1M3Xq7jx%2B%2F0%2FvTke3LyaLHTxTv8cvFxpo8Yv0%2FqjJVJBEVlmbNVdqErJ2ltd%2FIy%2BsidNfdyXJ7DrTy1ljswGr1MERNAkYUZGFwCvTFjblAtq58Q9Tfvh7%2FrTg8oBZgm6enNkzyjAvmqRHqU4q49apY7vQx9sEvCnz9Pfjd4QJHRgQrdkcSZ5H63BbgB8oTFAgwEDC4Z3o%2FHXeF2B9wIAw8lUQL2L3T42AuZh5JDHRHkMGCBWXToZL7lSDzEXpP5ZHTJHIKCyTYxGweTMT1lc3WN%2FSXZnNbMidxaQAld8fggn5TFEaB64awL9Eqh1TLLbYz4RPrqFC9xdMtQtA3NUkOxmL0qltFlqTD8t92G4URhIrPf%2FDBRJKjEwjukABxgfjWgT1ZqlVAj5ZBO2cTVyFJVNV3aed1n4V%2B4zOPOlaQjvxjrQzHSlrk0NOUmfbpq%2FVio2SV4PLYS9BlgdNbknx8CC4tb7MKL0%2FjKvTyzVDNFKX%2BJsWpyC1d8WrYYU9BluaFpZzEFW9Td44gpUMxQGVPQLTlRe4opSIzt4gZL%2BG4zZGCXyvOD9qjpOl8xxKrhrziEIJYUqH2ACwFBA0wvmnZ2fJ5BqxSQgQMGFsE%2B5dABA%2BbGj8evl1RsOlpD114y19Tq17vXFYmju%2Ffuz%2FCXh%2FLxYYNLibcO55kr1iZXdE3fW53xk1Bryita9Cx5RrFK3dI1G7X%2Fb6KMoiOpLpSqu%2B68f3k6YUYEU88oWDAgLAGCGFLnmT27hckQFiDIbChFsQRqB%2BYY3DMQfYlw5o%2BWszABTokpeyEot47a%2F2gM55GDzTfWyRMrnz04FwslasKxphKhlKX5O%2FPDDHOkkFy3akJywxgSkpsKNwt6SNCLEu04apCVq4Icw9cxredV7d0kGM%2FEoix%2FT6aoev%2FaobguSdGWOexI1WfOJcTD0GANZU0GxtW5U8VA2PBd9ZKky33jascSsXDTFmrZXA6aq2tcrYiYdefg1vNuoeTDch%2F4RFLPvCYYHLVfOHX5smDbkegRQyJD3W3DMLo2Hgf55m5jJYImcnpu4zEUlaEQSZsSYwpltxBNWMadi%2Fic3SJGiLDeQP1AcK763usSgPE8Eobws1QFwn8hBpTYo3Nv%2B4mgr1pTWgophQi6V4%2FLlCjGUSBog0LTSgRtKkjaE4JWVzF%2FIujuEHQmFqUI2jYvM9zdY2bjnCTXJenrc7NWGiicamUnBvYKkmb%2FOTO7Gf4H31765KYCrKAVQ5PkTwsnubAXNUvvDRxNIASFE5y64QRcItoeDBhfXT%2Fej41o2H%2BvCwSEqdyeYwnG%2BLZowr3T2O1rWjzd914MhqIUjwDNx0IynDaFKGfBEF%2BKhArwJGKyEqgk1gTIfaB2FTKwXHl5V0Nz455XvNAuZMuPlU8xEuAm7FRjGYJtk1Yjd5f6bD1UXoCyAod952DYpaCsuin5mrQvYdmIS7Uv6dtwnlO2emFxG6w4PVe7EbCLmrwcpbyYrbKqTBMKV8StHyBWOKN8r542vq6OkrHoas3m8xGFDwyRiNtrmE1sux5HmM2sq%2FpNR07UfsJsjEGwyoQKSJcpFCjhK8FRVOYVcs0pesTWXcfVFLuOFHE1nUWtrjeuxni62r7WyeeobGrNtiUVJxGwVVsltho6dGSi0JE7eCWKOb7QES7vLAJ6Z4eOhKmEKFTXu%2FkrNoRwgEyWYOM8OavKKMcHlftK0liD1H08Hbw9x0xs38If3vqPbco4D%2BvMM0p862AfRIG3myh3OKzpBCt92ex5SvaX6OaxxV%2BimQFyLFnQXsPFOZgcGmh6k1rUslrzqnenyjivPkB8U67FkX9Q11WXP0XeWAMJ3XjFpBsPQftRAXbGCi8MQbm5rmCt%2Bm1Nt8bamm46NeGFpSiJ7gleKOLh7YWcK%2Fa0Sz7RJngad0HdHsL7hSZWdQc7YeWtV4xNztm2Zqicf%2Bup73nxSE3qWO62wp%2FYFt%2FnQTRJz5YUWeGYdXu6UIKe7xxZTYnxyO99QfTG2EoyGekZXVn6GUrm8sb2llIUFZatXqesUEVUvMcTViSFhrDACOpMb7EKatxuueWaWMQkOVrZ9n%2BdtSGwEsHRueXM6lS65fag7am2oqlQLcDYVeijkqTuXhA36XXb1a2qSK4frj4%2FwLj%2FBraN6sgT1xQbUtV5WdE%2BXgI1WjGsA3vxsa%2FoIIfPFU2b3IufduXFXzfOLGt4EpmBRc8llRfQYZzzWbUuZOecaHD5dkrZNS6O8yRfWcJbljSUiWGinCJir0nd3PXdOqE22qrOHbxO0JIUg40Bbuu8xtSa%2FqydfDYcye%2F6x4rl5Smfm0%2FdyuZTwyCCu1Wzrm0ggZTtDt3rVlT26MKaumZjt5Q0%2FD14yVS4KazrnxMXt7kdR6jGrtsHnZm8oUI1U0XIuas%2B6PIYbkUHdK3WnM8gUe0g0bTcHKSpWb7k%2B%2Fr3FrfP3IEYAdfKDc3a%2Bj2y1tl06GBKntlkpsao%2B8v13fkO4%2Bt0NQwT71VGhERM%2FV8gk8xm4Axr1xhNUePzufXZ5H6RSFHTJyT2B9v8zFaEZj930MJ2q%2FcdtD7DAO0Kn44a%2FUwiCQP0a8pbD7f670FEu7J1g54nKDHxejU2UODE5OQDnHz1j0H8agmVW4eOipa9nlwIoc3abBrj1Q0T%2B4SYQboOPwxSKdIiL1wcHVBQZoqL7c2em%2BmZfb%2FSRGc%2FZuaOcukWdthMWXN4rzZjKgkF3KTNGMwU2Lr7iHa0L34w8mxrIJ0N25au1c5dlabdrQeKN3QtOl%2BrtEkD%2BBefHsOkibJgtFhFPn8JN0k4d%2Fl%2F%3C%2Fdiagram%3E%3C%2Fmxfile%3E)

## Структура проекта

1. **`bot_instance.py`** - создаёт и настраивает экземпляры бота и диспетчера.
2. **`handlers.py`** - обрабатывает команды и сообщения от пользователей и администраторов.
3. **`callback.py`** - обрабатывает inline-кнопки и колбэки.
4. **`config.py`** - настройки бота, такие как токен и путь к базе данных.
5. **`keyboards.py`** - определяет клавиатуры для взаимодействия с пользователями.
6. **`states.py`** - хранит состояния FSM для процесса создания вопроса и отправки ответа.
7. **`text.py`** - текстовые сообщения, которые бот отправляет пользователям и администраторам.
8. **`sql_command.py`** - взаимодействие с базой данных, включая добавление вопросов и управление сменами администраторов.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone <URL_РЕПОЗИТОРИЯ>
   cd <директория_проекта>
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Настройте файл конфигурации `config.py`:
   - Укажите ваш Telegram **`BOT_TOKEN`**.
   - Настройте путь к базе данных **`DATABASE_PATH`** (по умолчанию это `bot/db/database.db`).

4. Создайте базу данных и таблицы, если они ещё не созданы. Используйте SQLite или выполните необходимые команды для создания таблиц.

## Запуск

Для запуска бота выполните команду:

```bash
python bot/init.py
```

После этого бот начнёт прослушивать обновления и будет готов к работе.

## Основные функции

- **Пользователь**:
  - Задать вопрос: Пользователь может отправить сообщение через кнопку "❗ Задать вопрос ❗".
  - Получить статус отправленного вопроса: после отправки вопроса пользователю будет показано уведомление о том, что вопрос передан в службу поддержки.

- **Администратор**:
  - Начать/закончить смену: Администратор может начать или завершить смену с помощью кнопок "💼 Начать смену 💼" и "🏁 Закончить смену 🏁".
  - Ответить на вопрос пользователя: Когда пользователь задаёт вопрос, администратор может выбрать его и ответить.

## Команды

### Для пользователей:
- **/start**: Приветственное сообщение и кнопки для общения с администратором.


### Для администраторов:
- **/admin**: Приветственное сообщение и кнопки для управления сменой.
- **/startshift**: Начало смены администратора.
- **/endshift**: Завершение смены администратора.

## База данных

Бот использует SQLite для хранения информации о пользователях, администраторов и вопросах. В базе данных должны быть следующие таблицы:

1. **`admins`**:
   - `id`: ID администратора.
   - `name`: Имя администратора.
   - `shift`: Статус смены (0 - не на смене, 1 - на смене).

2. **`user_questions`**:
   - `user_id`: ID пользователя.
   - `question`: Текст вопроса пользователя.

## Структура базы данных

Примерная структура базы данных SQLite:

```sql
CREATE TABLE admins (
    id INTEGER PRIMARY KEY,
    name TEXT,
    shift INTEGER
);

CREATE TABLE user_questions (
    user_id INTEGER PRIMARY KEY,
    question TEXT
);
```

## Разработчики

- **Разработчик 1**: [Positivezlk](https://github.com/Positivezlk), [Герасимов Кирилл](https://t.me/quttei)
- **Разработчик 2**: [Романенко Никита](https://t.me/ArchangelGreenWoods)
