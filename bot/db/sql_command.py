import aiosqlite
from config import DATABASE_PATH

async def add_new_user_question(user_id, question):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("INSERT INTO user_questions VALUES (?, ?)", (user_id, question))
        await db.commit()


async def output_list_admin():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        cursor = await db.execute("SELECT id FROM admins")
        list = [row[0] for row in await cursor.fetchall()]
        return list
    
async def output_name_admin(id):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        cursor = await db.execute("SELECT name FROM admins WHERE id = ?", (id,))
        name = await cursor.fetchone()
        return name[0]
    
async def set_shift_admin(id, value):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        if value == 1:
            await db.execute("UPDATE admins SET shift = 1 WHERE id = ?", (id,))
        elif value == 0:
            await db.execute("UPDATE admins SET shift = 0 WHERE id = ?", (id,))
        await db.commit()

async def check_shift_admin(id):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        cursor = await db.execute("SELECT shift FROM admins WHERE id = ?", (id,))
        shift = await cursor.fetchone()
        return shift[0]
    
async def output_all_id_questions():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        cursor = await db.execute("SELECT user_id FROM user_questions")
        list = [row[0] for row in await cursor.fetchall()]
        return list
    

async def add_to_existing_question(user_id, question):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("UPDATE user_questions SET question = question || '\n\n' || ? WHERE user_id = ?", (question, user_id))
        await db.commit()


async def output_admins_on_shift():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        cursor = await db.execute("SELECT id FROM admins WHERE shift = 1")
        list = [row[0] for row in await cursor.fetchall()]
        return list


async def output_user_question(user_id):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        cursor = await db.execute("SELECT question FROM user_questions WHERE user_id = ?", (user_id,))
        question = await cursor.fetchone()
        return question[0]
