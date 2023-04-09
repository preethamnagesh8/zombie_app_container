from django.shortcuts import render
from django.db import connection

# Create your views here.

from .models import ZombieAttack

def zombie_attack_list(request):

    # Filter zombie attacks based on search query
    query = request.GET.get('q')
    if query:
        with connection.cursor() as cursor:
            # cursor.execute("SELECT location, date, zombie__name FROM zombie_app_zombieattack where location LIKE '%{0}%'".format(query))
            cursor.execute("SELECT location, date, zombie_id FROM zombie_app_zombieattack INNER JOIN zombie_app_zombie ON zombie_app_zombieattack.zombie_id = zombie_app_zombie.id WHERE location LIKE '%{0}%'".format(query))
            zombie_attacks = cursor.fetchall()
    else:
        with connection.cursor() as cursor:
            cursor.execute("SELECT location, date, zombie_id FROM zombie_app_zombieattack INNER JOIN zombie_app_zombie ON zombie_app_zombieattack.zombie_id = zombie_app_zombie.id")
            zombie_attacks = cursor.fetchall()

    return render(request, 'zombie_app/zombie_attack_list.html', {'zombie_attacks': zombie_attacks})