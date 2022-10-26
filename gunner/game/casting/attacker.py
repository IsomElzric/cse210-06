from game.casting.actor import Actor


class Attacker(Actor):
    """A solid, rectangular object that can be broken."""

    def __init__(self, body, animation, points, debug = False):
        """Constructs a new Brick.
        
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._points = points
        
    def get_animation(self):
        """Gets the brick's image.
        
        Returns:
            An instance of Image.
        """
        return self._animation

    def get_body(self):
        """Gets the brick's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_points(self):
        """Gets the brick's points.
        
        Returns:
            A number representing the brick's points.
        """
        return self._points

    def move_next(self):
        """Moves the Attacker using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)