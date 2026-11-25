#!/usr/bin/python3
"""Provide object identifiers and JSON persistence for geometry models."""

import json


class Base:
    """Assign a model identifier and persist model data as JSON."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Use the supplied identifier or allocate the next automatic one."""
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        """Write model dictionaries to the JSON file for this class."""
        dictionaries = [obj.to_dictionary() for obj in (list_objs or [])]
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as stream:
            stream.write(cls.to_json_string(dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Convert JSON text to a list, treating missing input as empty."""
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """Create a shape and apply the given attributes through update."""
        from models.square import Square

        instance = cls(1) if issubclass(cls, Square) else cls(1, 1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Restore instances from this class's file, if present."""
        try:
            with open(cls.__name__ + ".json", encoding="utf-8") as stream:
                dictionaries = cls.from_json_string(stream.read())
        except FileNotFoundError:
            return []
        return [cls.create(**attributes) for attributes in dictionaries]
