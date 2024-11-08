# Support Telegram Bot

## Описание

Этот бот служит для автоматизации работы службы поддержки, позволяя пользователям задавать вопросы, а администраторам — отвечать на них. Он предоставляет интерфейс для начала и окончания смены для администраторов, а также возможность пользователям задавать вопросы и получать ответы от администрации. 

Бот использует библиотеку `aiogram` для взаимодействия с Telegram API, а также SQLite для хранения данных пользователей и администраторов.

## Код создан на основе IDeF0 диаграммы

[ссылка на диаграмму](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=support-tg-bot.drawio#R%3Cmxfile%3E%3Cdiagram%20name%3D%22%D0%A1%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0%20%E2%80%94%201%22%20id%3D%22VsIl_wmOL8zB-NCBbUsj%22%3E7V1Zk6O6Ff41fuwuxGZ4dHtJUnUnNcmkKnfyxtiMm1y36dj0dPf99WGR4OhIAoxZbOMXCmSQhY7O8p1FTIz5y8dfDt7r85dw4%2B8murb5mBiLia67rh4fk4bPrMEy7axhewg2WRMpGr4Ff%2Fq0UaOtb8HGP3I3RmG4i4JXvnEd7vf%2BOuLavMMhfOdv%2Bxnu%2BH999ba%2B0PBt7e3E1n8Hm%2Bg5a3X0adH%2BVz%2FYPrN%2FJrab%2FfLisZvpmxyfvU34DpqM5cSYH8Iwys5ePub%2BLpk7Ni%2FZcyvFr%2FnADv4%2BqvPA7vd35%2Bs%2F1v9cLV%2B%2Ff%2F5995%2Ft9l9fHmgvv7zdG33hyUKbzNLjk5Uen8C5MVmQiaOl59lxHj%2BdnpD0uExv0NPG%2BISwHuJzIz232c1xyxN7dsWejY8mOFrg77IHZ%2BnRoTMafTIyHcK3%2FcZP3lSbGE%2Fvz0Hkf3v11smv7%2FG6jNueo5ddfEXiU%2FrO%2FiHyP5STSXISxUvbD1%2F86PAZ30If0A1KVbqsiUuv34tFQhjln8ECsWmbR9flNu%2B6IF18Qql3AiV1KSXdGZjaBSVOQc8Zo1LevmC0jVtWjD4mnfWC7LKFUBw1gT7xTEc8EbxdsN3H5%2Bt4xv1D3JDQI4gZb0Z%2FeAk2m%2BTxp4N%2FDP70fqRdJdR9DYN9lE6f9TSxFklfb1F4zERH0vUxOoR%2F%2BPNwF8b9LvbhPunlZ7Db4aZwH1GJo1vtrAti8uvCEJeFoUmWhdnVsjDEZYFp4%2B83s0RSJsTYecdjsOYpxfNW9ri%2FEcRm5RSBObAkU8DaDv7Oi4JffPeyeaH%2F8DVZDoACNk%2BBXP6yLo7h22Ht06egvEQdYRYXOoq8w9aPhI5SMuWv3ZxyppyhdcDQK8CFS8rKusYLYnuXMN4m%2BBWfbpNTQeJm4jnj3Clo14EoQAohEw5Z1%2FHLwd6vgvNb4HS8zDSJAuiV062xcbplu49TwlHBNqxmzC7ry0V9dczv9tjopxvxnNu8uiSNhbXQVz7Mnug3HRv9DAuJQFLQ4FT6mXp1Xx3Tz5Hr2yXQf7kWzDEOsJjpZaV%2B7kohL0eukE1iVmtkGSTrTCO7woqaff0bg8ZwncwAMReiBee9JAB2%2F%2BP4ms6UZAGJC%2BJ0yE5X8ajXUA7jsT4azKpjAxiRWsEQuqlNgDvq2yAgCueaCdxhC%2BCGsYGXxeFdLwhypawJVoD9v7fEi5g6NB4yzpnFNzivH5nAoD9zCkcH6kUD%2FzwXfHGZHHEFV5HOnipDg%2B0NeA4GY7PhpRMp8SI2UKH5%2Bbz7d8nJC4k8B1RYgLnN5xzKcahBoI1RNv5rEOLAJ%2Be05KrFMl2zRJlOSuRZ%2BzJd4attbzFcBanboC3D%2B5S2rlOPtEZnpJX4WxPSQkk643gVS64pILYNzldAzCFQYQNYQkDc5UrWQQ9ueNMU7ThDtjA6s%2BN0kRiJCfaNXoaH6DnchntvtyxakeFW3PNbGL7SSf6vH0WfdPaS%2BeepG0%2FX4fN3%2Bnx68T25eLTY5eID%2Frj4PNFGjN8nNcbKOIKisszYKrvRlZO0tjl5Hn3kxpp7Pi7P4VYeWssNGI3epvAJIM%2FCDDQugdyYMTOoltZPiPqb98PfdScHlAxMg%2FT04UkeUYHrqoR7lOyuPWqWOz0PfbBbwp8%2Fj343eEAR0YEC3ZH4meR2twVWA1wTFnMwENC4ZHg%2FbneFxx3wIHQ8lHgJ2F%2FocNgLmYWSQx0R5DBggZfo0MF8y5FYiL0G88nogjkEOZNtYjZ2JmN6yvrqGvtLojmtqRO5toAcuuLxQd4p8yNA8cJpF2iVQq1llusYcUT66hhPcXTNULQNyVJDsJi9CpbRRakw%2FLfdhu5EoSOz3%2FgwUQSoxMQ7JAAcoH41IE9WapFQI%2BSQdtnE1MhCVTVN2nndsfAvXGZx50LSkd%2BM5aHoactMGhpyk46uWj4WYnYJhsdmgo4BemdNfvwQWFjcZBdWnMZn7uWRpZohSvlLjFWSWzjj07JFn4Iuiw1NO%2FMp2KLsHodPgWKGSp%2BCbsmJ2pNPQaJsF1eYwnedLgO7lJ8ftEdN1%2FmMIZYNf8EuBDGlQG0DnAkIGmB6UbWz89MUWiWDDOwwsAi2KYd2GDAzfjx2vSRj09EamvaSvqZWv9a9rggc3bx1f4K9PJSNDwtcSqx12M9cMTe5oGv63uqIn4RaU17QorHkEcUqcUvnbNT2v4kiio4ku1Aq7rqz%2FuXhhBkRVD2jYLEAYQoQxJA6v9izRxgPYQaCiw2FKJZA7MAYg3sCoi9hznxo%2BRImwCgxZS8E%2BdZR2x%2BN4TwysPnCOnlg5V6DczZToiIcayphSlmYvzM7zDBHCsl1qyYkN4whIbmpMLOghQStKFGPowJZuSjIMXwd1Xpa1t5VgvGMLcri92SKsvcvHYrrkhBtmcGORH1mXEI8DBXWUNpkYFydG1UMhA1fVS8Jutw2rnYsEQs3LaGW9eWgvrrG1QqPWXcGbj3rFnI%2BTPeBI5Ja5jXB4KjtwqnLpwXbjkSOGBIe6m4bhtGV8TjINncbCxHUkdNzGY%2BhyAyFSNqUKFPIuwVrwjTunMXn7BHRQ4TlBqoHgn3Vt16XAIznnjCEn6UiEP6F6FBiQ%2Bfe9o6gL1pSWgouhQi6V4vLlAjGUSBog0LTSgRtKkjaE4JWZzHfEXR3CDpji1IEbZvnKe7uMbNxSpDrnPD1qVErDSROtbITA3sFSbH%2FnKndDP%2BDX88duakAK2jGUCf5aGEnZ9aiZuG9gb0JhCB3glPXnYBTRNuDAePL68f7sREN2%2B91gYDQlduzL8EY3xZNuHYam31Nk6f73ovBUKTiESD5mEuGk6YQ5SwY4kuRUAGeRExWApXEnAC5DdSuQAaaK0%2Fvaqhu3NOSF9qFbPm5chQjAW7CTjWWIeg2aTZyd6HP1l3lBSgrcNh3DoadC8qqi5IvSfoSFo04V%2FqSvhXnKWmrZya3wYzTU6UbAbuoydNRypPZKrPKNCFxRdz6AWKFE9L36knjy6ooGYus1mw%2BHlHYwBCJuL262cSy63G42cy6ot905ETtx83GFggWmVAA6TKBAjl8JRiKyrhCLjlFi9i6ab%2BaYteRwq%2BmM6%2FV5frV2Jqu1q914jkqnVqzbEm1kgjYqq0SWw3tOjKR68gdPBPFHJ%2FrCKd3Fg69k11HQleCF6rr3fwVG0I4gCdLsHEenFVFlOOTyn0lqa9Baj4eX709t5jYvoU%2FvPUf23ThPKwzyyixrYN9EAXebqLc4bCmEay0ZbPxlOwv0c2wxS%2FRzAA5lsxpr%2BHkHEwODRS9STVqWa551btTYZxnH6B1Uy7FkX1Q11SXjyIvrIGEbjxj0o2HoP6oADtjhReGINxcV9BW%2FZamW2MtTTedmvDCUqRE9wQvFP7w9lzOFXvaJUe0CZ7G3VC3hvB2oYlVXcFOWHrrBWOTU7atGSrm33roe14MqUkey81m%2BBPb4us8iCap2ZIiK%2Byzbk8WStDzjSOrKTEe%2Bb0viN4YW0k6Iz2jK0s%2FQcicX9jeUoiiQrPVq5QVsoiK93jCgqSQEBZoQZXpLWZBjdsst1wTs5gkRivb%2Fq%2BzMgSWIjg6s5xpnUqz3B60PNVWFBWqGRibCn1kktTdC%2BIqrW67ulQV8fXDxccH2Oq%2Fgm2jOrLENcWGVHVeVtSP50CNVhTrwFZ8bCs6yOBzRdUmt%2BKnXVnxl40zywqexMXAvOeSzAtoMM75qFoXvHOKN7h8O6XsHhf7eZKfLOEtSwrKRDdRThGx1qRu7PpmjVAbbVXnDp4naEmSwcYAt3VeYmpNP2sn7w178rv%2BWLE8PeW%2B%2BdS1bD41DCK4WTHr2gZiSNnu0L1uRWWPzq2pazY2S0nD78FLusJFYV1%2FTlzc5nYcrhq7bh10pvKGctVMFS7nruqgy324FRXQtUpz7k6i2k6iabk6SEOzfMr35e8tbp%2B4AzECrpUbmrX1PbLWl%2BnQzpQ8sslUjVH3y%2FXd2Q7jq3Q1DBPvVUaEQEz9L5BJejNwhLVrjKbI8blvfTa5XSRS5PQJgf3BNj%2BzFa7Z%2Bw5aWG%2F1voPW3Q3QLvPpqNDPJBI3QL%2BqvHV3q%2F8RRLQqWzfodYISE6tXYw0FTkwuPsHFV%2F8QxK%2BWULl16Kgo2evJhBDKrM2mPl7dMLFNiBdI1%2B6HQTJFWlwLZ3sHFJSZ4mR7s%2BdieqbfLzTQ2Y%2BauaFYuoUNNlNWHN6rzphKXAFXqTMGUwW27j6iHe2LD0aerA2kvWHd0rXYuanUtJu1QPGGrkXla5U06Qz%2BTSXOJKXCuqVPm90%2FXAzBMAfNoX%2Fn%2FuHiPjcKsyU7GbRVGxpfHsKkqLpQPLHJ9Pwl3CThneX%2FAQ%3D%3D%3C%2Fdiagram%3E%3C%2Fmxfile%3E)

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

- **Разработчик 1**: [Positivezlk](https://github.com/Positivezlk)
- **Разработчик 2**: Название/контакт
