from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        gunman = cast.get_first_actor(GUNMAN_GROUP)
        attackers = cast.get_actors(ATTACKER_GROUP)
        for attacker in attackers:
            attacker_body = attacker.get_body()
            gunman_body = gunman.get_body()

            if self._physics_service.has_collided(attacker_body, gunman_body):
                bounce_sound = Sound(BOUNCE_SOUND)
                over_sound = Sound(OVER_SOUND)
                cast.remove_actor(GUNMAN_GROUP, gunman)
