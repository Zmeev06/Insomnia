import asyncpg
import logging
import asyncio

from data import config

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    # level=logging.DEBUG,  # Можно заменить на другой уровень логгирования.
                    )

async def create_db():
    create_db_command=open('create_db.sql', 'r').read()

    logging.info('Connecting to database')
    con:asyncpg.Connection=await asyncpg.connect(
        user=config.PG_USER,
        password=config.PG_PASS,
        host=config.host
    )

    await con.execute(create_db_command)
    logging.info('Create table')
    await con.close()

async def create_pool():
    return await asyncpg.create_pool(
        user=config.PG_USER,
        password=config.PG_PASS,
        host=config.host
    )

if __name__=='__main__':
    loop=asyncio.get_event_loop()
    loop.run_until_complete(create_db())

