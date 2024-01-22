class Collidable:
    # Initialize the object with its position and dimensions
    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height

    # Check if this object collides with another object
    def collides_with(self, other):
        x, y = self.position
        other_x, other_y = other.position
        other_width, other_height = other.width, other.height

        # Return True if the objects overlap, False otherwise
        return not (other_x + other_width < x or 
                    other_x > x + self.width or 
                    other_y + other_height < y or 
                    other_y > y + self.height)
