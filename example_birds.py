# ----------------------------------------------------------------
class MainBird(object):
    import GlobalSurface
    # из-за того что снаружи нельзя сказать летает птица или нет приходится заводить флаг
    is_flight_available = True
    is_takeoff_available = None
    x = None
    y = None
    z = None
    speed = 1
    bird_type = None
    status = None

    def fly(self):
        # классический сайд эффект - если кто то напорет с is_takeoff_available то птица начнет летать невпопад
        # так же мы поимеем боли когда кроме типа земли что то еще начнет влиять на полет
        self.speed = 2
        if self.is_takeoff_available:
            self.status = 'fly'
            print 'i`m fly'

    def move(self, x, y, z):
        # если птица еще находится в "нигде" то вызов полета тоже будет некорректен но не упадет если не нафаршивать его дополнительным кодом
        if GlobalSurface.get_type_surface(x, y) == 'ground':
            self.is_takeoff_available = True
        self.x = x
        self.y = y
        self.z = z


class Penguin(MainBird):
    bird_type = 'penguin'
    def fly(self):
        raise Exception('иди нахуй')

class Sparrow(object):
    bird_type = 'sparrow'


sparrow = Sparrow()
sparrow.move(0,0,0)
sparrow.fly()

# кстати сразу проблема на будущее - мы смогли переместить птиц в одну точку)
penguin = Penguin()
penguin.move(0,0,0)
penguin.fly()

# ----------------------------------------------------------------
# терпимый к ошибкам вариант, сам по себе порождает больше ошибок но кода писать меньше
import GlobalSurface
class Bird(object):
    fly_method = Null
    # сразу подумали о том что причин не полететь может быть несколько
    fly_available_methods = []
    x = None
    y = None
    z = None
    speed = None
    bird_type = None

    def configure_fly(fly_method, fly_available_methods=[]):
        self.fly_method = fly_method
        self.fly_available_methods = fly_available_methods
        print('fly methods updated')

    def fly():
        if not fly_method:
            print 'has no fly_method, try configure_fly'
            return

        for cb in fly_available_methods:
            if not cb(x=x, y=y, z=z, speed=speed):
                print ' %s return false' % cb.__name__
                return

        self.speed = fly_method(x, y, z, speed, self.move)

    def move(x, y, z):
        self.x = x
        self.y = y
        self.z = z

def fly(x, y, z, speed, move_cb=Null):
    # хочу отметить что летать этим методом может не только птица
    if move_cb:
        move_cb(x, y, z+1)
    return speed * 2

# обратите внимание, что GlobalSurface резко стало можно сделать несколько штук не ломая вообще ничего
# это условие при котором можно смело плодить синглтоны и статику - как только начнут мешать просто убрать в нескольких местах
def check_surface(x, y, z, speed):
    return GlobalSurface.get_type_surface(x, y) == 'ground':
        
sparrow = new Bird()
sparrow.bird_type = 'sparrow'
sparrow.fly_available_methods.append(check_surface)
sparrow.fly_method = fly
sparrow.move(0,0,0)
sparrow.fly()


penguin = new Bird()
penguin.bird_type = 'penguin'
penguin.move(0,0,0)
# и вот прямо тут очевидно что лететь он не может, очевидно СНАРУЖИ сущности которая спрятала неважные подробности которые скорее всего менять не прийдется

# ----------------------------------------------------------------
# нетерпимый к ошибкам вариант (мой любимый, если не упало - точняк работает)
import GlobalSurface
class Bird(object):
    fly_method = Null
    # null явно заставляет падением сконфигурировать условия полета и заменяет собой метод configure_fly
    fly_available_methods = None
    x = None
    y = None
    z = None
    speed = None
    bird_type = None

    def fly():
        if not fly_method:
            raise Exception('has no fly_method')

        if not fly_available_methods:
            raise Exception('has no fly_available_methods')

        for cb in fly_available_methods:
            if not cb(x=x, y=y, z=z, speed=speed):
                print ' %s return false' % cb.__name__
                return

        self.speed = fly_method(x, y, z, speed, self.move)

    def move(x, y, z):
        self.x = x
        self.y = y
        self.z = z

def fly(x, y, z, speed, move_cb):
    # не перезали move_cb упало естесственым образом
    move_cb(x, y, z+1)
    return speed * 2

def check_surface(x, y, z, speed):
    return GlobalSurface.get_type_surface(x, y) == 'ground':
        
sparrow = new Bird()
sparrow.bird_type = 'sparrow'
sparrow.fly_available_methods.append(check_surface)
sparrow.fly_method = fly
sparrow.move(0,0,0)
sparrow.fly()


penguin = new Bird()
penguin.bird_type = 'penguin'
penguin.move(0,0,0)