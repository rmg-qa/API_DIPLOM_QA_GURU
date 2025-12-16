response_create_pet = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "category": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                }
            },
            "additionalProperties": False,
            "required": [
                "id",
                "name"
            ]
        },
        "name": {
            "type": "string"
        },
        "photoUrls": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "name": {
                        "type": "string"
                    }
                },
                "additionalProperties": False,
                "required": [
                    "id",
                    "name"
                ]
            }
        },
        "status": {
            "type": "string"
        }
    },
    "additionalProperties": False,
    "required": [
        "id",
        "category",
        "name",
        "photoUrls",
        "tags",
        "status"
    ]
}
get_pet = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "category": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                }
            },
            "additionalProperties": False,
            "required": [
                "id",
                "name"
            ]
        },
        "name": {
            "type": "string"
        },
        "photoUrls": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "name": {
                        "type": "string"
                    }
                },
                "additionalProperties": False,
                "required": [
                    "id",
                    "name"
                ]
            }
        },
        "status": {
            "type": "string"
        }
    },
    "additionalProperties": False,
    "required": [
        "id",
        "category",
        "name",
        "photoUrls",
        "tags",
        "status"
    ]
}
delete_and_put_pet_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "code": {
            "type": "integer"
        },
        "type": {
            "type": "string"
        },
        "message": {
            "type": "string"
        }
    },
    "additionalProperties": False,
    "required": [
        "code",
        "type",
        "message"
    ]
}
