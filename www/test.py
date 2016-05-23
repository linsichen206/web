#import orm,asyncio,sys
#from models import User, Blog, Comment

#async def test(loop):
#    await orm.create_pool(loop=loop,user='www-data', password='www-data', db='awesome')

#    u=User(name='test11',email='test11@test.com',passwd='test',image='about:blank')

 #   await u.save()

#if __name__ == '__main__':

 #   loop = asyncio.get_event_loop()
####    loop.run_until_complete( asyncio.wait([test( loop )]) )  
 ###   loop.close()
 ##   if loop.is_closed():
 #       sys.exit(0)

import orm
from models import User, Blog, Comment

def test():
    yield from orm.create_pool(user='www-data', password='www-data', database='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()
