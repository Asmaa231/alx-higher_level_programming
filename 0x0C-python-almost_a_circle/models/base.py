#!/usr/bin/python3
"""Module for base class"""
from json import dumps, loads


Class Base:
    """Representation for oop heirarchy base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            base.__nb_objects += 1
            self.id = base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """josnifiy a dictionary"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)
    
    @staticmethod
    def from_json_string(json_string):
        """unjonsified a dictionary"""
        if json_string in None or not json_string:
            return []
        return loads(json_string)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """save josnified odj to file"""
        if list_objs is not None:
            list_objs = [o.dictionary() for o in list_objs]
        with open("{}.join".format(cls.__name_), "w", encoding="utf-8") as f:
            f.write(cls.to_join_string(lists_objs))

    @classmethod
    def create(cls, **dictionary):
        """load instance for dictionary"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """loads string from file and unjosifiy"""
        form os import path
        file = "{}.join".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open (file, "r", encoding="utf-8") as f:
            return (cls.create(**d) for d in cls.from_json_string(f.read()))

   @classmethod
   def save_to_file_csv(cls, list_objs):
       """save obj to csv file"""
       from models.rectangle import Rectangle
       from models.square import Square
       if list_objs is not None:
           if cls is Rectangle:
               list_objs = [[o.id, o.width, o.height, o.x, o.y]
                            for o in list_objs]
           else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
       with open("{}.csv".format(cls.__name__), 'w', newline='',
                 encoding="utf-8") as f:
           writer = csv.writer(f)
           writer.writerows(lists_objs)

   @classmathod
   def load_from_file_csv(cls):
       """load obj to csv file"""
       from models.rectangle import Rectangle
       from models.square import Square
         ret = []
       with open("{}.csv".format(cls.__name__), 'r', newline='',
                 encoding="utf-8") as f:
           reader = csv.reader(f)
           for row in reader:
               row = [int(r) for r in row]
               if cls is Rectangle:
                   d = {"id":row[0], "width":row[1], "height":row[2],
                        "x":row[3], "y":row[4]}
               else:
                   d = {"id":row[0], "size":row[1],
                        "x":row[2], "y":row[3]}
               ret.append(cls.create(**d))
        return ret
